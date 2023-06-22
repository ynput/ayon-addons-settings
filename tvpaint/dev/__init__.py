from typing import Any, Type

from ayon_server.addons import BaseServerAddon

from .settings import TvpaintSettings, DEFAULT_VALUES


class TvpaintAddon(BaseServerAddon):
    name = "tvpaint"
    title = "TVPaint"
    version = "0.1.0"
    settings_model: Type[TvpaintSettings] = TvpaintSettings
    

    async def get_default_settings(self):
        settings_model_cls = self.get_settings_model()
        return settings_model_cls(**DEFAULT_VALUES)