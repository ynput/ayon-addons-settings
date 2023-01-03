from pydantic import Field, validator

from ayon_server.settings import BaseSettingsModel, ensure_unique_names


class CreatorPluginsSettings(BaseSettingsModel):
    """Nuke creator plugins project settings."""

    sub_input_field_one: str = Field(
        title="Sub input field one"
    )


DEFAULT_CREATE_SETTINGS = {
    "sub_input_field_one": "This Text"
}
