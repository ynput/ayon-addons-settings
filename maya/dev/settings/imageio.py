"""Providing models and setting values for image IO in Maya.

Note: Names were changed to get rid of the versions in class names.
"""
from pydantic import Field

from ayon_server.settings import BaseSettingsModel, MultiplatformPathListModel


class ColorManagementPreferenceV2Model(BaseSettingsModel):
    """Color Management Preference v2 (Maya 2022+)."""
    _layout = "expanded"

    enabled: bool = Field(True, title="Use Color Management Preference v2")
    configFilePath: MultiplatformPathListModel = Field(
        default_factory=MultiplatformPathListModel,
        title="OCIO Config File Path"
    )
    renderSpace: str = Field(title="Rendering Space")
    displayName: str = Field(title="Display")
    viewName: str = Field(title="View")


class ColorManagementPreferenceModel(BaseSettingsModel):
    """Color Management Preference (legacy)."""
    _layout = "expanded"

    configFilePath: MultiplatformPathListModel = Field(
        default_factory=MultiplatformPathListModel,
        title="OCIO Config File Path"
    )
    renderSpace: str = Field(title="Rendering Space")
    viewTransform: str = Field(title="Viewer Transform ")


class ImageIOSettings(BaseSettingsModel):
    """Maya color management project settings.

    Todo: What to do with color management preferences version?
    """

    _isGroup: bool = True

    colorManagementPreference_v2: ColorManagementPreferenceV2Model = Field(
        default_factory=ColorManagementPreferenceV2Model,
        title="Color Management Preference v2 (Maya 2022+)"
    )
    colorManagementPreference: ColorManagementPreferenceModel = Field(
        default_factory=ColorManagementPreferenceModel,
        title="Color Management Preference (legacy)"
    )


DEFAULT_IMAGEIO_SETTINGS = {
        "colorManagementPreference_v2": {
            "enabled": True,
            "configFilePath": {
                "windows": [],
                "darwin": [],
                "linux": []
            },
            "renderSpace": "ACEScg",
            "displayName": "sRGB",
            "viewName": "ACES 1.0 SDR-video"
        },
        "colorManagementPreference": {
            "configFilePath": {
                "windows": [],
                "darwin": [],
                "linux": []
            },
            "renderSpace": "scene-linear Rec 709/sRGB",
            "viewTransform": "sRGB gamma"
        }
    }
