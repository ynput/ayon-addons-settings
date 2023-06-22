from typing import Any, Type

from ayon_server.addons import BaseServerAddon

from .settings import MusterSettings, DEFAULT_VALUES


class MusterAddon(BaseServerAddon):
    name = "muster"
    version = "0.1.0"
    title = "Muster"
    settings_model: Type[MusterSettings] = MusterSettings

    async def get_default_settings(self):
        settings_model_cls = self.get_settings_model()
        return settings_model_cls(**DEFAULT_VALUES)