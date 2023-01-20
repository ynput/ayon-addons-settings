from ayon_server.settings import BaseSettingsModel, Field


class WorkfileBuilderSettings(BaseSettingsModel):
    """Nuke templated workfile build project settings. """

    sub_input_field_one: str = Field(
        title="Sub input field one"
    )


DEFAULT_WORKFILE_BUILDER_SETTINGS = {
    "sub_input_field_one": "This Text"
}
