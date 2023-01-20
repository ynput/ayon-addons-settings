from ayon_server.settings import BaseSettingsModel, Field


class PublisherPluginsSettings(BaseSettingsModel):
    """Nuke publisher plugins project settings."""

    sub_input_field_one: str = Field(
        title="Sub input field one"
    )


DEFAULT_PUBLISH_SETTINGS = {
    "sub_input_field_one": "This Text"
}
