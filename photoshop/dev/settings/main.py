from pydantic import Field
from openpype.settings.common import BaseSettingsModel

from .creator_plugins import PhotoshopCreatorPlugins
from .publish_plugins import PhotoshopPublishPlugins
from .workfile_builder import WorkfileBuilderPlugin


class PhotoshopSettings(BaseSettingsModel):
    """Photoshop Project Settings."""
    create: PhotoshopCreatorPlugins = Field(
        default_factory=PhotoshopCreatorPlugins,
        title="Creator plugins"
    )

    publish: PhotoshopPublishPlugins = Field(
        default_factory=PhotoshopPublishPlugins,
        title="Publish plugins"
    )

    workfile_builder: WorkfileBuilderPlugin = Field(
        default_factory=WorkfileBuilderPlugin,
        title="Workfile Builder"
    )


DEFAULT_PHOTOSHOP_SETTING = {
    "create": {
        "CreateImage": {
            "defaults": [
                "Main"
            ]
        }
    },
    "publish": {
        "CollectColorCodedInstances": {
            "create_flatten_image": "no",
            "flatten_subset_template": "",
            "color_code_mapping": []
        },
        "CollectInstances": {
            "flatten_subset_template": ""
        },
        "CollectReview": {
            "publish": True
        },
        "CollectVersion": {
            "enabled": False
        },
        "ValidateContainers": {
            "enabled": True,
            "optional": True,
            "active": True
        },
        "ValidateNaming": {
            "invalid_chars": "[ \\\\/+\\*\\?\\(\\)\\[\\]\\{\\}:,;]",
            "replace_char": "_"
        },
        "ExtractImage": {
            "formats": [
                "png",
                "jpg"
            ]
        },
        "ExtractReview": {
            "make_image_sequence": False,
            "max_downscale_size": 8192,
            "jpg_options": {
                "tags": [
                    "review",
                    "ftrackreview"
                ]
            },
            "mov_options": {
                "tags": [
                    "review",
                    "ftrackreview"
                ]
            }
        }
    },
    "workfile_builder": {
        "create_first_version": False,
        "custom_templates": []
    }
}
