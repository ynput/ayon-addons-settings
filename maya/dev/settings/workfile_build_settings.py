from pydantic import Field
from ayon_server.settings import BaseSettingsModel, task_types_enum


class ContextItemModel(BaseSettingsModel):
    _layout = "expanded"
    subset_name_filters: list[str] = Field(
        default_factory=list, title="Subset name Filters")
    families: list[str] = Field(default_factory=list, title="Families")
    repre_names: list[str] = Field(default_factory=list, title="Repre Names")
    loaders: list[str] = Field(default_factory=list, title="Loaders")


class WorkfileSettingModel(BaseSettingsModel):
    _layout = "expanded"
    task_types: list[str] = Field(default_factory=list,
        enum_resolver=task_types_enum, title="Task types")
    tasks: list[str] = Field(default_factory=list, title="Task names")
    current_context: list[ContextItemModel] = Field(
        default_factory=list,
        title="Current Context")
    linked_assets: list[ContextItemModel] = Field(
        default_factory=list,
        title="Linked Assets")


class ProfilesModel(BaseSettingsModel):
    profiles: list[WorkfileSettingModel] = Field(
        default_factory=list,
        title="Profiles"
    )


DEFAULT_WORKFILE_SETTING = {
    "profiles": [
        {
            "task_types": [],
            "tasks": [
                "Lighting"
            ],
            "current_context": [
                {
                    "subset_name_filters": [
                        ".+[Mm]ain"
                    ],
                    "families": [
                        "model"
                    ],
                    "repre_names": [
                        "abc",
                        "ma"
                    ],
                    "loaders": [
                        "ReferenceLoader"
                    ]
                },
                {
                    "subset_name_filters": [],
                    "families": [
                        "animation",
                        "pointcache",
                        "proxyAbc"
                    ],
                    "repre_names": [
                        "abc"
                    ],
                    "loaders": [
                        "ReferenceLoader"
                    ]
                },
                {
                    "subset_name_filters": [],
                    "families": [
                        "rendersetup"
                    ],
                    "repre_names": [
                        "json"
                    ],
                    "loaders": [
                        "RenderSetupLoader"
                    ]
                },
                {
                    "subset_name_filters": [],
                    "families": [
                        "camera"
                    ],
                    "repre_names": [
                        "abc"
                    ],
                    "loaders": [
                        "ReferenceLoader"
                    ]
                }
            ],
            "linked_assets": [
                {
                    "subset_name_filters": [],
                    "families": [
                        "sedress"
                    ],
                    "repre_names": [
                        "ma"
                    ],
                    "loaders": [
                        "ReferenceLoader"
                    ]
                },
                {
                    "subset_name_filters": [],
                    "families": [
                        "ArnoldStandin"
                    ],
                    "repre_names": [
                        "ass"
                    ],
                    "loaders": [
                        "assLoader"
                    ]
                }
            ]
        }
    ]
}