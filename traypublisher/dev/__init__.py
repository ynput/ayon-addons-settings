from ayon_server.addons import BaseServerAddon

from .settings.main import TraypublisherSettings, DEFAULT_TRAYPUBLISHER_SETTING
from .version import __version__


class Traypublisher(BaseServerAddon):
    name = "traypublisher"
    version = __version__

    settings_model = TraypublisherSettings

    async def get_default_settings(self):
        settings_model_cls = self.get_settings_model()
        return settings_model_cls(**DEFAULT_TRAYPUBLISHER_SETTING)
