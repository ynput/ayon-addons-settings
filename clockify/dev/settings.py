from ayon_server.settings import BaseSettingsModel, Field

class ClockifySettings(BaseSettingsModel):
    workspace_name: str = Field(
        "",
        title="Workspace name"
    )
