from typing import Any, Type

from ayon_server.addons import BaseServerAddon

from .settings import KitsuSettings, DEFAULT_VALUES


class KitsuAddon(BaseServerAddon):
    name = "kitsu"
    title = "Kitsu"
    version = "0.1.0"
    settings_model: Type[KitsuSettings] = KitsuSettings
    frontend_scopes = {}
    services = {}
    
    async def get_default_settings(self):
        settings_model_cls = self.get_settings_model()
        return settings_model_cls(**DEFAULT_VALUES)
