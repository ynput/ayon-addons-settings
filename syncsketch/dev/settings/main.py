from pydantic import Field, validator

from ayon_server.settings import BaseSettingsModel, ensure_unique_names

from .publish_plugins import (
    PublishPluginsModel,
    DEFAULT_SYNCSKETCH_PLUGINS_SETTINGS
)


class ServerListSubmodel(BaseSettingsModel):
    active: bool = Field(title="Active")
    name: str = Field(title="Name")
    url: str = Field(title="Value")
    auth_token: str = Field(title="Auth Token")


class SyncsketchSettings(BaseSettingsModel):

    syncsketch_server_configs:  list[ServerListSubmodel] = Field(
        default_factory=list,
        title="SyncSketch server configs",
    )

    publish: PublishPluginsModel = Field(
        default_factory=PublishPluginsModel,
        title="Publish Plugins",
    )

    @validator("syncsketch_server_configs")
    def validate_unique_names(cls, value):
        ensure_unique_names(value)
        return value


DEFAULT_VALUES = {
    "syncsketch_server_configs": [
        {
            "name": "default",
            "url": "http://studio.syncsketch.com",
            "active": True,
            "auth_token": ""
        }
    ],
    "publish": DEFAULT_SYNCSKETCH_PLUGINS_SETTINGS
}
