from pydantic import validator, Field

from ayon_server.settings import (
    BaseSettingsModel
)

from .imageio import (
    ImageIOSettings,
    DEFAULT_IMAGEIO_SETTINGS
)

from .create_plugins import (
    CreatorPluginsSettings,
    DEFAULT_CREATE_SETTINGS
)
from .loader_plugins import (
    LoaderPuginsModel,
    DEFAULT_FLAME_LOADER_SETTINGS
)
from .scriptsmenu import (
    ScriptsmenuSettings,
    DEFAULT_SCRIPTSMENU_SETTINGS
)
from .filters import PublishFiltersModel


class HieroSettings(BaseSettingsModel):
    """Nuke addon settings."""

    imageio: ImageIOSettings = Field(
        default_factory=ImageIOSettings,
        title="Color Management (imageio)",
    )

    create: CreatorPluginsSettings = Field(
        default_factory=CreatorPluginsSettings,
        title="Creator Plugins",
    )
    load: LoaderPuginsModel = Field(
        default_factory=LoaderPuginsModel,
        title="Loader plugins"
    )
    scriptsmenu: ScriptsmenuSettings = Field(
        default_factory=ScriptsmenuSettings,
        title="Scripts Menu Definition",
    )
    filters: list[PublishFiltersModel] = Field(
        default_factory=list
    )

DEFAULT_VALUES = {
    "imageio": DEFAULT_IMAGEIO_SETTINGS,
    "create": DEFAULT_CREATE_SETTINGS,
    "load": DEFAULT_FLAME_LOADER_SETTINGS,
    "scriptsmenu": DEFAULT_SCRIPTSMENU_SETTINGS
}
