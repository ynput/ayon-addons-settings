from pydantic import Field
from ayon_server.settings import BaseSettingsModel, ImageIOBaseModel

from .simple_creators import (
    SimpleCreatorPlugin,
    DEFAULT_SIMPLE_CREATORS,
)
from .editorial_creators import (
    TraypublisherEditorialCreatorPlugins,
    DEFAULT_EDITORIAL_CREATORS,
)
from .creator_plugins import BatchMovieCreatorPlugin
from .publish_plugins import TrayPublisherPublishPlugins


class TraypublisherSettings(BaseSettingsModel):
    """Traypublisher Project Settings."""
    imageio: ImageIOBaseModel = Field(
        default_factory=ImageIOBaseModel,
        title="OCIO config"
    )
    simple_creators: list[SimpleCreatorPlugin] = Field(
        title="Creator plugins",
        default_factory=SimpleCreatorPlugin,
    )
    #
    editorial_creators: TraypublisherEditorialCreatorPlugins = Field(
        title="Editorial Creators",
        default_factory=TraypublisherEditorialCreatorPlugins,
    )

    BatchMovieCreator: BatchMovieCreatorPlugin = Field(
        title="Batch Movie Creator",
        default_factory=BatchMovieCreatorPlugin
    )

    publish: TrayPublisherPublishPlugins = Field(
        title="Publish Plugins",
        default_factory=TrayPublisherPublishPlugins
    )


DEFAULT_TRAYPUBLISHER_SETTING = {
    "simple_creators": DEFAULT_SIMPLE_CREATORS,
    "editorial_creators": DEFAULT_EDITORIAL_CREATORS,
    "BatchMovieCreator": {
        "default_variants": [
            "Main"
        ],
        "default_tasks": [
            "Compositing"
        ],
        "extensions": [
            ".mov"
        ]
    },
    "publish": {
        "ValidateFrameRange": {
            "enabled": True,
            "optional": True,
            "active": True
        }
    }
}
