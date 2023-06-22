from typing import Any, Type

from ayon_server.addons import BaseServerAddon

from .settings import TimersManagerSettings


class TimersManagerAddon(BaseServerAddon):
    name = "timers_manager"
    version = "0.1.0"
    title = "Timers Manager"
    settings_model: Type[TimersManagerSettings] = TimersManagerSettings
