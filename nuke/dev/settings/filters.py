from ayon_server.settings import BaseSettingsModel, Field

class PublishFiltersModel(BaseSettingsModel):
    _layout = "expanded"
    name: str = Field(title="Name")
    value: str = Field(
        "",
        title="JSON",
        widget="textarea",
    )