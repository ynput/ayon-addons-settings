from pydantic import Field, validator
from openpype.settings import BaseSettingsModel, Field

from .workfile_builder import WorkfileBuilderPlugin

from .plugins import (
    PublishPluginsModel,
    LoadPluginsModel,
)

class PublishFiltersModel(BaseSettingsModel):
    _layout = "expanded"
    name: str = Field(title="Name")
    value: str = Field(
        "",
        title="JSON",
        widget="textarea",
    )


class TvpaintSettings(BaseSettingsModel):
    stop_timer_on_application_exit: bool = Field(
        False,
        title="Stop timer on application exit")

    publish: PublishPluginsModel = Field(default_factory=PublishPluginsModel, title="Publish plugins")
    load: LoadPluginsModel = Field(default_factory=LoadPluginsModel, title="Load plugins")
    workfile_builder: WorkfileBuilderPlugin = Field(
        default_factory=WorkfileBuilderPlugin,
        title="Workfile Builder"
    )
    filters: list[PublishFiltersModel] = Field(
        default_factory=list
    )


DEFAULT_VALUES = {
    "stop_timer_on_application_exit": True,
    "publish": {
        "CollectRenderScene": {
            "enabled": False,
            "render_layer": "Main"
        },
        "ExtractSequence": {
            "review_bg": "#ffffff", #TODO: this used to have alpha
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
    # "filters": {}
}