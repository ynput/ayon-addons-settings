
from pydantic import Field
from ayon_server.settings.common import BaseSettingsModel

def task_types_enum():
    return [
    {"label": "Generic", "value": "Generic"},
    {"label": "Art", "value": "Art"},
    {"label": "Modeling", "value": "Modeling"},
    {"label": "Texture", "value": "Texture"},
    {"label": "Lookdev", "value": "Lookdev"},
    {"label": "Rigging", "value": "Rigging"},
    {"label": "Edit", "value": "Edit"},
    {"label": "Layout", "value": "Layout"},
    {"label": "Setdress", "value": "Setdress"},
    {"label": "Animation", "value": "Animation"},
    {"label": "FX", "value": "FX"},
    {"label": "Lighting", "value": "Lighting"},
    {"label": "Paint", "value": "Paint"},
    {"label": "Compositing", "value": "Compositing"},
    {"label": "Roto", "value": "Roto"},
    {"label": "Matchmove", "value": "Matchmove"}
    ]


class WorkfileBuildProfilesModel(BaseSettingsModel):
    _layout = "expanded"
    task_types: list[str] = Field(default_factory=list,
        enum_resolver=task_types_enum, title="Task types")
    task_names: list[str] = Field(default_factory=list, title="Task names")
    path: str = Field("", title="Path to template")


class TemplatedProfilesModel(BaseSettingsModel):
    profiles: list[WorkfileBuildProfilesModel]=Field(default_factory=list,
    title="Profiles")


DEFAULT_TEMPLATED_WORKFILE_SETTINGS = {
        "profiles": []
}

