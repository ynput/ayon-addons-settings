from ayon_server.settings import BaseSettingsModel, Field


class LoaderPluginsSettings(BaseSettingsModel):
    """Nuke loader plugins project settings."""

    sub_input_field_one: str = Field(
        title="Sub input field one"
    )


DEFAULT_LOAD_SETTINGS = {
    "sub_input_field_one": "This Text"
}
