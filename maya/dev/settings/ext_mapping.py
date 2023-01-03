from pydantic import Field

from ayon_server.settings import BaseSettingsModel


class ExtMappingSubmodel(BaseSettingsModel):
    _layout = "compact"
    name: str = Field(title="Family")
    value: str = Field(title="Extension")


class ExtMappingModel(BaseSettingsModel):
    _layout = "expanded"

    ext_mapping: list[ExtMappingSubmodel] = Field(default_factory=list, title="Extension Mapping")


DEFAULT_EXT_MAPPING_SETTINGS = {
    "ext_mapping": [
        {"name": "model", "value": "ma"},
        {"name": "mayaAscii", "value": "ma"},
        {"name": "camera", "value": "ma"},
        {"name": "rig", "value": "ma"},
        {"name": "workfile", "value": "ma"},
        {"name": "yetiRig", "value": "ma"}
    ]
}
