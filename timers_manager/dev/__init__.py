from typing import Any, Type

from openpype.addons import BaseServerAddon

from .settings import TimersManagerSettings


class TimersManagerAddon(BaseServerAddon):
    name = "timers_manager"
    version = "1.0.0"
    title = "Timers Manager"
    settings_model: Type[TimersManagerSettings] = TimersManagerSettings