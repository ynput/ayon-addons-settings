from pydantic import Field

from ayon_server.settings import BaseSettingsModel


class CollectActiveServerConfigModel(BaseSettingsModel):
    """Settings for active SyncSketch server."""

    single: bool = Field(title="Single SyncSketch server")


class PublishPluginsModel(BaseSettingsModel):
    CollectActiveServerConfig: CollectActiveServerConfigModel = \
        Field(
            default_factory=CollectActiveServerConfigModel,
            title="Collect active SyncSketch server"
        )


DEFAULT_SYNCSKETCH_PLUGINS_SETTINGS = {
    "CollectActiveServerConfig":  {
        "single": True
    }
}
