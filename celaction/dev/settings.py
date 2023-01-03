from ayon_server.settings import BaseSettingsModel, Field


class ExtractCelactionDeadlineModel(BaseSettingsModel):
    enabled: bool = Field(
        True,
        title="Enabled"
    )
    deadline_department: str = Field(
        "",
        title="Deadline apartment"
    )
    deadline_priority: int = Field(
        50,
        title="Deadline priority"
    )
    deadline_pool: str = Field(
        "",
        title="Deadline pool"
    )
    deadline_pool_secondary: str = Field(
        "",
        title="Deadline pool (secondary)"
    )
    deadline_group: str = Field(
        "",
        title="Deadline Group"
    )
    deadline_chunk_size: int = Field(
        10,
        title="Deadline Chunk size"
    )


class PublishPuginsModel(BaseSettingsModel):
    ExtractCelactionDeadline: ExtractCelactionDeadlineModel = Field(
        default_factory=ExtractCelactionDeadlineModel,
        title="ExtractCelactionDeadline"
    )


class CelActionSettings(BaseSettingsModel):
    publish: PublishPuginsModel = Field(
        default_factory=PublishPuginsModel,
        title="Publish plugins",
    )


DEFAULT_VALUES = {
    "publish": {
        "ExtractCelactionDeadline": {
            "enabled": True,
            "deadline_department": "",
            "deadline_priority": 50,
            "deadline_pool": "",
            "deadline_pool_secondary": "",
            "deadline_group": "",
            "deadline_chunk_size": 10
        }
    }
}