from pydantic import Field, validator
import json
from ayon_server.settings import BaseSettingsModel
from ayon_server.exceptions import BadRequestException
from .publishers_model import ModelPublishSetting, DEFAULT_MODEL_PUBLISH_SETTING
from .publishers_rig import RigPublishSetting, DEFAULT_RIG_PUBLISH_SETTING
from .publish_playblast import ExtractPlayblastSetting, DEFAULT_PLAYBLAST_SETTING


def linear_unit_enum():
    """Get linear units enumerator."""
    return [
        {"label": "mm", "value": "millimeter"},
        {"label": "cm", "value": "centimeter"},
        {"label": "m", "value": "meter"},
        {"label": "km", "value": "kilometer"},
        {"label": "in", "value": "inch"},
        {"label": "ft", "value": "foot"},
        {"label": "yd", "value": "yard"},
        {"label": "mi", "value": "mile"}
    ]

def angular_unit_enum():
    """Get angular units enumerator."""
    return [
        {"label": "deg", "value": "degree"},
        {"label": "rad", "value": "radian"},
    ]

class CollectMayaRenderModel(BaseSettingsModel):
    sync_workfile_version: bool = Field(title = "Sync render version with workfile")


class CollectFbxCameraModel(BaseSettingsModel):
    enabled: bool = Field(title="CollectFbxCamera")


class CollectGLTFModel(BaseSettingsModel):
    enabled: bool = Field(title="CollectGLTF")


class ValidateInstanceInContextModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateInstanceInContext")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ValidateContainersModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateContainers")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ValidateFrameRangeModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateFrameRange")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")
    exclude_families: list[str] = Field(
        default_factory=["model", "rig", "staticMesh"],
        title="Families"
    )

class ValidateShaderNameModel(BaseSettingsModel):
    """
    Shader name regex can use named capture group asset to validate against current asset name.
    """
    enabled: bool = Field(title="ValidateShaderName")
    optional: bool = Field(title="Optional")
    regex: str = Field("(?P<asset>.*)_(.*)_SHD", title="Validation regex")


class ValidateShadingEngineModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateShadingEngine")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ValidateAttributesModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateAttributes")
    attributes: str = Field("{}", title="Attributes",
    widget="textarea")
    @validator("attributes")
    def validate_json(cls, value):
        if not value.strip():
            return "{}"
        try:
            converted_value = json.loads(value)
            success = isinstance(converted_value, dict)
        except json.JSONDecodeError:
            success = False

        if not success:
            raise BadRequestException(
                "The attibutes can't be parsed as json object"
            )
        return value


class ValidateLoadedPluginModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateLoadedPlugin")
    optional: bool = Field(title="Optional")
    whitelist_native_plugins : bool = Field(title="Whitelist Maya Native Plugins")
    authorized_plugins: list[str] = Field(default_factory=[], title="Authorized plugins")


class ValidateMayaUnitsModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateMayaUnits")
    optional: bool = Field(title="Optional")
    validate_linear_units: bool = Field(title="Validate linear units")
    linear_units: str = Field(enum_resolver=linear_unit_enum, title="Linear Units")
    validate_angular_units:  bool = Field(title="Validate angular units")
    angular_units: str = Field(enum_resolver=angular_unit_enum, title="Angular units")
    validate_fps: bool = Field(title="Validate fps")


class ValidateUnrealStaticMeshNameModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateUnrealStaticMeshName")
    optional: bool = Field(title="Optional")
    validate_mesh: bool = Field(title="Validate mesh names")
    validate_collision: bool = Field(title="Validate collison names")


class ValidateCycleErrorModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateCycleError")
    optional: bool = Field(title="Optional")
    families: list[str] = Field(default_factory=["rig"], title="Families")


# Validate Render Setting
class ArnoldRenderSubMol(BaseSettingsModel):
    _layout = "compact"
    type: str = Field(title="Type")
    value: str = Field(title="Value")


class VRayRenderSubMol(BaseSettingsModel):
    _layout = "compact"
    type: str = Field(title="Type")
    value: str = Field(title="Value")


class RedshiftRenderSubMol(BaseSettingsModel):
    _layout = "compact"
    type: str = Field(title="Type")
    value: str = Field(title="Value")


class RendermanRenderSubMol(BaseSettingsModel):
    _layout = "compact"
    type: str = Field(title="Type")
    value: str = Field(title="Value")


class ValidateRenderSettingsModel(BaseSettingsModel):
    arnold_render_attributes: list[ArnoldRenderSubMol] = Field(
        default_factory=list, title="Arnold Render Attributes")
    vray_render_attributes: list[VRayRenderSubMol] = Field(
        default_factory=list, title="VRay Render Attributes")
    redshift_render_attributes: list[RedshiftRenderSubMol] = Field(
        default_factory=list, title="Redshift Render Attributes")
    renderman_render_attributes: list[RendermanRenderSubMol] = Field(
        default_factory=list, title="Renderman Render Attributes")


class ValidateCurrentRenderLayerIsRenderableModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateCurrentRenderLayerIsRenderable")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ValidateRenderImageRuleModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateRenderImageRule")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ValidateRenderNoDefaultCamerasModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateRenderNoDefaultCameras")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ValidateRenderSingleCameraModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateRenderNoDefaultCameras")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ValidateRenderLayerAOVsModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateRenderLayerAOVs")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ValidateStepSizeModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateStepSize")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ValidateVRayDistributedRenderingModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateVRayDistributedRendering")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ValidateVrayReferencedAOVsModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateVrayReferencedAOVs")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ValidateVRayTranslatorEnabledModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateVRayTranslatorEnabled")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ValidateVrayProxyModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateVrayProxy")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ValidateVrayProxyMembersModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateVrayProxyMembers")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ValidateYetiRenderScriptCallbacksModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateYetiRenderScriptCallbacks")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ValidateYetiRigCacheStateModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateYetiRigCacheState")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ValidateYetiRigInputShapesInInstanceModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateYetiRigInputShapesInInstance")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ValidateYetiRigSettingsModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateYetiRigSettings")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ValidateCameraAttributesModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateCameraAttributes")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ValidateAssemblyNameModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateAssemblyName")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ValidateAssemblyNamespacesModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateAssemblyNamespaces")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ValidateAssemblyModelTransformsModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateAssemblyModelTransforms")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ValidateAssRelativePathsModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateAssRelativePaths")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ValidateInstancerContentModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateInstancerContent")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ValidateInstancerFrameRangesModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateInstancerFrameRanges")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ValidateNoDefaultCamerasModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateNoDefaultCameras")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ValidateUnrealUpAxisModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateUnrealUpAxis")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ValidateCameraContentsModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateUnrealUpAxis")
    optional: bool = Field(title="Optional")
    validate_shapes: bool = Field(title="Validate presence of shapes")


class ExtractMayaSceneRawModel(BaseSettingsModel):
    """Add loaded instances to those published families:"""
    enabled: bool = Field(title="ExtractMayaSceneRaw")
    add_for_families: list[str] = Field(default_factory=["layout"], title="Families")


class ExtractCameraAlembicModel(BaseSettingsModel):
    """
    List of attributes that will be added to the baked alembic camera. Needs to be written in python list syntax.
    """
    enabled: bool = Field(title="ExtractCameraAlembic")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")
    bake_attributes: str = Field("[]", title="Base Attributes", widget="textarea")


class PublishersModel(BaseSettingsModel):
    CollectMayaRender: CollectMayaRenderModel = Field(
        default_factory = CollectMayaRenderModel,
        title="Collect Render Layers",
        section="Collectors"
    )
    CollectFbxCamera: CollectFbxCameraModel = Field(
        default_factory=CollectFbxCameraModel,
        title="Collect Camera for FBX export",
    )
    CollectGLTF: CollectGLTFModel = Field(
        default_factory=CollectGLTFModel,
        title="Collect Assets for GLB/GLTF export"
    )
    ValidateInstanceInContext: ValidateInstanceInContextModel = Field(
        default_factory = ValidateInstanceInContextModel,
        title="Validate Instance In Context",
        section="Validators"
    )
    ValidateContainers: ValidateContainersModel = Field(
        default_factory=ValidateContainersModel,
        title="Validate Containers"
    )
    ValidateFrameRange: ValidateFrameRangeModel = Field(
        default_factory=ValidateFrameRangeModel,
        title="Validate Frame Range"
    )
    ValidateShaderName: ValidateShaderNameModel = Field(
        default_factory=ValidateShaderNameModel,
        title="Validate Shader Name"
    )
    ValidateShadingEngine: ValidateShadingEngineModel = Field(
        default_factory=ValidateShadingEngineModel,
        title="Validate Look Shading Engine Naming"
    )
    ValidateAttributes: ValidateAttributesModel = Field(
        default_factory=ValidateAttributesModel,
        title="Validate Attributes"
    )
    ValidateLoadedPlugin: ValidateLoadedPluginModel = Field(
        default_factory=ValidateLoadedPluginModel,
        title="Validate Loaded Plugin"
    )
    ValidateMayaUnits: ValidateMayaUnitsModel = Field(
        default_factory=ValidateMayaUnitsModel,
        title="Validate Maya Units"
    )
    ValidateUnrealStaticMeshName: ValidateUnrealStaticMeshNameModel = Field(
        default_factory=ValidateUnrealStaticMeshNameModel,
        title="Validate Unreal Static Mesh Name"
    )
    ValidateCycleError: ValidateCycleErrorModel = Field(
        default_factory=ValidateCycleErrorModel,
        title="Validate Cycle Error"
    )
    ValidateRenderSettings: ValidateRenderSettingsModel = Field(
        default_factory=ValidateRenderSettingsModel,
        title="Validate Render Settings"
    )
    ValidateCurrentRenderLayerIsRenderable: ValidateCurrentRenderLayerIsRenderableModel = Field(
        default_factory=ValidateCurrentRenderLayerIsRenderableModel,
        title="Validate Current Render Layer Has Renderable Camera"
    )
    ValidateRenderImageRule: ValidateRenderImageRuleModel = Field(
        default_factory=ValidateRenderImageRuleModel,
        title="Validate Render Image Rule (Workspace)"
    )
    ValidateRenderNoDefaultCameras: ValidateRenderNoDefaultCamerasModel = Field(
        default_factory=ValidateRenderNoDefaultCamerasModel,
        title="Validate No Default Cameras Renderable"
    )
    ValidateRenderSingleCamera: ValidateRenderSingleCameraModel = Field(
        default_factory=ValidateRenderSingleCameraModel,
        title="Validate Render Single Camera "
    )
    ValidateRenderLayerAOVs: ValidateRenderLayerAOVsModel = Field(
        default_factory=ValidateRenderLayerAOVsModel,
        title="Validate Render Passes/AOVs Are Registered"
    )
    ValidateStepSize: ValidateStepSizeModel = Field(
        default_factory= ValidateStepSizeModel,
        title="Validate Step Size"
    )
    ValidateVRayDistributedRendering: ValidateVRayDistributedRenderingModel = Field(
        default_factory=ValidateVRayDistributedRenderingModel,
        title="VRay Distributed Rendering"
    )
    ValidateVrayReferencedAOVs: ValidateVrayReferencedAOVsModel = Field(
        default_factory=ValidateVrayReferencedAOVsModel,
        title="VRay Referenced AOVs"
    )
    ValidateVRayTranslatorEnabled: ValidateVRayTranslatorEnabledModel = Field(
        default_factory=ValidateVRayTranslatorEnabledModel,
        title="VRay Translator Settings"
    )
    ValidateVrayProxy: ValidateVrayProxyModel = Field(
        default_factory=ValidateVrayProxyModel,
        title="VRay Proxy Settings"
    )
    ValidateVrayProxyMembers: ValidateVrayProxyMembersModel = Field(
        default_factory=ValidateVrayProxyMembersModel,
        title="VRay Proxy Members"
    )
    ValidateYetiRenderScriptCallbacks: ValidateYetiRenderScriptCallbacksModel = Field(
        default_factory=ValidateYetiRenderScriptCallbacksModel,
        title="Yeti Render Script Callbacks"
    )
    ValidateYetiRigCacheState: ValidateYetiRigCacheStateModel = Field(
        default_factory=ValidateYetiRigCacheStateModel,
        title="Yeti Rig Cache State"
    )
    ValidateYetiRigInputShapesInInstance: ValidateYetiRigInputShapesInInstanceModel = Field(
        default_factory=ValidateYetiRigInputShapesInInstanceModel,
        title="Yeti Rig Input Shapes In Instance"
    )
    ValidateYetiRigSettings: ValidateYetiRigSettingsModel = Field(
        default_factory=ValidateYetiRigSettingsModel,
        title="Yeti Rig Settings"
    )
    model: ModelPublishSetting = Field(
        default_factory=ModelPublishSetting,
        title="Model"
    )
    rig: RigPublishSetting = Field(
        default_factory=RigPublishSetting,
        title="Rig"
    )
    ValidateCameraAttributes: ValidateCameraAttributesModel = Field(
        default_factory=ValidateCameraAttributesModel,
        title="Validate Camera Attributes"
    )
    ValidateAssemblyName: ValidateAssemblyNameModel = Field(
        default_factory=ValidateAssemblyNameModel,
        title="Validate Assembly Name"
    )
    ValidateAssemblyNamespaces: ValidateAssemblyNamespacesModel = Field(
        default_factory=ValidateAssemblyNamespacesModel,
        title="Validate Assembly Namespaces"
    )
    ValidateAssemblyModelTransforms: ValidateAssemblyModelTransformsModel = Field(
        default_factory=ValidateAssemblyModelTransformsModel,
        title="Validate Assembly Model Transforms"
    )
    ValidateAssRelativePaths: ValidateAssRelativePathsModel = Field(
        default_factory=ValidateAssRelativePathsModel,
        title="Validate Ass Relative Paths"
    )
    ValidateInstancerContent: ValidateInstancerContentModel = Field(
        default_factory=ValidateInstancerContentModel,
        title="Validate Instancer Content"
    )
    ValidateInstancerFrameRanges: ValidateInstancerFrameRangesModel = Field(
        default_factory=ValidateInstancerFrameRangesModel,
        title="Validate Instancer Cache Frame Ranges"
    )
    ValidateNoDefaultCameras: ValidateNoDefaultCamerasModel = Field(
        default_factory=ValidateNoDefaultCamerasModel,
        title="Validate No Default Cameras"
    )
    ValidateUnrealUpAxis: ValidateUnrealUpAxisModel = Field(
        default_factory=ValidateUnrealUpAxisModel,
        title="Validate Unreal Up-Axis Check"
    )
    ValidateCameraContents: ValidateCameraContentsModel = Field(
        default_factory=ValidateCameraContentsModel,
        title="Validate Camera Content"
    )
    ExtractPlayblast : ExtractPlayblastSetting = Field(
        default_factory = ExtractPlayblastSetting,
        title="Extract Playblast Settings",
        section="Extractors"
    )
    ExtractMayaSceneRaw: ExtractMayaSceneRawModel = Field(
        default_factory=ExtractMayaSceneRawModel,
        title="Maya Scene(Raw)"
    )
    ExtractCameraAlembic: ExtractCameraAlembicModel = Field(
        default_factory=ExtractCameraAlembicModel,
        title="Extract Camera Alembic"
    )


DEFAULT_PUBLISH_SETTINGS = {
    "CollectMayaRender": {
        "sync_workfile_version": False
    },
    "CollectFbxCamera":{
        "enabled": False
    },
    "CollectGLTF":{
        "enabled": False
    },
    "ValidateInstanceInContext": {
        "enabled": True,
        "optional": True,
        "active": True
    },
    "ValidateContainers": {
        "enabled": True,
        "optional": True,
        "active": True
    },
    "ValidateFrameRange": {
            "enabled": True,
            "optional": True,
            "active": True,
            "exclude_families": [
                "model",
                "rig",
                "staticMesh"
        ]
    },
    "ValidateShaderName": {
            "enabled": False,
            "optional": True,
            "regex": "(?P<asset>.*)_(.*)_SHD"
    },
    "ValidateShadingEngine": {
            "enabled": True,
            "optional": True,
            "active": True
    },
    "ValidateAttributes": {
            "enabled": False,
            "attributes": "{}"
    },
    "ValidateLoadedPlugin": {
            "enabled": False,
            "optional": True,
            "whitelist_native_plugins": False,
            "authorized_plugins": []
    },
    "ValidateMayaUnits": {
            "enabled": True,
            "optional": False,
            "validate_linear_units": True,
            "linear_units": "cm",
            "validate_angular_units": True,
            "angular_units": "deg",
            "validate_fps": True
    },
    "ValidateUnrealStaticMeshName": {
            "enabled": True,
            "optional": True,
            "validate_mesh": False,
            "validate_collision": True
    },
    "ValidateCycleError": {
            "enabled": True,
            "optional": False,
            "families": [
                "rig"
            ]
    },
    "ValidateRenderSettings": {
            "arnold_render_attributes": [],
            "vray_render_attributes": [],
            "redshift_render_attributes": [],
            "renderman_render_attributes": []
    },
    "ValidateCurrentRenderLayerIsRenderable": {
            "enabled": True,
            "optional": False,
            "active": True
    },
    "ValidateRenderImageRule": {
            "enabled": True,
            "optional": False,
            "active": True
    },
    "ValidateRenderNoDefaultCameras": {
            "enabled": True,
            "optional": False,
            "active": True
    },
    "ValidateRenderSingleCamera": {
            "enabled": True,
            "optional": False,
            "active": True
    },
    "ValidateRenderLayerAOVs": {
            "enabled": True,
            "optional": False,
            "active": True
    },
    "ValidateStepSize": {
            "enabled": True,
            "optional": False,
            "active": True
    },
    "ValidateVRayDistributedRendering": {
            "enabled": True,
            "optional": False,
            "active": True
    },
    "ValidateVrayReferencedAOVs": {
            "enabled": True,
            "optional": False,
            "active": True
    },
    "ValidateVRayTranslatorEnabled": {
            "enabled": True,
            "optional": False,
            "active": True
    },
    "ValidateVrayProxy": {
            "enabled": True,
            "optional": False,
            "active": True
    },
    "ValidateVrayProxyMembers": {
            "enabled": True,
            "optional": False,
            "active": True
    },
    "ValidateYetiRenderScriptCallbacks": {
            "enabled": True,
            "optional": False,
            "active": True
    },
    "ValidateYetiRigCacheState": {
            "enabled": True,
            "optional": False,
            "active": True
    },
    "ValidateYetiRigInputShapesInInstance": {
            "enabled": True,
            "optional": False,
            "active": True
    },
    "ValidateYetiRigSettings": {
            "enabled": True,
            "optional": False,
            "active": True
    },
    "model":DEFAULT_MODEL_PUBLISH_SETTING,
    "rig": DEFAULT_RIG_PUBLISH_SETTING,
    "ValidateCameraAttributes": {
            "enabled": False,
            "optional": True,
            "active": True
    },
    "ValidateAssemblyName": {
            "enabled": True,
            "optional": True,
            "active": True
    },
    "ValidateAssemblyNamespaces": {
            "enabled": True,
            "optional": False,
            "active": True
    },
    "ValidateAssemblyModelTransforms": {
            "enabled": True,
            "optional": False,
            "active": True
    },
    "ValidateAssRelativePaths": {
            "enabled": True,
            "optional": False,
            "active": True
    },
    "ValidateInstancerContent": {
            "enabled": True,
            "optional": False,
            "active": True
    },
    "ValidateInstancerFrameRanges": {
            "enabled": True,
            "optional": False,
            "active": True
    },
    "ValidateNoDefaultCameras": {
            "enabled": True,
            "optional": False,
            "active": True
    },
    "ValidateUnrealUpAxis": {
            "enabled": False,
            "optional": True,
            "active": True
    },
    "ValidateCameraContents": {
            "enabled": True,
            "optional": False,
            "validate_shapes": True
    },
    "ExtractPlayblast": DEFAULT_PLAYBLAST_SETTING,
    "ExtractMayaSceneRaw": {
            "enabled": True,
            "add_for_families": [
                "layout"
            ]
        },
    "ExtractCameraAlembic": {
            "enabled": True,
            "optional": True,
            "active": True,
            "bake_attributes": "[]"
    }
}