from typing import Type

from openpype.addons import BaseServerAddon

from .settings import FlameSettings, DEFAULT_VALUES


class FlameAddon(BaseServerAddon):
    name = "flame"
    title = "Flame"
    version = "1.0.0"
    settings_model: Type[FlameSettings] = FlameSettings
    frontend_scopes = {}
    services = {}

    async def get_default_settings(self):
        settings_model_cls = self.get_settings_model()
        return settings_model_cls(**DEFAULT_VALUES)