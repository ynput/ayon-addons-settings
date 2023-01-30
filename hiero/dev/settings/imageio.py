from pydantic import Field
from ayon_server.settings import BaseSettingsModel, MultiplatformPathListModel


ocio_configs_switcher_enum = [
    {"value": "nuke-default", "label": "nuke-default"},
    {"value": "spi-vfx", "label": "spi-vfx"},
    {"value": "spi-anim", "label": "spi-anim"},
    {"value": "aces_0.1.1", "label": "aces_0.1.1"},
    {"value": "aces_0.7.1" , "label": "aces_0.7.1"},
    {"value": "aces_1.0.1", "label": "aces_1.0.1"},
    {"value": "aces_1.0.3", "label": "aces_1.0.3"},
    {"value": "aces_1.1", "label": "aces_1.1"},
    {"value": "aces_1.2", "label": "aces_1.2"},
    {"value": "aces_1.3", "label": "aces_1.3"},
    {"value": "custom", "label": "custom"}
]


class WorkfileColorspaceSettings(BaseSettingsModel):
    """Hiero workfile colorspace preset. """
    """# TODO: enhance settings with host api:
    we need to add mapping to resolve properly keys.
    Hiero is excpecting camel case key names,
    but for better code consistency we are using snake_case:

    ocio_config = ocioConfigName
    ocio_config_path = ocioconfigpath
    working_space_name = workingSpace
    int_16_name = sixteenBitLut
    int_8_name = eightBitLut
    float_name = floatLut
    log_name = logLut
    viewer_name = viewerLut
    thumbnail_name = thumbnailLut
    """

    ocioConfigName: str = Field(
        title="OpenColorIO Config",
        description="Switch between OCIO configs",
        enum_resolver=lambda: ocio_configs_switcher_enum,
        conditionalEnum=True
    )

    ocioconfigpath: MultiplatformPathListModel = Field(
        default_factory=MultiplatformPathListModel,
        title="Custom OCIO config path"
    )

    workingSpace: str = Field(
        title="Working Space"
    )
    viewerLut: str = Field(
        title="Viewer"
    )
    eightBitLut: str = Field(
        title="8-bit files"
    )
    sixteenBitLut: str = Field(
        title="16-bit files"
    )
    logLut: str = Field(
        title="Log files"
    )
    floatLut: str = Field(
        title="Float files"
    )
    thumbnailLut: str = Field(
        title="Thumnails"
    )


class ClipColorspaceRulesItems(BaseSettingsModel):
    _layout = "expanded"

    regex: str = Field("", title="Regex expression")
    colorspace: str = Field("", title="Colorspace")


class RegexInputsModel(BaseSettingsModel):
    inputs: list[ClipColorspaceRulesItems] = Field(
        default_factory=list,
        title="Inputs"
    )


class ImageIOSettings(BaseSettingsModel):
    """Hiero color management project settings. """
    _isGroup: bool = True

    workfile: WorkfileColorspaceSettings = Field(
        default_factory=WorkfileColorspaceSettings,
        title="Workfile"
    )
    """# TODO: enhance settings with host api:
    - old settings are using `regexInputs` key but we
      need to rename to `regex_inputs`
    - no need for `inputs` middle part. It can stay
      directly on `regex_inputs`
    """
    regexInputs:  RegexInputsModel = Field(
        default_factory=RegexInputsModel,
        title="Assign colorspace to clips via rules"
    )


DEFAULT_IMAGEIO_SETTINGS = {
    "workfile": {
        "ocioConfigName": "nuke-default",
        "ocioconfigpath": {
            "windows": [],
            "darwin": [],
            "linux": []
        },
        "workingSpace": "linear",
        "viewerLut": "sRGB",
        "eightBitLut": "sRGB",
        "sixteenBitLut": "sRGB",
        "logLut": "Cineon",
        "floatLut": "linear",
        "thumbnailLut": "sRGB"
    },
    "regexInputs": {
        "inputs": [
            {
                "regex": "[^-a-zA-Z0-9](plateRef).*(?=mp4)",
                "colorspace": "sRGB"
            }
        ]
    }
}
