from ayon_server.settings import BaseSettingsModel, Field


class OcioPathModel(BaseSettingsModel):
    windows: str = Field('', title="Windows")
    darwin: str = Field('', title="MacOS")
    linux: str = Field('', title="Linux")


class OcioModel(BaseSettingsModel):
    enabled: bool = False
    configFilePath: OcioPathModel = Field(
        default_factory=OcioPathModel,
        title="OCIO Config File Path"
    )


class imageioModel(BaseSettingsModel):
    ocio: OcioModel = Field(
        default_factory=OcioModel,
        title="OpenColorIO (OCIO)",
    )


class FusionSettings(BaseSettingsModel):
    imageio: imageioModel = Field(
        default_factory=imageioModel,
        title="Color Management (ImageIO)"
    )
