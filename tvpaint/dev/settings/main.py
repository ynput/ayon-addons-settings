from pydantic import Field, validator
from ayon_server.settings import (
    BaseSettingsModel,
    ImageIOBaseModel,
    ensure_unique_names,
)

from .workfile_builder import WorkfileBuilderPlugin

from .plugins import (
    PublishPluginsModel,
    LoadPluginsModel,
)


class PublishGUIFilterItemModel(BaseSettingsModel):
    _layout = "compact"
    name: str = Field(title="Name")
    value: bool = Field(True, title="Active")


class PublishGUIFiltersModel(BaseSettingsModel):
    _layout = "compact"
    name: str = Field(title="Name")
    value: list[PublishGUIFilterItemModel] = Field(default_factory=list)

    @validator("value")
    def validate_unique_outputs(cls, value):
        ensure_unique_names(value)
        return value


class TvpaintSettings(BaseSettingsModel):
    imageio: ImageIOBaseModel = Field(
        default_factory=ImageIOBaseModel,
        title="OCIO config"
    )
    stop_timer_on_application_exit: bool = Field(
        False,
        title="Stop timer on application exit")

    publish: PublishPluginsModel = Field(
        default_factory=PublishPluginsModel,
        title="Publish plugins")
    load: LoadPluginsModel = Field(
        default_factory=LoadPluginsModel,
        title="Load plugins")
    workfile_builder: WorkfileBuilderPlugin = Field(
        default_factory=WorkfileBuilderPlugin,
        title="Workfile Builder"
    )
    filters: list[PublishGUIFiltersModel] = Field(
        default_factory=list,
        title="Publish GUI Filters")

    @validator("filters")
    def validate_unique_outputs(cls, value):
        ensure_unique_names(value)
        return value


DEFAULT_VALUES = {
    "stop_timer_on_application_exit": True,
    "publish": {
        "CollectRenderScene": {
            "enabled": False,
            "render_layer": "Main"
        },
        "ExtractSequence": {
            "review_bg": [255, 255, 255, 1.0],
            "families_to_review": [
                "review",
                "renderlayer",
                "renderscene"
            ]
        },
        "ValidateProjectSettings": {
            "enabled": True,
            "optional": True,
            "active": True
        },
        "ValidateMarks": {
            "enabled": True,
            "optional": True,
            "active": True
        },
        "ValidateStartFrame": {
            "enabled": False,
            "optional": True,
            "active": True
        },
        "ValidateAssetName": {
            "enabled": True,
            "optional": True,
            "active": True
        },
        "ExtractConvertToEXR": {
            "enabled": False,
            "replace_pngs": True,
            "exr_compression": "ZIP"
        }
    },
    "load": {
        "LoadImage": {
            "defaults": {
                "stretch": True,
                "timestretch": True,
                "preload": True
            }
        },
        "ImportImage": {
            "defaults": {
                "stretch": True,
                "timestretch": True,
                "preload": True
            }
        }
    },
    "workfile_builder": {
        "create_first_version": False,
        "custom_templates": []
    },
    "filters": []
}