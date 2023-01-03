from typing import Any, Type

from ayon_server.addons import BaseServerAddon

from .settings import RoyalRenderSettings


class RoyalRenderAddon(BaseServerAddon):
    name = "royalrender"
    version = "1.0.0"
    title = "Royal Render"
    settings_model: Type[RoyalRenderSettings] = RoyalRenderSettings