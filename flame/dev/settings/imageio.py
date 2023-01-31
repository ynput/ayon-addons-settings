from pydantic import Field
from ayon_server.settings import (
    BaseSettingsModel,
    ImageIOConfigModel,
    ImageIOFileRulesModel,
)


class ProfileNamesMappingInputsModel(BaseSettingsModel):
    _layout = "expanded"

    flameName: str = Field("", title="Flame name")
    ocioName: str = Field("", title="OCIO name")


class ProfileNamesMappingModel(BaseSettingsModel):
    _layout = "expanded"

    inputs: list[ProfileNamesMappingInputsModel] = Field(
        default_factory=list,
        title="Profile names mapping"
    )


class ImageIOProjectModel(BaseSettingsModel):
    colourPolicy: str = Field(
        "ACES 1.1",
        title="Colour Policy (name or path)",
        section="Project"
    )
    frameDepth: str = Field(
        "16-bit fp",
        title="Image Depth"
    )
    fieldDominance: str = Field(
        "PROGRESSIVE",
        title="Field Dominance"
    )


class ImageIOModel(BaseSettingsModel):
    _isGroup = True

    ocio_config: ImageIOConfigModel = Field(
        default_factory=ImageIOConfigModel,
        title="OCIO config"
    )
    file_rules: ImageIOFileRulesModel = Field(
        default_factory=ImageIOFileRulesModel,
        title="File Rules"
    )
    # NOTE 'project' attribute was expanded to this model but that caused
    #   inconsistency with v3 settings and harder conversion handling
    #   - it can be moved back but keep in mind that it must be handled in v3
    #       conversion script too
    project: ImageIOProjectModel = Field(
        default_factory=ImageIOProjectModel,
        title="Project"
    )
    profilesMapping: ProfileNamesMappingModel = Field(
        default_factory=ProfileNamesMappingModel,
        title="Profile names mapping"
    )


DEFAULT_IMAGEIO_SETTINGS = {
    "project": {
        "colourPolicy": "ACES 1.1",
        "frameDepth": "16-bit fp",
        "fieldDominance": "PROGRESSIVE"
    },
    "profilesMapping": {
        "inputs": [
            {
                "flameName": "ACEScg",
                "ocioName": "ACES - ACEScg"
            },
            {
                "flameName": "Rec.709 video",
                "ocioName": "Output - Rec.709"
            }
        ]
    }
}
