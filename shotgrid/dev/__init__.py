from typing import Any, Type

from openpype.addons import BaseServerAddon

from .settings import ShotgridSettings, DEFAULT_VALUES


class ShotgridAddon(BaseServerAddon):
    name = "shotgrid"
    title = "Shotgrid"
    version = "1.0.0"
    settings_model: Type[ShotgridSettings] = ShotgridSettings
    frontend_scopes = {}
    services = {}

    async def get_default_settings(self):
        settings_model_cls = self.get_settings_model()
        return settings_model_cls(**DEFAULT_VALUES)
