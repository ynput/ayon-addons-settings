from pydantic import Field
from ayon_server.settings.common import BaseSettingsModel

from .loader_plugins import HarmonyLoaderPlugins
from .publish_plugins import HarmonyPublishPlugins


class HarmonySettings(BaseSettingsModel):
    """Harmony Project Settings."""

    load: HarmonyLoaderPlugins = Field(
        default_factory=HarmonyLoaderPlugins,
        title="Loader plugins"
    )

    publish: HarmonyPublishPlugins = Field(
        default_factory=HarmonyPublishPlugins,
        title="Publish plugins"
    )


DEFAULT_HARMONY_SETTING = {
    "load": {
        "ImageSequenceLoader": {
            "family": [
                "shot",
                "render",
                "image",
                "plate",
                "reference"
            ],
            "representations": [
                "jpeg",
                "png",
                "jpg"
            ]
        }
    },
    "publish": {
        "CollectPalettes": {
            "allowed_tasks": [
                ".*"
            ]
        },
        "ValidateAudio": {
            "enabled": True,
            "optional": True,
            "active": True
        },
        "ValidateContainers": {
            "enabled": True,
            "optional": True,
            "active": True
        },
        "ValidateSceneSettings": {
            "enabled": True,
            "optional": True,
            "active": True,
            "frame_check_filter": [],
            "skip_resolution_check": [],
            "skip_timelines_check": []
        }
    }
}
