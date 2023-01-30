from ayon_server.settings import BaseSettingsModel, Field


class ScriptsmenuSubmodel(BaseSettingsModel):
    """Item Definition"""
    _isGroup = True

    type: str = Field(title="Type")
    command: str = Field(title="Command")
    sourcetype: str = Field(title="Source Type")
    title: str = Field(title="Title")
    tooltip: str = Field(title="Tooltip")


class ScriptsmenuSettings(BaseSettingsModel):
    """Nuke script menu project settings."""
    _isGroup = True

    # TODO: in api rename key `name` to `menu_name`
    name: str = Field(title="Menu Name")
    definition: list[ScriptsmenuSubmodel] = Field(
        default_factory=list, title="Definition", description="Scriptmenu Items Definition")


DEFAULT_SCRIPTSMENU_SETTINGS = {
    "name": "OpenPype Tools",
    "definition": [
        {
            "type": "action",
            "sourcetype": "python",
            "title": "OpenPype Docs",
            "command": "import webbrowser;webbrowser.open(url='https://openpype.io/docs/artist_hosts_nuke_tut')",
            "tooltip": "Open the OpenPype Nuke user doc page"
        }
    ]
}
