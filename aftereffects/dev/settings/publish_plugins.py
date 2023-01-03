from pydantic import Field

from openpype.settings import BaseSettingsModel


class ValidateSceneSettingsPlugin(BaseSettingsModel):
    """Validate naming of subsets and layers"""  #
    _isGroup = True
    enabled: bool = True
    optional: bool = Field(False, title="Optional")
    active: bool = Field(True, title="Active")

    skip_resolution_check: list[str] = Field(
        default_factory=list,
        title="Skip Resolution Check for Tasks"
    )

    skip_timelines_check: list[str] = Field(
        default_factory=list,
        title="Skip Timeline Check for Tasks"
    )


class AfterEffectsPublishPlugins(BaseSettingsModel):

    ValidateSceneSettings: ValidateSceneSettingsPlugin = Field(
        title="Validate Scene Settings",
        default_factory=ValidateSceneSettingsPlugin,
    )

