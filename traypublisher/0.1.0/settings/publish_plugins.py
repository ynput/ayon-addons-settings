from pydantic import Field

from ayon_server.settings import BaseSettingsModel


class ValidateFrameRangeModel(BaseSettingsModel):
    """Allows to publish multiple video files in one go. <br />Name of matching
     asset is parsed from file names ('asset.mov', 'asset_v001.mov',
     'my_asset_to_publish.mov')"""
    _isGroup = True
    enabled: bool = True
    optional: bool = Field(False, title="Optional")
    active: bool = Field(True, title="Active")


class TrayPublisherPublishPlugins(BaseSettingsModel):
    ValidateFrameRange: ValidateFrameRangeModel = Field(
        title="Validate Frame Range",
        default_factory=ValidateFrameRangeModel,
    )
