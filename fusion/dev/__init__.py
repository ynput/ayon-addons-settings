from typing import Any, Type

from openpype.addons import BaseServerAddon

from .settings import FusionSettings


class FusionAddon(BaseServerAddon):
    name = "fusion"
    title = "Fusion"
    version = "1.0.0"
    settings_model: Type[FusionSettings] = FusionSettings 
    frontend_scopes = {}
    services = {}
