from pydantic import Field, validator
from ayon_server.settings import (
    BaseSettingsModel,
    normalize_name,
    ensure_unique_names,
    task_types_enum,
)


class TimeoutProfiles(BaseSettingsModel):
    _layout = "expanded"

    hosts: list[str] = Field(default_factory=list, title="Host names")
    task_types: list[str] = Field(
        default_factory=list,
        title="Task types",
        enum_resolver=task_types_enum
    )
    timeout: int = Field(600, title="Timeout (sec)")
    
    
class TaskTypeToFamilyItemModel(BaseSettingsModel):
    _layout = "expanded"
    is_sequence: bool = Field(False, title="Is sequence")
    extensions: list[str] = Field(default_factory=list, title="Extensions")
    families: list[str] = Field(default_factory=list, title="Families")
    tags: list[str] = Field(default_factory=list, title="Tags")
    result_family: list[str] = Field(default_factory=list, title="Resulting family")


class TaskTypeToFamilyModel(BaseSettingsModel):
    _layout = "expanded"
    name: str = Field("", title="Task type")
    task_type: list[TaskTypeToFamilyItemModel] = Field(
        default_factory=list
    )

    @validator("name")
    def validate_name(cls, value):
        """Ensure name does not contain weird characters"""
        return normalize_name(value)
  

class CollectPublishedFilesModel(BaseSettingsModel):
    """Select if all versions of published items should be kept same. (As max(published) + 1.). \n
    Configure resulting family and tags on representation based on uploaded file and task. \n
    Eg. **'.png'** is uploaded >> create instance of **'render'** family **'Create review'** in Tags >> mark representation to create review from."""
    sync_next_version: bool = Field(
        True,
        title="Sync next publish version")
    task_type_to_family: list[TaskTypeToFamilyModel] = Field(
        default_factory=list,
        title="Task type to family mapping")

    @validator("task_type_to_family")
    def validate_names(cls, value):
        ensure_unique_names(value)
        return value


class CollectTVPaintInstancesModel(BaseSettingsModel):
    """Regex helps to extract render layer and pass names from TVPaint layer name.
The regex must contain named groups **'layer'** and **'pass'** which are used for creation of RenderPass instances. \n


Example layer name: **"L001_Person_Hand"** \n
Example regex: **"(?P<layer>L[0-9]{3}_\w+)_(?P<pass>.+)"** \n
Extracted layer: **"L001_Person"** \n
Extracted pass: **"Hand"** 
"""
    layer_name_regex: str = Field("", title="Layer name regex")


class PublishPluginsModel(BaseSettingsModel):
    CollectPublishedFiles: CollectPublishedFilesModel = Field(
        default_factory=CollectPublishedFilesModel, 
        title="Collect published files",
        description="")
    collectTVPaintInstances: CollectTVPaintInstancesModel = Field(
        default_factory=CollectTVPaintInstancesModel,
        title="Collect TVPaint instances"
    )


class WebpublisherSettings(BaseSettingsModel):
    timeout_profiles: list[TimeoutProfiles] = Field(
        default_factory=list, 
        title="Timeout profiles")
    publish: PublishPluginsModel = Field(default_factory=PublishPluginsModel, title="Publish plugins")


DEFAULT_VALUES = {
    "timeout_profiles": [
        {
            "hosts": [
                "photoshop"
            ],
            "task_types": [],
            "timeout": 600
        }
    ],
    "publish": {
        "CollectPublishedFiles": {
            "sync_next_version": False,
            "task_type_to_family": {
                "Animation": [
                    {
                        "is_sequence": False,
                        "extensions": [
                            "tvp"
                        ],
                        "families": [],
                        "tags": [],
                        "result_family": "workfile"
                    },
                    {
                        "is_sequence": True,
                        "extensions": [
                            "png",
                            "exr",
                            "tiff",
                            "tif"
                        ],
                        "families": [
                            "review"
                        ],
                        "tags": [
                            "review"
                        ],
                        "result_family": "render"
                    }
                ],
                "Compositing": [
                    {
                        "is_sequence": False,
                        "extensions": [
                            "aep"
                        ],
                        "families": [],
                        "tags": [],
                        "result_family": "workfile"
                    },
                    {
                        "is_sequence": True,
                        "extensions": [
                            "png",
                            "exr",
                            "tiff",
                            "tif"
                        ],
                        "families": [
                            "review"
                        ],
                        "tags": [
                            "review"
                        ],
                        "result_family": "render"
                    }
                ],
                "Layout": [
                    {
                        "is_sequence": False,
                        "extensions": [
                            "psd"
                        ],
                        "families": [],
                        "tags": [],
                        "result_family": "workfile"
                    },
                    {
                        "is_sequence": False,
                        "extensions": [
                            "png",
                            "jpg",
                            "jpeg",
                            "tiff",
                            "tif"
                        ],
                        "families": [
                            "review"
                        ],
                        "tags": [
                            "review"
                        ],
                        "result_family": "image"
                    }
                ],
                "default_task_type": [
                    {
                        "is_sequence": False,
                        "extensions": [
                            "tvp",
                            "psd"
                        ],
                        "families": [],
                        "tags": [],
                        "result_family": "workfile"
                    },
                    {
                        "is_sequence": True,
                        "extensions": [
                            "png",
                            "exr",
                            "tiff",
                            "tif"
                        ],
                        "families": [
                            "review"
                        ],
                        "tags": [
                            "review"
                        ],
                        "result_family": "render"
                    }
                ]
            }
        },
        "CollectTVPaintInstances": {
            "layer_name_regex": "(?P<layer>L[0-9]{3}_\\w+)_(?P<pass>.+)"
        }
    }
}