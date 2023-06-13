from pydantic import Field
from ayon_server.settings import BaseSettingsModel, HostImageIOBaseModel

from .simple_creators import (
    SimpleCreatorPlugin,
    DEFAULT_SIMPLE_CREATORS,
)
from .editorial_creators import (
    TraypublisherEditorialCreatorPlugins,
    DEFAULT_EDITORIAL_CREATORS,
)
from .creator_plugins import (
    TrayPublisherCreatePluginsModel,
    DEFAULT_CREATORS
)
from .publish_plugins import TrayPublisherPublishPlugins


class TraypublisherSettings(BaseSettingsModel):
    """Traypublisher Project Settings."""
    imageio: HostImageIOBaseModel = Field(
        default_factory=HostImageIOBaseModel,
        title="Color Management (ImageIO)"
    )
    simple_creators: list[SimpleCreatorPlugin] = Field(
        title="Simple Create Plugins",
        default_factory=SimpleCreatorPlugin,
    )
    editorial_creators: TraypublisherEditorialCreatorPlugins = Field(
        title="Editorial Creators",
        default_factory=TraypublisherEditorialCreatorPlugins,
    )
    create: TrayPublisherCreatePluginsModel = Field(
        title="Create",
        default_factory=TrayPublisherCreatePluginsModel
    )
    publish: TrayPublisherPublishPlugins = Field(
        title="Publish Plugins",
        default_factory=TrayPublisherPublishPlugins
    )


DEFAULT_TRAYPUBLISHER_SETTING = {
    "simple_creators": DEFAULT_SIMPLE_CREATORS,
    "editorial_creators": DEFAULT_EDITORIAL_CREATORS,
    "create": DEFAULT_CREATORS,
    "publish": {
        "ValidateFrameRange": {
            "enabled": True,
            "optional": True,
            "active": True
        }
    }
}
