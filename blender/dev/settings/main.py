from pydantic import Field, validator
from ayon_server.settings import (
    BaseSettingsModel,
    TemplateWorkfileBaseOptions,
    ImageIOBaseModel,
)

from .publish_plugins import (
    PublishPuginsModel,
    DEFAULT_BLENDER_PUBLISH_SETTINGS
)


class BlenderSettings(BaseSettingsModel):
    imageio: ImageIOBaseModel = Field(
        default_factory=ImageIOBaseModel,
        title="OCIO config"
    )
    workfile_builder: TemplateWorkfileBaseOptions = Field(
        default_factory=TemplateWorkfileBaseOptions,
        title="Workfile Builder"
    )

    publish: PublishPuginsModel = Field(
        default_factory=PublishPuginsModel,
        title="Publish Plugins"
    )


DEFAULT_VALUES = {
    "publish": DEFAULT_BLENDER_PUBLISH_SETTINGS,
    "workfile_builder": {
        "create_first_version": False,
        "custom_templates": []
    }
}