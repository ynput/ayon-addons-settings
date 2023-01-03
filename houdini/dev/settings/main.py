from pydantic import Field, validator
from ayon_server.settings import BaseSettingsModel, ensure_unique_names


from .publish_plugins import (
    PublishPluginsModel,
    CreatePluginsModel,
    DEFAULT_HOUDINI_PUBLISH_SETTINGS,
    DEFAULT_HOUDINI_CREATE_SETTINGS
)


class PathsTemplate(BaseSettingsModel):
    """Todo: This should be unified across the addons."""

    windows: str = Field("", title="Windows")
    darwin: str = Field("", title="MacOS")
    linux: str = Field("", title="Linux")


class MultiplatformStrList(BaseSettingsModel):
    """Todo: This should be unified across the addons."""

    windows: list[str] = Field(default_factory=list, title="Windows")
    linux: list[str] = Field(default_factory=list, title="Linux")
    darwin: list[str] = Field(default_factory=list, title="MacOS")


class ShelfToolsModel(BaseSettingsModel):
    name: str = Field(title="Name")
    help: str = Field(title="Help text")
    script: PathsTemplate = Field(
        default_factory=PathsTemplate,
        title="Script Path "
    )
    icon: PathsTemplate = Field(
        default_factory=PathsTemplate,
        title="Icon Path "
    )


class ShelfDefinitionModel(BaseSettingsModel):
    _layout = "expanded"
    shelf_name: str = Field(title="Shelf name")
    tools_list: list[ShelfToolsModel] = Field(
        default_factory=list,
        title="Shelf Tools"
    )

class ShelvesModel(BaseSettingsModel):
    _layout = "expanded"
    shelf_set_name: str = Field(title="Shelfs set name")

    shelf_set_source_path: MultiplatformStrList = Field(
        default_factory=MultiplatformStrList,
        title="Shelf Set Path (optional)"
    )

    shelf_definition: list[ShelfDefinitionModel] = Field(
        default_factory=list,
        title="Shelf Definitions"
    )


class HoudiniSettings(BaseSettingsModel):

    shelves: list[ShelvesModel] = Field(
        default_factory=list,
        title="Houdini Scripts Shelves",
    )

    publish: PublishPluginsModel = Field(
        default_factory=PublishPluginsModel,
        title="Publish Plugins",
    )

    create: CreatePluginsModel = Field(
        default_factory=CreatePluginsModel,
        title="Creator Plugins",
    )


DEFAULT_VALUES = {
    "shelves": [],
    "create": DEFAULT_HOUDINI_CREATE_SETTINGS,
    "publish": DEFAULT_HOUDINI_PUBLISH_SETTINGS
}
