from ayon_server.settings import BaseSettingsModel, Field

class ClockifySettings(BaseSettingsModel):
    worskpace_name: str = Field(
        "",
        title="Workspace name"
    )
