from typing import Any, Type

from openpype.addons import BaseServerAddon

from .settings import HoudiniSettings, DEFAULT_VALUES


class Houdini(BaseServerAddon):
    name = "houdini"
    title = "Houdini"
    version = "1.0.0"
    settings_model: Type[HoudiniSettings] = HoudiniSettings

    async def get_default_settings(self):
        settings_model_cls = self.get_settings_model()
        return settings_model_cls(**DEFAULT_VALUES)