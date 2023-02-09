from pydantic import Field
from ayon_server.settings import (
    BaseSettingsModel,
    ImageIOConfigModel,
    ImageIOFileRulesModel,
    MultiplatformPathModel,
)


class OcioModel(BaseSettingsModel):
    enabled: bool = False
    configFilePath: MultiplatformPathModel = Field(
        default_factory=MultiplatformPathModel,
        title="OCIO Config File Path"
    )


class imageioModel(BaseSettingsModel):
    ocio_config: ImageIOConfigModel = Field(
        default_factory=ImageIOConfigModel,
        title="OCIO config"
    )
    file_rules: ImageIOFileRulesModel = Field(
        default_factory=ImageIOFileRulesModel,
        title="File Rules"
    )
    ocio: OcioModel = Field(
        default_factory=OcioModel,
        title="OpenColorIO (OCIO)",
    )


class FusionSettings(BaseSettingsModel):
    imageio: imageioModel = Field(
        default_factory=imageioModel,
        title="Color Management (ImageIO)"
    )
