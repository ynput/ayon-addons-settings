from pydantic import Field, validator

from ayon_server.settings import BaseSettingsModel, normalize_name, ensure_unique_names


class DictLikeSubmodel(BaseSettingsModel):
    _layout = "expanded"

    name: str = Field("", title="Name")
    shotgrid_url: str = Field("", title="Server URL")
    shotgrid_script_name: str = Field("", title="Script name")
    shotgrid_script_key: str = Field("", title="Script API key")
    
    @validator("name")
    def validate_name(cls, value):
        """Ensure name does not contain weird characters"""
        return normalize_name(value)


class AssetModel(BaseSettingsModel):
    asset_type: str = Field("sg_asset_type", title="Asset type")  #TODO: changed from type


class SequenceModel(BaseSettingsModel):
    episode_link: str = Field("episode", title="Episode link") 


class ShotModel(BaseSettingsModel):
    episode_link: str = Field("sg_episode", title="Episode link") 
    sequence_link: str = Field("sg_sequence", title="Sequence link")


class TaskModel(BaseSettingsModel):
    task: str = Field("step", title="Step link") 


class EventHandlerModel(BaseSettingsModel):
    enabled: bool = Field(title="Enabled")


class FieldsModel(BaseSettingsModel):
    asset: AssetModel = Field(default_factory=AssetModel, title="Asset")
    sequence: SequenceModel = Field(default_factory=SequenceModel, title="Sequence")
    shot: ShotModel = Field(default_factory=ShotModel, title="Shot")
    task: TaskModel = Field(default_factory=TaskModel, title="Task")


class ShotgridSettings(BaseSettingsModel):
    leecher_manager_url: str = Field(
        "",
        title="Shotgrid Leecher Manager URL"
    )
    leecher_backend_url: str = Field(
        "",
        title="Shotgrid Leecher Backend URL"
    )
    filter_projects_by_login: bool = Field(
        False,
        title="Filter projects by SG login")
    shotgrid_settings: list[DictLikeSubmodel] = Field(
        default_factory=list,
        title="Shotgrid Servers"
    )
    shotgrid_project_id: int = Field(title="Shotgrid project id")
    shotgrid_server: str = Field(title="Shotgrid server")
    event: EventHandlerModel = Field(
        default_factory=EventHandlerModel,
        title="Event Handler")
    fields: FieldsModel = Field(default_factory=FieldsModel, title="Fields Template")

    @validator("shotgrid_settings")
    def validate_names(cls, value):
        ensure_unique_names(value)
        return value


DEFAULT_VALUES = {
    "shotgrid_project_id": 0,
    "shotgrid_server": "",
    "event": {
        "enabled": False
    },
    "fields": {
        "asset": {
            "asset_type": "sg_asset_type"
        },
        "sequence": {
            "episode_link": "episode"
        },
        "shot": {
            "episode_link": "sg_episode",
            "sequence_link": "sg_sequence"
        },
        "task": {
            "step": "step"
        }
    }
}



