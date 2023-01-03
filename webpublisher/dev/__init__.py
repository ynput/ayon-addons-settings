from typing import Type

from ayon_server.addons import BaseServerAddon

from .settings import WebpublisherSettings, DEFAULT_VALUES


class WebpublisherAddon(BaseServerAddon):
    name = "webpublisher"
    title = "Webpublisher"
    version = "1.0.0"
    settings_model: Type[WebpublisherSettings] = WebpublisherSettings
    frontend_scopes = {}
    services = {}

    async def get_default_settings(self):
        settings_model_cls = self.get_settings_model()
        return settings_model_cls(**DEFAULT_VALUES)
