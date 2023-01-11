from pydantic import Field, validator

from ayon_server.settings import BaseSettingsModel, ensure_unique_names
from ayon_server.types import ColorRGBA_uint8


class CollectRenderSceneModel(BaseSettingsModel):
    """It is possible to fill 'render_layer' or 'variant' in subset name template with custom value.
    - value of 'render_pass' is always "beauty"."""
    enabled: bool = False
    render_layer: str = Field("Main", title="Render Layer")


class ExtractSequenceModel(BaseSettingsModel):
    """Review BG color is used for whole scene review and for thumbnails."""
    # TODO Use alpha color
    review_bg: ColorRGBA_uint8 = Field((255, 255, 255, 1.0), title="Review BG color")
    families_to_review: list[str] = Field(default_factory=list, title="Families to review")


class ValidatePluginModel(BaseSettingsModel):
    enabled: bool = True
    optional: bool = Field(True, title="Optional")
    active: bool = Field(True, title="Active")


class ExtractConvertToEXRModel(BaseSettingsModel):
    """WARNING: This plugin does not work on MacOS (using OIIO tool)."""
    enabled: bool = False
    replace_pngs: bool = True
    def compression_enum():
        [
            {
                "value": "ZIP", "label": "ZIP"
            },
            {
                "value": "ZIPS", "label": "ZIPS"
            },
            {
                "value": "DWAA", "label": "DWAA"
            },
            {
                "value": "DWAB", "label": "DWAB"
            },
            {
                "value": "PIZ", "label": "PIZ"
            },
            {   "value": "RLE", "label": "RLE"
            },
            {
                "value": "PXR24", "label": "PXR24"
            },
            {
                "value": "B44", "label": "B44"
            },
            {
                "value": "B44A", "label": "B44A"
            },
            {
                "value": "none", "label": "None"
            }
        ]

    exr_compression: str = Field(
        "",
        enum_resolver=compression_enum,
        title="EXR Compression"
    )


class LoadImageDefaultModel(BaseSettingsModel):
    _layout = "expanded"
    stretch: bool = Field(title="Stretch")
    timestretch: bool = Field(title="TimeStretch")
    preload: bool = Field(title="Preload")


class LoadImageModel(BaseSettingsModel):
    defaults: LoadImageDefaultModel = Field(
        default_factory=LoadImageDefaultModel
    )


class PublishPluginsModel(BaseSettingsModel):
    CollectRenderScene: CollectRenderSceneModel = Field(default_factory=CollectRenderSceneModel, title="Collect Render Scene")
    ExtractSequence: ExtractSequenceModel = Field(default_factory=ExtractSequenceModel, title="Extract Sequence")
    ValidateProjectSettings: ValidatePluginModel = Field(default_factory=ValidatePluginModel, title="Validate Project Settings")
    ValidateMarks: ValidatePluginModel = Field(default_factory=ValidatePluginModel, title="Validate MarkIn/Out")
    ValidateStartFrame: ValidatePluginModel = Field(default_factory=ValidatePluginModel, title="Validate Scene Start Frame")
    ValidateAssetName: ValidatePluginModel = Field(default_factory=ValidatePluginModel, title="Validate Asset Name")
    ExtractConvertToEXR: ExtractConvertToEXRModel = Field(default_factory=ExtractConvertToEXRModel, title="Extract Convert To EXR")


class LoadPluginsModel(BaseSettingsModel):
    LoadImage: LoadImageModel = Field(default_factory=LoadImageModel, title="Load Image")
    ImportImage: LoadImageModel = Field(default_factory=LoadImageModel, title="Import Image")
