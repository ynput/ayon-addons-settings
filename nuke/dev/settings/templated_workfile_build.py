from pydantic import Field, validator

from openpype.settings import BaseSettingsModel, ensure_unique_names


class TemplatedWorkfileBuildSettings(BaseSettingsModel):
    """Nuke templated workfile build project settings. """

    sub_input_field_one: str = Field(
        title="Sub input field one"
    )


DEFAULT_TEMPLATED_WORKFILE_BUILD_SETTINGS = {
    "sub_input_field_one": "This Text"
}
