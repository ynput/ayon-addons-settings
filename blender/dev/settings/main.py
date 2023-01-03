from openpype.settings import Field, BaseSettingsModel, TemplateWorkfileOptions

from .publish_plugins import PublishPuginsModel, DEFAULT_BLENDER_PUBLISH_SETTINGS


class BlenderSettings(BaseSettingsModel):
    workfile_builder: TemplateWorkfileOptions = Field(
        default_factory=TemplateWorkfileOptions,
        title="Workfile Builder"
    )

    publish: PublishPuginsModel = Field(
        default_factory=PublishPuginsModel,
        title="Publish Plugins"
    )

DEFAULT_VALUES = {
    "publish": DEFAULT_BLENDER_PUBLISH_SETTINGS
}