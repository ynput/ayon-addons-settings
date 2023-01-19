from pydantic import Field, validator
import json
from ayon_server.exceptions import BadRequestException
from ayon_server.settings import BaseSettingsModel

default_suffix_naming = "{\n    \"mesh\": [\n        \"_GEO\",\n        \"_GES\",\n        \"_GEP\",\n        \"_OSD\"\n    ],\n    \"nurbsCurve\": [\n        \"_CRV\"\n    ],\n    \"nurbsSurface\": [\n        \"_NRB\"\n    ],\n    \"locator\": [\n        \"_LOC\"\n    ],\n    \"group\": [\n        \"_GRP\"\n    ]\n}"


class MultiplatformStrList(BaseSettingsModel):
    windows: str = Field("", title="Windows")
    linux: str = Field("", title="Linux")
    darwin: str = Field("", title="MacOS")


class ValidateModelNameModel(BaseSettingsModel):

    enabled: bool = Field(title="ValidateModelName")
    database: bool = Field(title="Use database shader name definitions")
    material_file: MultiplatformStrList = Field(
        default_factory=MultiplatformStrList,
        title="Material File",
        description=("Path to material file defining list of material names to check.")
    )
    regex: str = Field("(.*)_(\\d)*_(?P<shader>.*)_(GEO)",
    title="Validation regex",
    description=(
        "Regex for validating name of top level group name.You can use named capturing groups:(?P<asset>.*) for Asset name"
        ))
    top_level_regex: str = Field(".*_GRP",
    title="Top level group name regex",
    description=("To check for asset in name so *_some_asset_name_GRP is valid, use:.*?_(?P<asset>.*)_GEO"))


class ValidateModelContentModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateModelContent")
    optional: bool = Field(title="Optional")
    validate_top_group: bool = Field(title="Validate one top group")


class ValidateTransformNamingSuffixModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateTransformNamingSuffix")
    optional: bool = Field(title="Optional")
    SUFFIX_NAMING_TABLE: str = Field(default_suffix_naming,
    title="Suffix Naming Tables",
    widget="textarea",
    description=("Validates transform suffix based on the type of its children shapes."))
    @validator("SUFFIX_NAMING_TABLE")
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
                "The text can't be parsed as json object"
            )
        return value
    ALLOW_IF_NOT_IN_SUFFIX_TABLE: bool = Field(title="Allow if suffix not in table")


class ValidateColorSetsModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateColorSets")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ValidateMeshHasOverlappingUVsModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateMeshHasOverlappingUVs")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ValidateMeshArnoldAttributesModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateMeshArnoldAttributes")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ValidateMeshShaderConnectionsModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateMeshShaderConnections")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ValidateMeshSingleUVSetModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateMeshSingleUVSet")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ValidateMeshHasUVsModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateMeshHasUVs")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ValidateMeshLaminaFacesModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateMeshLaminaFaces")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ValidateMeshNgonsModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateMeshNgons")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ValidateMeshNonManifoldModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateMeshNonManifold")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ValidateMeshNoNegativeScaleModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateMeshNoNegativeScale")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ValidateMeshNonZeroEdgeLengthModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateMeshNonZeroEdgeLength")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ValidateMeshNormalsUnlockedModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateMeshNormalsUnlocked")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ValidateMeshUVSetMap1Model(BaseSettingsModel):
    """Validate model's default uv set exists and is named 'map1'."""
    enabled: bool = Field(title="ValidateMeshUVSetMap1")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ValidateMeshVerticesHaveEdgesModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateMeshVerticesHaveEdges")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ValidateNoAnimationModel(BaseSettingsModel):
    """Ensure no keyframes on nodes in the Instance."""
    enabled: bool = Field(title="ValidateNoAnimation")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ValidateNoNamespaceModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateNoNamespace")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ValidateNoNullTransformsModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateNoNullTransforms")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ValidateNoUnknownNodesModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateNoUnknownNodes")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ValidateNodeNoGhostingModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateNodeNoGhosting")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ValidateShapeDefaultNamesModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateShapeDefaultNames")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ValidateShapeRenderStatsModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateShapeRenderStats")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ValidateShapeZeroModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateShapeZero")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ValidateTransformZeroModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateTransformZero")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ValidateUniqueNamesModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateUniqueNames")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ValidateNoVRayMeshModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateNoVRayMesh")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ValidateUnrealMeshTriangulatedModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateUnrealMeshTriangulated")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ValidateAlembicVisibleOnlyModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateAlembicVisibleOnly")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ExtractAlembicModel(BaseSettingsModel):
    enabled: bool = Field(title="ExtractAlembic")
    families: list[str] = Field(default_factory=["pointcache", "model", "vrayproxy"],
        title="Families")


class ModelPublishSetting(BaseSettingsModel):
    ValidateModelName: ValidateModelNameModel = Field(
        default_factory=ValidateModelNameModel,
        title="Validate Model Name"
    )
    ValidateModelContent: ValidateModelContentModel = Field(
        default_factory=ValidateModelContentModel,
        title="Validate Model Content"
    )
    ValidateTransformNamingSuffix: ValidateTransformNamingSuffixModel = Field(
        default_factory=ValidateTransformNamingSuffixModel,
        title="Validate Transform Naming Suffix"
    )
    ValidateColorSets: ValidateColorSetsModel = Field(
        default_factory=ValidateColorSetsModel,
        title="Validate Color Sets"
    )
    ValidateMeshHasOverlappingUVs: ValidateMeshHasOverlappingUVsModel = Field(
        default_factory=ValidateMeshHasOverlappingUVsModel,
        title="Validate Mesh Has Overlapping UVs"
    )
    ValidateMeshArnoldAttributes: ValidateMeshArnoldAttributesModel = Field(
        default_factory=ValidateMeshArnoldAttributesModel,
        title="Validate Mesh Arnold Attributes"
    )
    ValidateMeshShaderConnections: ValidateMeshShaderConnectionsModel = Field(
        default_factory=ValidateMeshShaderConnectionsModel,
        title="Validate Mesh Shader Connections"
    )
    ValidateMeshSingleUVSet: ValidateMeshSingleUVSetModel = Field(
        default_factory=ValidateMeshSingleUVSetModel,
        title="Validate Mesh Single UV Set"
    )
    ValidateMeshHasUVs: ValidateMeshHasUVsModel = Field(
        default_factory=ValidateMeshHasUVsModel,
        title="Validate Mesh Has UVs"
    )
    ValidateMeshLaminaFaces: ValidateMeshLaminaFacesModel = Field(
        default_factory=ValidateMeshLaminaFacesModel,
        title="Validate Mesh Lamina Faces"
    )
    ValidateMeshNgons: ValidateMeshNgonsModel = Field(
        default_factory=ValidateMeshNgonsModel,
        title="Validate Mesh Ngons"
    )
    ValidateMeshNonManifold: ValidateMeshNonManifoldModel = Field(
        default_factory=ValidateMeshNonManifoldModel,
        title="Validate Mesh Non-Manifold"
    )
    ValidateMeshNoNegativeScale: ValidateMeshNoNegativeScaleModel = Field(
        default_factory=ValidateMeshNoNegativeScaleModel,
        title="Validate Mesh No Negative Scale"
    )
    ValidateMeshNonZeroEdgeLength: ValidateMeshNonZeroEdgeLengthModel = Field(
        default_factory=ValidateMeshNonZeroEdgeLengthModel,
        title="Validate Mesh Edge Length Non Zero"
    )
    ValidateMeshNormalsUnlocked: ValidateMeshNormalsUnlockedModel = Field(
        default_factory=ValidateMeshNormalsUnlockedModel,
        title="Validate Mesh Normals Unlocked"
    )
    ValidateMeshUVSetMap1: ValidateMeshUVSetMap1Model = Field(
        default_factory=ValidateMeshUVSetMap1Model,
        title="Validate Mesh UV Set Map 1"
    )
    ValidateMeshVerticesHaveEdges: ValidateMeshVerticesHaveEdgesModel = Field(
        default_factory=ValidateMeshVerticesHaveEdgesModel,
        title="Validate Mesh Vertices Have Edges"
    )
    ValidateNoAnimation: ValidateNoAnimationModel = Field(
        default_factory=ValidateNoAnimationModel,
        title="Validate No Animation"
    )
    ValidateNoNamespace: ValidateNoNamespaceModel = Field(
        default_factory=ValidateNoNamespaceModel,
        title="Validate No Namespace"
    )
    ValidateNoNullTransforms: ValidateNoNullTransformsModel = Field(
        default_factory=ValidateNoNullTransformsModel,
        title="Validate No Null Transforms"
    )
    ValidateNoUnknownNodes: ValidateNoUnknownNodesModel = Field(
        default_factory=ValidateNoUnknownNodesModel,
        title="Validate No Unknown Nodes"
    )
    ValidateNodeNoGhosting: ValidateNodeNoGhostingModel = Field(
        default_factory=ValidateNodeNoGhostingModel,
        title="Validate Node No Ghosting"
    )
    ValidateShapeDefaultNames: ValidateShapeDefaultNamesModel = Field(
        default_factory=ValidateShapeDefaultNamesModel,
        title="Validate Shape Default Names"
    )
    ValidateShapeRenderStats: ValidateShapeRenderStatsModel = Field(
        default_factory=ValidateShapeRenderStatsModel,
        title="Validate Shape Render Stats"
    )
    ValidateShapeZero: ValidateShapeZeroModel = Field(
        default_factory=ValidateShapeZeroModel,
        title="Validate Shape Zero"
    )
    ValidateTransformZero: ValidateTransformZeroModel = Field(
        default_factory=ValidateTransformZeroModel,
        title="Validate Transform Zero"
    )
    ValidateUniqueNames: ValidateUniqueNamesModel = Field(
        default_factory=ValidateUniqueNamesModel,
        title="Validate Unique Names"
    )
    ValidateNoVRayMesh: ValidateNoVRayMeshModel = Field(
        default_factory=ValidateNoVRayMeshModel,
        title="Validate No V-Ray Proxies (VRayMesh)"
    )
    ValidateUnrealMeshTriangulated: ValidateUnrealMeshTriangulatedModel = Field(
        default_factory=ValidateUnrealMeshTriangulatedModel,
        title="Validate if Mesh is Triangulated"
    )
    ValidateAlembicVisibleOnly: ValidateAlembicVisibleOnlyModel = Field(
        default_factory=ValidateAlembicVisibleOnlyModel,
        title="Validate Alembic Visible Node"
    )
    ExtractAlembic: ExtractAlembicModel = Field(
        default_factory=ExtractAlembicModel,
        title="Extract Alembic",
        section="Extractors"
    )


DEFAULT_MODEL_PUBLISH_SETTING = {
    "ValidateModelName": {
        "enabled": False,
        "database": True,
        "material_file": {
            "windows": "",
            "darwin": "",
            "linux": ""
        },
        "regex": "(.*)_(\\d)*_(?P<shader>.*)_(GEO)",
        "top_level_regex": ".*_GRP"
    },
    "ValidateModelContent": {
        "enabled": True,
        "optional": False,
        "validate_top_group": True
    },
    "ValidateTransformNamingSuffix": {
        "enabled": True,
        "optional": True,
        "SUFFIX_NAMING_TABLE": "{\"mesh\": [\n\"_GEO\",\n\"_GES\",\n \"_GEP\",\n\"_OSD\"\n],\n\"nurbsCurve\": [\n\"_CRV\"\n],\n\"nurbsSurface\": [\n\"_NRB\"\n],\n\"locator\": [\n\"_LOC\"\n],\n\"group\": [\n\"_GRP\"\n]}",
        "ALLOW_IF_NOT_IN_SUFFIX_TABLE": True
    },
    "ValidateColorSets": {
            "enabled": True,
            "optional": True,
            "active": True
    },
    "ValidateMeshHasOverlappingUVs": {
            "enabled": False,
            "optional": True,
            "active": True
    },
    "ValidateMeshArnoldAttributes": {
            "enabled": False,
            "optional": True,
            "active": True
    },
    "ValidateMeshShaderConnections": {
            "enabled": True,
            "optional": True,
            "active": True
    },
    "ValidateMeshSingleUVSet": {
            "enabled": False,
            "optional": True,
            "active": True
    },
    "ValidateMeshHasUVs": {
            "enabled": True,
            "optional": True,
            "active": True
    },
    "ValidateMeshLaminaFaces": {
            "enabled": False,
            "optional": True,
            "active": True
    },
    "ValidateMeshNgons": {
            "enabled": False,
            "optional": True,
            "active": True
    },
    "ValidateMeshNonManifold": {
            "enabled": False,
            "optional": True,
            "active": True
    },
    "ValidateMeshNoNegativeScale": {
            "enabled": True,
            "optional": False,
            "active": True
    },
    "ValidateMeshNonZeroEdgeLength": {
            "enabled": True,
            "optional": True,
            "active": True
    },
    "ValidateMeshNormalsUnlocked": {
            "enabled": False,
            "optional": True,
            "active": True
    },
    "ValidateMeshUVSetMap1": {
            "enabled": False,
            "optional": True,
            "active": True
    },
    "ValidateMeshVerticesHaveEdges": {
            "enabled": True,
            "optional": True,
            "active": True
    },
    "ValidateNoAnimation": {
            "enabled": False,
            "optional": True,
            "active": True
    },
    "ValidateNoNamespace": {
            "enabled": True,
            "optional": False,
            "active": True
    },
    "ValidateNoNullTransforms": {
            "enabled": True,
            "optional": False,
            "active": True
    },
    "ValidateNoUnknownNodes": {
            "enabled": True,
            "optional": False,
            "active": True
    },
    "ValidateNodeNoGhosting": {
            "enabled": False,
            "optional": False,
            "active": True
    },
    "ValidateShapeDefaultNames": {
            "enabled": False,
            "optional": True,
            "active": True
    },
    "ValidateShapeRenderStats": {
            "enabled": False,
            "optional": True,
            "active": True
    },
    "ValidateShapeZero": {
            "enabled": False,
            "optional": True,
            "active": True
    },
    "ValidateTransformZero": {
            "enabled": False,
            "optional": True,
            "active": True
    },
    "ValidateUniqueNames": {
            "enabled": False,
            "optional": True,
            "active": True
    },
    "ValidateNoVRayMesh": {
            "enabled": True,
            "optional": False,
            "active": True
    },
    "ValidateUnrealMeshTriangulated": {
            "enabled": False,
            "optional": True,
            "active": True
    },
    "ValidateAlembicVisibleOnly": {
            "enabled": True,
            "optional": False,
            "active": True
    },
    "ExtractAlembic": {
            "enabled": True,
            "families": [
                "pointcache",
                "model",
                "vrayproxy"
            ]
    },
}

