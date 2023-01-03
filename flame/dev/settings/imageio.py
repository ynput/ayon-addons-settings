from ayon_server.settings import Field, BaseSettingsModel


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


class ImageIOModel(BaseSettingsModel):
    _isGroup = True

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

    profilesMapping: ProfileNamesMappingModel = Field(
        default_factory=ProfileNamesMappingModel,
        title="Profile names mapping"
    )


DEFAULT_FLAME_IMAGEIO_SETTINGS = {
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
