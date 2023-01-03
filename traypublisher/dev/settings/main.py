from pydantic import Field
from ayon_server.settings.common import BaseSettingsModel

from .simple_creators import SimpleCreatorPlugin
from .editorial_creators import TraypublisherEditorialCreatorPlugins
from .creator_plugins import BatchMovieCreatorPlugin
from .publish_plugins import TrayPublisherPublishPlugins


class TraypublisherSettings(BaseSettingsModel):
    """Traypublisher Project Settings."""
    simple_creators: list[SimpleCreatorPlugin] = Field(
        title="Creator plugins",
        default_factory=SimpleCreatorPlugin,
    )
    #
    editorial_creators: TraypublisherEditorialCreatorPlugins = Field(
        title="Editorial Creators",
        default_factory=TraypublisherEditorialCreatorPlugins,
    )

    BatchMovieCreator: BatchMovieCreatorPlugin = Field(
        title="Batch Movie Creator",
        default_factory=BatchMovieCreatorPlugin
    )

    publish: TrayPublisherPublishPlugins = Field(
        title="Publish Plugins",
        default_factory=TrayPublisherPublishPlugins
    )


DEFAULT_TRAYPUBLISHER_SETTING = {
    "simple_creators": [
        {
            "family": "workfile",
            "identifier": "",
            "label": "Workfile",
            "icon": "fa.file",
            "default_variants": [
                "Main"
            ],
            "description": "Backup of a working scene",
            "detailed_description": "Workfiles are full scenes from any application that are directly edited by artists. They represent a state of work on a task at a given point and are usually not directly referenced into other scenes.",
            "allow_sequences": False,
            "allow_multiple_items": False,
            "extensions": [
                ".ma",
                ".mb",
                ".nk",
                ".hrox",
                ".hip",
                ".hiplc",
                ".hipnc",
                ".blend",
                ".scn",
                ".tvpp",
                ".comp",
                ".zip",
                ".prproj",
                ".drp",
                ".psd",
                ".psb",
                ".aep"
            ]
        }
    ],
    "editorial_creators": {
        "editorial_simple": {
            "default_variants": [
                "Main"
            ],
            "clip_name_tokenizer": {
                "_sequence_": "(sc\\d{3})",
                "_shot_": "(sh\\d{3})"
            },
            "shot_metadata_creator": {
                "shot_rename": {
                    "enabled": True,
                    "shot_rename_template": "{project[code]}_{_sequence_}_{_shot_}"
                },
                "shot_hierarchy": {
                    "enabled": True,
                    "parents_path": "{project}/{folder}/{sequence}",
                    "parents": [
                        {
                            "type": "Project",
                            "name": "project",
                            "value": "{project[name]}"
                        },
                        {
                            "type": "Folder",
                            "name": "folder",
                            "value": "shots"
                        },
                        {
                            "type": "Sequence",
                            "name": "sequence",
                            "value": "{_sequence_}"
                        }
                    ]
                }
            },
            "shot_add_tasks": {},
            "shot_subset_creator": {
                "family_presets": [
                    {
                        "family": "review",
                        "variant": "Reference",
                        "review": True,
                        "output_file_type": ".mp4"
                    },
                    {
                        "family": "plate",
                        "variant": "",
                        "review": False,
                        "output_file_type": ".mov"
                    },
                    {
                        "family": "audio",
                        "variant": "",
                        "review": False,
                        "output_file_type": ".wav"
                    }
                ]
            }
        }
    },
    "BatchMovieCreator": {
        "default_variants": [
            "Main"
        ],
        "default_tasks": [
            "Compositing"
        ],
        "extensions": [
            ".mov"
        ]
    },
    "publish": {
        "ValidateFrameRange": {
            "enabled": True,
            "optional": True,
            "active": True
        }
    }
}
