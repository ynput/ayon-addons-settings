from pydantic import Field, validator
from ayon_server.settings import (
    BaseSettingsModel,
    TemplateWorkfileBaseOptions,
    HostImageIOBaseModel,
)

from .publish_plugins import (
    PublishPuginsModel,
    DEFAULT_BLENDER_PUBLISH_SETTINGS
)


class UnitScaleSettingsModel(BaseSettingsModel):
    enabled: bool = Field(True, title="Enabled")
    apply_on_opening: bool = Field(
        False, title="Apply on Opening Existing Files")
    base_file_unit_scale: float = Field(
        1.0, title="Base File Unit Scale"
    )


class BlenderSettings(BaseSettingsModel):
    unit_scale_settings: UnitScaleSettingsModel = Field(
        default_factory=UnitScaleSettingsModel,
        title="Set Unit Scale"
    )
    imageio: HostImageIOBaseModel = Field(
        default_factory=HostImageIOBaseModel,
        title="Color Management (ImageIO)"
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
    "unit_scale_settings": {
        "enabled": True,
        "apply_on_opening": False,
        "base_file_unit_scale": 0.01
    },
    "publish": DEFAULT_BLENDER_PUBLISH_SETTINGS,
    "workfile_builder": {
        "create_first_version": False,
        "custom_templates": []
    }
}
