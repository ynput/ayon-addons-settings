from pydantic import Field

from openpype.settings import BaseSettingsModel


class ImageSequenceLoaderPlugin(BaseSettingsModel):
    family: list[str] = Field(default_factory=list,
                              title="Families")

    representations: list[str] = Field(default_factory=list,
                                       title="Representations")


class HarmonyLoaderPlugins(BaseSettingsModel):
    ImageSequenceLoader: ImageSequenceLoaderPlugin = Field(
        title="Load Image Sequence",
        default_factory=ImageSequenceLoaderPlugin,
    )
