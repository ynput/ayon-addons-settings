from pydantic import Field

from ayon_server.settings import BaseSettingsModel
from ayon_server.types import ColorRGBA_uint8



class ColorsSetting(BaseSettingsModel):
    model: ColorRGBA_uint8 = Field((209, 132, 30, 255), title="Model:")
    rig: ColorRGBA_uint8 = Field((59, 226, 235, 255), title="Rig:")
    pointcache: ColorRGBA_uint8 = Field((94, 209, 30, 255),
        title="Pointcache:")
    animation: ColorRGBA_uint8 = Field((94, 209, 30, 255),
        title="Animation:")
    ass: ColorRGBA_uint8 = Field((249, 135, 53, 255),
        title="Arnold StandIn:")
    camera: ColorRGBA_uint8 = Field((136, 114, 244, 255), title="Camera:")
    fbx: ColorRGBA_uint8 = Field((215, 166, 255, 255), title="FBX:")
    mayaAscii: ColorRGBA_uint8 = Field((67, 174, 255, 255), title="Maya Ascii:")
    mayaScene: ColorRGBA_uint8 = Field((67, 174, 255, 255), title="Maya Scene:")
    setdress: ColorRGBA_uint8 = Field((255, 250, 90, 255), title="Set Dress:")
    layout: ColorRGBA_uint8 = Field((255, 250, 90, 255), title="Layout:")
    vdbcache: ColorRGBA_uint8 = Field((249, 54, 0, 255), title="VDB Cache:")
    vrayproxy: ColorRGBA_uint8 = Field((255, 150, 12, 255), title="VRay Proxy:")
    vrayscene_layer: ColorRGBA_uint8 = Field((255, 150, 12, 255), title="VRay Scene:")
    yeticache: ColorRGBA_uint8 = Field((99, 206, 220, 255), title="Yeti Cache:")
    yetiRig: ColorRGBA_uint8 = Field((0, 205, 125, 255), title="Yeti Rig:")


class LoadersModel(BaseSettingsModel):
    colors: ColorsSetting = Field(default_factory=ColorsSetting,
    title="Loaded Subsets Outliner Colors")


DEFAULT_LOADERS_SETTING = {
        "colors": {
            "model": [
                209,
                132,
                30,
                255
            ],
            "rig": [
                59,
                226,
                235,
                255
            ],
            "pointcache": [
                94,
                209,
                30,
                255
            ],
            "animation": [
                94,
                209,
                30,
                255
            ],
            "ass": [
                249,
                135,
                53,
                255
            ],
            "camera": [
                136,
                114,
                244,
                255
            ],
            "fbx": [
                215,
                166,
                255,
                255
            ],
            "mayaAscii": [
                67,
                174,
                255,
                255
            ],
            "mayaScene": [
                67,
                174,
                255,
                255
            ],
            "setdress": [
                255,
                250,
                90,
                255
            ],
            "layout": [
                255,
                250,
                90,
                255
            ],
            "vdbcache": [
                249,
                54,
                0,
                255
            ],
            "vrayproxy": [
                255,
                150,
                12,
                255
            ],
            "vrayscene_layer": [
                255,
                150,
                12,
                255
            ],
            "yeticache": [
                99,
                206,
                220,
                255
            ],
            "yetiRig": [
                0,
                205,
                125,
                255
            ]
        }
}

