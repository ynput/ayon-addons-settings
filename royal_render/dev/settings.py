from pydantic import Field
from ayon_server.settings import BaseSettingsModel


class MultiplatformStrList(BaseSettingsModel):
    """Todo: This should be unified across the addons."""

    windows: list[str] = Field(default_factory=list, title="Windows")
    linux: list[str] = Field(default_factory=list, title="Linux")
    darwin: list[str] = Field(default_factory=list, title="MacOS")


class ServerListSubmodel(BaseSettingsModel):
    _layout = "compact"
    name: str = Field(["default"], title="Name")
    value: MultiplatformStrList = Field(
        default_factory=MultiplatformStrList
    )


class RoyalRenderSettings(BaseSettingsModel):
    enabled: bool = True

    rr_paths:  list[ServerListSubmodel] = Field(
        default_factory=list,
        title="Royal Render Root Paths",
    )


DEFAULT_VALUES = {
    "enabled": False,
    "rr_paths": [{
        "name": "default",
        "value": {
            "windows": "",
            "darwin": "",
            "linux": ""
        }
        }
    ]
}
