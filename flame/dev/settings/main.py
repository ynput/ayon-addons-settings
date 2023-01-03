from openpype.settings import Field, BaseSettingsModel, TemplateWorkfileOptions

from .imageio import ImageIOModel, DEFAULT_FLAME_IMAGEIO_SETTINGS
from .create_plugins import CreatePuginsModel, DEFAULT_FLAME_CREATE_SETTINGS
from .publish_plugins import PublishPuginsModel, DEFAULT_FLAME_PUBLISH_SETTINGS
from .loader_plugins import LoaderPuginsModel, DEFAULT_FLAME_LOADER_SETTINGS


class FlameSettings(BaseSettingsModel):
    imageio: ImageIOModel = Field(
        default_factory=ImageIOModel,
        title="Color Management (ImageIO)"
    )
    create: CreatePuginsModel = Field(
        default_factory=CreatePuginsModel,
        title="Create plugins"
    )
    publish: PublishPuginsModel = Field(
        default_factory=PublishPuginsModel,
        title="Publish plugins"
    )
    load: LoaderPuginsModel = Field(
        default_factory=LoaderPuginsModel,
        title="Loader plugins"
    )

DEFAULT_VALUES = {
    "imageio": DEFAULT_FLAME_IMAGEIO_SETTINGS,
    "create": DEFAULT_FLAME_CREATE_SETTINGS,
    "publish": DEFAULT_FLAME_PUBLISH_SETTINGS,
    "load": DEFAULT_FLAME_LOADER_SETTINGS
}