from pydantic import Field

from ayon_server.settings import BaseSettingsModel


class ChannelMessage(BaseSettingsModel):
    channels: list[str] = Field(default_factory=list, title="Channels")
    upload_thumbnail: bool = Field(default=True, title="Upload thumbnail")
    upload_review: bool = Field(default=True, title="Upload review")
    message: str = Field('', title="Message")


task_types_enum = [
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


class Profile(BaseSettingsModel):

    families: list[str] = Field(default_factory=list, title="Families")
    hosts: list[str] = Field(default_factory=list, title="Hosts")
    task_types: list[str] = Field(
        default_factory=list,
        title="Task types",
        enum_resolver=lambda: task_types_enum
    )
    task_names: list[str] = Field(default_factory=list, title="Task names")
    subset_names: list[str] = Field(default_factory=list, title="Subset names")
    review_upload_limit: float = Field(
        50.0,
        title="Upload review maximum file size (MB)")

    _desc = ("Message sent to channel selected by profile. "
             "Message template can contain {} placeholders from anatomyData "
             "or {review_filepath} for too large review files to link only.")
    channel_messages: list[ChannelMessage] = Field(
        default_factory=list,
        title="Messages to channels",
        description=_desc,
        section="Messages",
        widget="textarea"
    )


class CollectSlackFamiliesPlugin(BaseSettingsModel):
    _isGroup = True
    enabled: bool = True
    optional: bool = Field(False, title="Optional")

    profiles: list[Profile] = Field(
        title="Profiles",
        default_factory=Profile
    )


class SlackPublishPlugins(BaseSettingsModel):
    CollectSlackFamilies: CollectSlackFamiliesPlugin = Field(
        title="Notification to Slack",
        default_factory=CollectSlackFamiliesPlugin,
    )
