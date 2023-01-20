from typing import Literal
from pydantic import Field
from ayon_server.settings import (
    BaseSettingsModel
)

from .common import PathsTemplate


ocio_configs_switcher_enum = [
    {"value": "nuke-default", "label": "nuke-default"},
    {"value": "spi-vfx", "label": "spi-vfx"},
    {"value": "spi-anim", "label": "spi-anim"},
    {"value": "aces_0_1_1", "label": "aces_0.1.1"},
    {"value": "aces_0_7_1" , "label": "aces_0.7.1"},
    {"value": "aces_1_0_1", "label": "aces_1.0.1"},
    {"value": "aces_1_0_3", "label": "aces_1.0.3"},
    {"value": "aces_1_1", "label": "aces_1.1"},
    {"value": "aces_1_2", "label": "aces_1.2"},
     {"value": "aces_1_3", "label": "aces_1.3"},
    {"value": "custom", "label": "custom"}
]

class WorkfileColorspaceSettings(BaseSettingsModel):
    """Hiero workfile colorspace preset. """
    """# TODO: Changes in host api:
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

    color_management: Literal["Nuke", "OCIO"] = Field(
        title="Color Management"
    )

    """# TODO: Changes in host api:
    we need to do mapping to convert underscore in aces versions
    to dot version > aces_1_0_2 = aces_1.0.2
    """
    ocio_config: str = Field(
        title="OpenColorIO Config",
        description="Switch between OCIO configs",
        enum_resolver=lambda: ocio_configs_switcher_enum,
        conditionalEnum=True
    )

    """# TODO: Changes in host api:
    In v3 hiero is excpecting key `customOCIOConfigPath`
    but here it is `config`
    """
    ocio_config_path: PathsTemplate = Field(
        default_factory=PathsTemplate,
        title="Custom OCIO config path"
    )

    working_space_name: str = Field(
        title="Working Space"
    )
    viewer_name: str = Field(
        title="Viewer"
    )
    int_8_name: str = Field(
        title="8-bit files"
    )
    int_16_name: str = Field(
        title="16-bit files"
    )
    log_name: str = Field(
        title="Log files"
    )
    float_name: str = Field(
        title="Float files"
    )
    thumbnail_name: str = Field(
        title="Thumnails"
    )


class ClipColorspaceRulesItems(BaseSettingsModel):
    _layout = "expanded"

    regex: str = Field("", title="Regex expression")
    colorspace: str = Field("", title="Colorspace")


class ImageIOSettings(BaseSettingsModel):
    """Hiero color management project settings. """
    _isGroup: bool = True

    workfile: WorkfileColorspaceSettings = Field(
        default_factory=WorkfileColorspaceSettings,
        title="Workfile"
    )
    """# TODO: Changes in host api:
    - old settings are using `regexInputs` key
    - removed `inputs` middle part not it is
      directly on regex_inputs
    """
    regex_inputs: list[ClipColorspaceRulesItems] = Field(
        default_factory=list,
        title="Assign colorspace to clips via rules"
    )


DEFAULT_IMAGEIO_SETTINGS = {
    "workfile": {
        "color_management": "Nuke",
        "ocio_config": "nuke-default",
        "ocio_config_path": {
            "windows": "",
            "darwin": "",
            "linux": ""
        },
        "working_space_name": "linear",
        "viewer_name": "sRGB",
        "int_8_name": "sRGB",
        "int_16_name": "sRGB",
        "log_name": "Cineon",
        "float_name": "linear",
        "thumbnail_name": "sRGB"
    },
    "regex_inputs": [
        {
            "regex": "(beauty).*(?=.exr)",
            "colorspace": "linear"
        }
    ]
}
