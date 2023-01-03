from openpype.settings import BaseSettingsModel, Field

class ocioPath(BaseSettingsModel):
    windows: str = Field('', title="Windows")
    darwin: str = Field('', title="MacOS")
    linux: str = Field('', title="Linux")


class ocio(BaseSettingsModel):
    ocioPathModel: ocioPath = Field(default_factory=ocioPath, title="OCIO Config File Path")
    enabled:  bool = False
 

    

class imageioModel(BaseSettingsModel):
    ocioSettings: ocio = Field(
        title="OpenColorIO (OCIO)",
        default_factory=ocio,
    )    

class FusionSettings(BaseSettingsModel):
    imageio:  imageioModel = Field(default_factory=imageioModel, title="Color Management (ImageIO)")
