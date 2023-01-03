from pydantic import Field, validator

from ayon_server.settings import BaseSettingsModel, ensure_unique_names


class GizmoSettings(BaseSettingsModel):
    """Nuke gizmo project settings. """

    sub_input_field_one: str = Field(
        title="Sub input field one"
    )


DEFAULT_GIZMO_SETTINGS = {
    "sub_input_field_one": "This Text"
}
