from ayon_server.settings import BaseSettingsModel, Field

class EntityPattern(BaseSettingsModel):
    episode: str = Field(title="Episode")
    sequence: str = Field(title="Sequence")
    shot: str = Field(title="Shot")

class IntegrateKitsuNotes(BaseSettingsModel):
    set_status_note: bool = Field(title="Set status on note")
    note_status_shortname: str = Field(title="Note shortname")

class PublishPlugins(BaseSettingsModel):
    IntegrateKitsuNote:  IntegrateKitsuNotes = Field(
        default_factory=IntegrateKitsuNotes,
        title="Integrate Kitsu Note"
        )


class KitsuSettings(BaseSettingsModel):
    server: str = Field(
        "",
        title="Kitsu Server"
    )
    entities_naming_pattern: EntityPattern = Field(
        default_factory=EntityPattern, 
        title="Entities naming pattern")
    publish: PublishPlugins = Field(
        default_factory=PublishPlugins,
        title="Publish plugins"
        )



DEFAULT_VALUES = {
    "entities_naming_pattern": {
        "episode": "E##",
        "sequence": "SQ##",
        "shot": "SH##"
    },
    "publish": {
        "IntegrateKitsuNote": {
            "set_status_note": False,
            "note_status_shortname": "wfa"
        }
    }
}
