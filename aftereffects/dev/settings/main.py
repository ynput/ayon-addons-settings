from pydantic import Field
from ayon_server.settings.common import BaseSettingsModel

from .creator_plugins import AfterEffectsCreatorPlugins
from .publish_plugins import AfterEffectsPublishPlugins
from .workfile_builder import WorkfileBuilderPlugin


class AfterEffectsSettings(BaseSettingsModel):
    """AfterEffects Project Settings."""
    create: AfterEffectsCreatorPlugins = Field(
        default_factory=AfterEffectsCreatorPlugins,
        title="Creator plugins"
    )

    publish: AfterEffectsPublishPlugins = Field(
        default_factory=AfterEffectsPublishPlugins,
        title="Publish plugins"
    )

    workfile_builder: WorkfileBuilderPlugin = Field(
        default_factory=WorkfileBuilderPlugin,
        title="Workfile Builder"
    )


DEFAULT_AFTEREFFECTS_SETTING = {
    "create": {
        "RenderCreator": {
            "defaults": [
                "Main"
            ]
        }
    },
    "publish": {
        "ValidateSceneSettings": {
            "enabled": True,
            "optional": True,
            "active": True,
            "skip_resolution_check": [
                ".*"
            ],
            "skip_timelines_check": [
                ".*"
            ]
        }
    },
    "workfile_builder": {
        "create_first_version": False,
        "custom_templates": []
    }
}
