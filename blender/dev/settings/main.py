from ayon_server.settings import (
    Field,
    BaseSettingsModel,
    PathModel
)
from ayon_server.settings.enum import task_types_enum

from .publish_plugins import (
    PublishPuginsModel,
    DEFAULT_BLENDER_PUBLISH_SETTINGS
)

class CustomTemplateModel(BaseSettingsModel):
    _layout = "expanded"
    _isGroup = True
    task_types: list[str] = Field(
        default_factory=list,
        title="Task types",
        enum_resolver=task_types_enum
    )
    path: PathModel = Field(default_factory=PathModel, title="Path")


class BlenderTemplateWorkfileOptions(BaseSettingsModel):
    create_first_version: bool = Field(
        False,
        title="Create first workfile",
    )
    custom_templates: list[CustomTemplateModel] = Field(
        default_factory=list,
        title="Custom templates",
    )


class BlenderSettings(BaseSettingsModel):
    workfile_builder: BlenderTemplateWorkfileOptions = Field(
        default_factory=BlenderTemplateWorkfileOptions,
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