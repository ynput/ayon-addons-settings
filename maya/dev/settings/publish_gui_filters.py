
from pydantic import Field
from ayon_server.settings.common import BaseSettingsModel


class GUIFiltersModel(BaseSettingsModel):
    _layout = "compact"
    name: str = Field(title="Name")
    value: str = Field("{}", title="JSON", widget="textarea")


class PublishFiltersModel(BaseSettingsModel):
     _layout = "expanded"
     filters: list[GUIFiltersModel] = Field(default_factory=list, title="Publish GUI Filters")


DEFAULT_GUI_FILTERS_SETTINGS = {
    "filters": [
        {"name": "preset 1",
        "value": "{\n   \"ValidateNoAnimation\": false,\n   \"ValidateShapeDefaultNames\": false\n}"
        },
        {"name": "preset 2",
        "value": "{\n   \"ValidateNoAnimation\": false,\n}"
        }
    ]
}

