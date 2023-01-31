from ayon_server.settings import Field, BaseSettingsModel


class ValidateCameraZeroKeyframeModel(BaseSettingsModel):
    enabled: bool = Field(
        True,
        title="Validate Camera Zero Keyframe"
    )
    optional: bool = Field(
        True,
        title="Optional"
    )
    active: bool = Field(
        True,
        title="Active"
    )


class ValidateMeshHasUvsModel(BaseSettingsModel):
    enabled: bool = Field(
        True,
        title="Validate Mesh Has Uvs"
    )
    optional: bool = Field(
        True,
        title="Optional"
    )
    active: bool = Field(
        True,
        title="Active"
    )


class ValidateMeshNoNegativeScaleModel(BaseSettingsModel):
    enabled: bool = Field(
        True,
        title="Validate Mesh No Negative Scale"
    )
    optional: bool = Field(
        False,
        title="Optional"
    )
    active: bool = Field(
        True,
        title="Active"
    )


class ValidateTransformZeroModel(BaseSettingsModel):
    enabled: bool = Field(
        True,
        title="Validate Transform Zero"
    )
    optional: bool = Field(
        False,
        title="Optional"
    )
    active: bool = Field(
        True,
        title="Active"
    )


class ExtractBlendModel(BaseSettingsModel):
    enabled: bool = Field(
        True,
        title="Extract Blend"
    )
    optional: bool = Field(
        True,
        title="Optional"
    )
    active: bool = Field(
        True,
        title="Active"
    )
    families: list[str] = Field(
        default_factory=["model", "camera", "rig", "action", "layout"],
        title="Families"
    )


class ExtractFBXModel(BaseSettingsModel):
    enabled: bool = Field(
        True,
        title="Extract FBX"
    )
    optional: bool = Field(
        True,
        title="Optional"
    )
    active: bool = Field(
        False,
        title="Active"
    )


class ExtractABCModel(BaseSettingsModel):
    enabled: bool = Field(
        True,
        title="Extract FBX"
    )
    optional: bool = Field(
        True,
        title="Optional"
    )
    active: bool = Field(
        False,
        title="Active"
    )


class ExtractBlendAnimationModel(BaseSettingsModel):
    enabled: bool = Field(
        True,
        title="Extract FBX"
    )
    optional: bool = Field(
        True,
        title="Optional"
    )
    active: bool = Field(
        True,
        title="Active"
    )


class ExtractAnimationFBXModel(BaseSettingsModel):
    enabled: bool = Field(
        True,
        title="Extract FBX"
    )
    optional: bool = Field(
        True,
        title="Optional"
    )
    active: bool = Field(
        False,
        title="Active"
    )


class ExtractCameraModel(BaseSettingsModel):
    enabled: bool = Field(
        True,
        title="Extract FBX"
    )
    optional: bool = Field(
        True,
        title="Optional"
    )
    active: bool = Field(
        True,
        title="Active"
    )


class ExtractLayoutModel(BaseSettingsModel):
    enabled: bool = Field(
        True,
        title="Extract FBX"
    )
    optional: bool = Field(
        True,
        title="Optional"
    )
    active: bool = Field(
        False,
        title="Active"
    )


class PublishPuginsModel(BaseSettingsModel):
    ValidateCameraZeroKeyframe: ValidateCameraZeroKeyframeModel = Field(
        default_factory=ValidateCameraZeroKeyframeModel,
        title="Validate Camera Zero Keyframe",
        section="Validators"
    )
    ValidateMeshHasUvs: ValidateMeshHasUvsModel = Field(
        default_factory=ValidateMeshHasUvsModel,
        title="Validate Mesh Has Uvs"
    )
    ValidateMeshNoNegativeScale: ValidateMeshNoNegativeScaleModel = Field(
        default_factory=ValidateMeshNoNegativeScaleModel,
        title="Validate Mesh No Negative Scale"
    )
    ValidateTransformZero: ValidateTransformZeroModel = Field(
        default_factory=ValidateTransformZeroModel,
        title="Validate Transform Zero"
    )
    ExtractBlend: ExtractBlendModel = Field(
        default_factory=ExtractBlendModel,
        title="Extract Blend",
        section="Extractors"
    )
    ExtractFBX: ExtractFBXModel = Field(
        default_factory=ExtractFBXModel,
        title="Extract FBX"
    )
    ExtractABC: ExtractABCModel = Field(
        default_factory=ExtractABCModel,
        title="Extract ABC"
    )
    ExtractBlendAnimation: ExtractBlendAnimationModel = Field(
        default_factory=ExtractBlendAnimationModel,
        title="Extract Blend Animation"
    )
    ExtractAnimationFBX: ExtractAnimationFBXModel = Field(
        default_factory=ExtractAnimationFBXModel,
        title="Extract Animation FBX"
    )
    ExtractCamera: ExtractCameraModel = Field(
        default_factory=ExtractCameraModel,
        title="Extract Camera"
    )
    ExtractLayout: ExtractLayoutModel = Field(
        default_factory=ExtractLayoutModel,
        title="Extract Layout"
    )


DEFAULT_BLENDER_PUBLISH_SETTINGS = {
    "ValidateCameraZeroKeyframe": {
        "enabled": True,
        "optional": True,
        "active": True
    },
    "ValidateMeshHasUvs": {
        "enabled": True,
        "optional": True,
        "active": True
    },
    "ValidateMeshNoNegativeScale": {
        "enabled": True,
        "optional": False,
        "active": True
    },
    "ValidateTransformZero": {
        "enabled": True,
        "optional": False,
        "active": True
    },
    "ExtractBlend": {
        "enabled": True,
        "optional": True,
        "active": True,
        "families": [
            "model",
            "camera",
            "rig",
            "action",
            "layout"
        ]
    },
    "ExtractFBX": {
        "enabled": True,
        "optional": True,
        "active": False
    },
    "ExtractABC": {
        "enabled": True,
        "optional": True,
        "active": False
    },
    "ExtractBlendAnimation": {
        "enabled": True,
        "optional": True,
        "active": True
    },
    "ExtractAnimationFBX": {
        "enabled": True,
        "optional": True,
        "active": False
    },
    "ExtractCamera": {
        "enabled": True,
        "optional": True,
        "active": True
    },
    "ExtractLayout": {
        "enabled": True,
        "optional": True,
        "active": False
    }
}
