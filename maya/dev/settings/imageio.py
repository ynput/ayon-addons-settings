"""Providing models and setting values for image IO in Maya.

Note: Names were changed to get rid of the versions in class names.
"""
from pydantic import Field

from ayon_server.settings import BaseSettingsModel


class PathsTemplate(BaseSettingsModel):
    """Path template for multiplatform paths.

    Todo:
        This should be unified across the addons.
    """
    windows: list[str] = Field(title="Windows")
    darwin: list[str] = Field(title="MacOS")
    linux: list[str] = Field(title="Linux")


class ColorManagementPreferencesModel(BaseSettingsModel):
    """Color Management Preference v2 (Maya 2022+)."""
    _layout = "expanded"

    enabled: bool = Field(True, title="Use Color Management Preference v2")
    configFilePath: PathsTemplate = Field(default_factory=PathsTemplate, title="OCIO Config File Path")
    renderSpace: str = Field(title="Rendering Space")
    displayName: str = Field(title="Display")
    viewName: str = Field(title="View")


class ColorManagementPreferencesLegacyModel(BaseSettingsModel):
    """Color Management Preference (legacy)."""
    _layout = "expanded"

    configFilePath: PathsTemplate = Field(default_factory=PathsTemplate, title="OCIO Config File Path")
    renderSpace: str = Field(title="Rendering Space")
    viewTransform: str = Field(title="Viewer Transform ")


class ImageIOSettings(BaseSettingsModel):
    """Maya color management project settings.

    Todo: What to do with color management preferences version?
    """

    _isGroup: bool = True

    ColorManagementPreferences: ColorManagementPreferencesModel = Field(
        default_factory=ColorManagementPreferencesModel,
        title="Color Management Preference v2 (Maya 2022+)"
    )
    ColorManagementPreferencesLegacy: ColorManagementPreferencesLegacyModel = Field(
        default_factory=ColorManagementPreferencesLegacyModel,
        title="Color Management Preference (legacy)"
    )


DEFAULT_IMAGEIO_SETTINGS = {
        "ColorManagementPreferences": {
            "enabled": True,
            "configFilePath": {
                "windows": [""],
                "darwin": [""],
                "linux": [""]
            },
            "renderSpace": "ACEScg",
            "displayName": "sRGB",
            "viewName": "ACES 1.0 SDR-video"
        },
        "ColorManagementPreferencesLegacy": {
            "configFilePath": {
                "windows": [""],
                "darwin": [""],
                "linux": [""]
            },
            "renderSpace": "scene-linear Rec 709/sRGB",
            "viewTransform": "sRGB gamma"
        }
    }
