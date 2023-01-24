from ayon_server.settings import (
    BaseSettingsModel,
    task_types_enum,
    Field
)
from .common import PathsTemplate


class TemplatedWorkfileProfileModel(BaseSettingsModel):
    task_types: list[str] = Field(
        default_factory=list,
        title="Task types",
        enum_resolver=task_types_enum
    )
    task_names: list[str] = Field(
        default_factory=list,
        title="Task names"
    )
    path: PathsTemplate = Field(
        default_factory=PathsTemplate,
        title="Path to template"
    )
    keep_placeholder: bool = Field(
        False,
        title="Keep placeholders")
