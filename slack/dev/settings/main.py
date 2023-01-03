from pydantic import Field
from openpype.settings.common import BaseSettingsModel

from .publish_plugins import SlackPublishPlugins


class SlackSettings(BaseSettingsModel):
    """Slack project settings."""
    enabled: bool = Field(default=True)
    token: str = Field("", title="Auth Token")

    publish: SlackPublishPlugins = Field(
        title="Publish plugins",
        description="Fill combination of families, task names and hosts " 
                    "when to send notification",
    )


DEFAULT_SLACK_SETTING = {
    "token": "",
    "publish": {
        "CollectSlackFamilies": {
            "enabled": True,
            "optional": True,
            "profiles": [
                {
                    "families": [],
                    "hosts": [],
                    "task_types": [],
                    "tasks": [],
                    "subsets": [],
                    "review_upload_limit": 50.0,
                    "channel_messages": []
                }
            ]
        }
    }
}
