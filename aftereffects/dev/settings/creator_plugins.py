from pydantic import Field

from ayon_server.settings import BaseSettingsModel


class CreateRenderPlugin(BaseSettingsModel):
    defaults: list[str] = Field(default_factory=list,
                                title="Default Variants")


class AfterEffectsCreatorPlugins(BaseSettingsModel):
    RenderCreator: CreateRenderPlugin = Field(
        title="Create Render",
        default_factory=CreateRenderPlugin,
    )
