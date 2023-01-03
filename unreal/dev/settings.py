from ayon_server.settings import BaseSettingsModel, Field


class ProjectSetup(BaseSettingsModel):
    dev_mode: bool = Field(
        True,
        title="Dev mode"
    )


class UnrealSettings(BaseSettingsModel):
    level_sequences_for_layouts: bool = Field(
        False,
        title="Generate level sequences when loading layouts"
    )
    delete_unmatched_assets: bool = Field(
        False,
        title="Delete assets that are not matched"
    )

    project_setup: ProjectSetup = Field(
        default_factory=ProjectSetup,
        title="Project Setup",
    )


DEFAULT_VALUES = {
    "level_sequences_for_layouts": False,
    "delete_unmatched_assets": False,
    "project_setup": {
        "dev_mode": True
    }
}