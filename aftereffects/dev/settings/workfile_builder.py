from pydantic import Field

from ayon_server.settings import BaseSettingsModel


class PathsTemplate(BaseSettingsModel):
    windows: str = Field(
        '',
        title="Windows"
    )
    darwin: str = Field(
        '',
        title="MacOS"
    )
    linux: str = Field(
        '',
        title="Linux"
    )


class CustomBuilderTemplate(BaseSettingsModel):
    task_types: list[str] = Field(
        default_factory=list,
        title="Task types",
    )
    template_path: PathsTemplate = Field(
        default_factory=PathsTemplate
    )


class WorkfileBuilderPlugin(BaseSettingsModel):
    _title = "Workfile Builder"
    create_first_version: bool = Field(
        False,
        title="Create first workfile"
    )

    custom_templates: list[CustomBuilderTemplate] = Field(
        default_factory=CustomBuilderTemplate
    )



