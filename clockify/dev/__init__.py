from typing import Type

from ayon_server.addons import BaseServerAddon

from .settings import ClockifySettings


class ClockifyAddon(BaseServerAddon):
    name = "clockify"
    title = "Clockify"
    version = "1.0.0"
    settings_model: Type[ClockifySettings] = ClockifySettings
    frontend_scopes = {}
    services = {}
