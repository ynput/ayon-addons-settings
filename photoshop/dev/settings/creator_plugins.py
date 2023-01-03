from pydantic import Field

from openpype.settings import BaseSettingsModel


class CreateImagePlugin(BaseSettingsModel):
    defaults: list[str] = Field(default_factory=list,
                                title="Default Subsets")


class PhotoshopCreatorPlugins(BaseSettingsModel):
    CreateImage: CreateImagePlugin = Field(
        title="Create Image",
        default_factory=CreateImagePlugin,
    )
