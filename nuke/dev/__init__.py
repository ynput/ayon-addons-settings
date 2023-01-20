from typing import Type

from ayon_server.addons import BaseServerAddon, AddonLibrary

from .settings import NukeSettings, DEFAULT_VALUES


class NukeAddon(BaseServerAddon):
    name = "nuke"
    title = "Foundry Nuke"
    version = "1.0.0"
    settings_model: Type[NukeSettings] = NukeSettings

    async def get_default_settings(self):
        settings_model_cls = self.get_settings_model()
        return settings_model_cls(**DEFAULT_VALUES)
