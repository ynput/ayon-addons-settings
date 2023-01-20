from pydantic import validator, Field

from ayon_server.settings import (
    BaseSettingsModel,
    ensure_unique_names
)

from .imageio import (
    ImageIOSettings,
    DEFAULT_IMAGEIO_SETTINGS
)

from .create_plugins import (
    CreatorPluginsSettings,
    DEFAULT_CREATE_SETTINGS
)

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


DEFAULT_VALUES = {
    "imageio": DEFAULT_IMAGEIO_SETTINGS,
    "create": DEFAULT_CREATE_SETTINGS
}
