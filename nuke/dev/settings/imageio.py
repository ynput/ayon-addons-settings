from typing import Literal
from pydantic import validator
from ayon_server.settings import BaseSettingsModel, Field

from .common import PathsTemplate, KnobModel


class NodesModel(BaseSettingsModel):
    """TODO: This needs to be somehow labeled in settings panel
    or at least it could show gist of configuration
    """
    plugins: list[str] = Field(
        title="Used in plugins"
    )
    nuke_node_class: str = Field(
        title="Nuke Node Class",
    )

    """TODO:
    Need complete rework of knob types in nuke integration.
    We could not support v3 style of settings.
    """
    # TODO: this is not setting by default dict, why?
    knobs: list[KnobModel] = Field(
        title="Knobs",
    )

    @validator("knobs")
    def ensure_unique_names(cls, value):
        """Ensure name fields within the lists have unique names."""
        ensure_unique_names(value)
        return value


class NodesSetting(BaseSettingsModel):
    required_nodes: list[NodesModel] = Field(
        title="Plugin required",
        default_factory=list
    )
    override_nodes: list[NodesModel] = Field(
        title="Plugin's node overrides",
        default_factory=list
    )

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
    {"value": "custom", "label": "custom"}
]

class WorkfileColorspaceSettings(BaseSettingsModel):
    """Nuke workfile colorspace preset. """
    """TODO:
    we need to add mapping to resolve properly keys.
    Nuke is excpecting camel case key names,
    but for better code consistency we are using snake_case:

    color_management = colorManagement
    ocio_config = OCIO_config
    custom = customOCIOConfigPath
    working_space_name = workingSpaceLUT
    monitor_name = monitorLut
    monitor_out_name = monitorOutLut
    int_8_name = int8Lut
    int_16_name = int16Lut
    log_name = logLut
    float_name = floatLut
    """

    color_management: Literal["Nuke", "OCIO"] = Field(
        title="Color Management"
    )

    """TODO:
    we need to do mapping to convert underscore in aces versions
    to dot version > aces_1_0_2 = aces_1.0.2
    """
    ocio_config: str = Field(
        title="OpenColorIO Config",
        description="Switch between OCIO configs",
        enum_resolver=lambda: ocio_configs_switcher_enum,
        conditionalEnum=True
    )

    """TODO:
    In v3 nuke is excpecting key `customOCIOConfigPath`
    but here it is `config`
    """
    custom: PathsTemplate = Field(
        default_factory=PathsTemplate,
        title="Custom OCIO config path"
    )

    working_space_name: str = Field(
        title="Working Space"
    )
    monitor_name: str = Field(
        title="Monitor"
    )
    monitor_out_name: str = Field(
        title="Monitor Output"
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

class ImageIOSettings(BaseSettingsModel):
    """Nuke color management project settings. """
    _isGroup: bool = True

    enabled: bool

    """ TODO:
    need to be remapped in nuke code to accept new position

    originally: nuke/imageio/viewer/viewerProcess
    new: nuke/imageio/viewer
    """
    viewer: str = Field(
        title="Viewer Process Name",
        description="""Viewer profile is used during
        Creation of new viewer node at knob viewerProcess"""
    )

    """ TODO:
    need to be remapped in nuke code to accept new position

    originally: nuke/imageio/baking/viewerProcess
    new: nuke/imageio/baking
    """
    baking: str = Field(
        title="Baking Process Name",
        description="""Baking profile is used during
        ExctractReviewDataMov baking"""
    )

    workfile: WorkfileColorspaceSettings = Field(
        default_factory=WorkfileColorspaceSettings,
        title="Workfile"
    )

    nodes: NodesSetting = Field(
        default_factory=NodesSetting,
        title="Nodes"
    )

DEFAULT_IMAGEIO_SETTINGS = {
    "enabled": True,
    "viewer": "sRGB",
    "baking": "rec709",
    "workfile": {
        "color_management": "Nuke",
        "ocio_config": "nuke-default",
        "custom": {
            "windows": "",
            "darwin": "",
            "linux": ""
        },
        "working_space_name": "linear",
        "monitor_name": "sRGB",
        "monitor_out_name": "rec709",
        "int_8_name": "sRGB",
        "int_16_name": "sRGB",
        "log_name": "Cineon",
        "float_name": "linear"
    },
    "nodes": {
        "required_nodes": [
            {
                "plugins": [
                    "CreateWriteRender"
                ],
                "nuke_node_class": "Write",
                "knobs": [
                    {
                        "type": "text",
                        "name": "file_type",
                        "text": "exr"
                    },
                    {
                        "type": "text",
                        "name": "datatype",
                        "text": "16 bit half"
                    },
                    {
                        "type": "text",
                        "name": "compression",
                        "text": "Zip (1 scanline)"
                    },
                    {
                        "type": "boolean",
                        "name": "autocrop",
                        "boolean": True
                    },
                    {
                        "type": "color_gui",
                        "name": "tile_color",
                        "color_gui": [
                            186,
                            35,
                            35
                        ]
                    },
                    {
                        "type": "text",
                        "name": "channels",
                        "text": "rgb"
                    },
                    {
                        "type": "text",
                        "name": "colorspace",
                        "text": "linear"
                    },
                    {
                        "type": "boolean",
                        "name": "create_directories",
                        "boolean": True
                    }
                ]
            },
            {
                "plugins": [
                    "CreateWritePrerender"
                ],
                "nuke_node_class": "Write",
                "knobs": [
                    {
                        "type": "text",
                        "name": "file_type",
                        "text": "exr"
                    },
                    {
                        "type": "text",
                        "name": "datatype",
                        "text": "16 bit half"
                    },
                    {
                        "type": "text",
                        "name": "compression",
                        "text": "Zip (1 scanline)"
                    },
                    {
                        "type": "boolean",
                        "name": "autocrop",
                        "boolean": True
                    },
                    {
                        "type": "color_gui",
                        "name": "tile_color",
                        "color_gui": [
                            171,
                            171,
                            10
                        ]
                    },
                    {
                        "type": "text",
                        "name": "channels",
                        "text": "rgb"
                    },
                    {
                        "type": "text",
                        "name": "colorspace",
                        "text": "linear"
                    },
                    {
                        "type": "boolean",
                        "name": "create_directories",
                        "boolean": True
                    }
                ]
            },
            {
                "plugins": [
                    "CreateWriteStill"
                ],
                "nuke_node_class": "Write",
                "knobs": [
                    {
                        "type": "text",
                        "name": "file_type",
                        "text": "tiff"
                    },
                    {
                        "type": "text",
                        "name": "datatype",
                        "text": "16 bit"
                    },
                    {
                        "type": "text",
                        "name": "compression",
                        "text": "Deflate"
                    },
                    {
                        "type": "color_gui",
                        "name": "tile_color",
                        "color_gui": [
                            56,
                            162,
                            7
                        ]
                    },
                    {
                        "type": "text",
                        "name": "channels",
                        "text": "rgb"
                    },
                    {
                        "type": "text",
                        "name": "colorspace",
                        "text": "sRGB"
                    },
                    {
                        "type": "boolean",
                        "name": "create_directories",
                        "boolean": True
                    }
                ]
            }
        ],
        "override_nodes": []
    },
    "regexInputs": {
        "inputs": [
            {
                "regex": "(beauty).*(?=.exr)",
                "colorspace": "linear"
            }
        ]
    }
}
