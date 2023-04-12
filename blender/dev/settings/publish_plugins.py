from ayon_server.settings import Field, BaseSettingsModel





class ValidatePluginModel(BaseSettingsModel):
    enabled: bool = Field(True)
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


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





class PublishPuginsModel(BaseSettingsModel):
    ValidateCameraZeroKeyframe: ValidatePluginModel = Field(
        default_factory=ValidatePluginModel,
        title="Validate Camera Zero Keyframe",
        section="Validators"
    )
    ValidateMeshHasUvs: ValidatePluginModel = Field(
        default_factory=ValidatePluginModel,
        title="Validate Mesh Has Uvs"
    )
    ValidateMeshNoNegativeScale: ValidatePluginModel = Field(
        default_factory=ValidatePluginModel,
        title="Validate Mesh No Negative Scale"
    )
    ValidateTransformZero: ValidatePluginModel = Field(
        default_factory=ValidatePluginModel,
        title="Validate Transform Zero"
    )
    ExtractBlend: ExtractBlendModel = Field(
        default_factory=ExtractBlendModel,
        title="Extract Blend",
        section="Extractors"
    )
    ExtractFBX: ValidatePluginModel = Field(
        default_factory=ValidatePluginModel,
        title="Extract FBX"
    )
    ExtractABC: ValidatePluginModel = Field(
        default_factory=ValidatePluginModel,
        title="Extract ABC"
    )
    ExtractBlendAnimation: ValidatePluginModel = Field(
        default_factory=ValidatePluginModel,
        title="Extract Blend Animation"
    )
    ExtractAnimationFBX: ValidatePluginModel = Field(
        default_factory=ValidatePluginModel,
        title="Extract Animation FBX"
    )
    ExtractCamera: ValidatePluginModel = Field(
        default_factory=ValidatePluginModel,
        title="Extract Camera"
    )
    ExtractLayout: ValidatePluginModel = Field(
        default_factory=ValidatePluginModel,
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
