from pydantic import Field
from openpype.settings.common import BaseSettingsModel
from .imageio import ImageIOSettings, DEFAULT_IMAGEIO_SETTINGS
from .mel_workspace import MelWorkspaceModel, DEFAULT_MEL_WORKSPACE_SETTINGS
from .ext_mapping import ExtMappingModel, DEFAULT_EXT_MAPPING_SETTINGS
from .maya_dirmap import MayaDirmapModel, DEFAULT_MAYA_DIRMAP_SETTINGS
from .scriptsmenu import ScriptsmenuModel, DEFAULT_SCRIPTSMENU_SETTINGS
from .render_settings import RenderSettingsModel, DEFAULT_RENDER_SETTINGS
# from .creators import CreatorsModel, DEFAULT_CREATORS_SETTINGS


class MayaSettings(BaseSettingsModel):
    """Maya Project Settings."""
    _layout = "expanded"

    imageio: ImageIOSettings = Field(
        default_factory=ImageIOSettings, title="Color Management (imageio)")
    mel_workspace: MelWorkspaceModel = Field(
        default_factory=MelWorkspaceModel, title="Maya MEL Workspace")
    ext_mapping: ExtMappingModel = Field(
        default_factory=ExtMappingModel, title="Extension Mapping")
    maya_dirmap: MayaDirmapModel = Field(
        default_factory=MayaDirmapModel, title="Maya dirmap Settings")
    scriptsmenu: ScriptsmenuModel = Field(
        default_factory=ScriptsmenuModel, title="Scriptsmenu Settings")
    render_settings: RenderSettingsModel = Field(
        default_factory=RenderSettingsModel, title="Render Settings")
    # creators: CreatorsModel = Field(
    #     default_factory=CreatorsModel, title="Creators")


DEFAULT_MAYA_SETTING = {
    "imageio": DEFAULT_IMAGEIO_SETTINGS,
    "mel_workspace": DEFAULT_MEL_WORKSPACE_SETTINGS,
    "ext_mapping": DEFAULT_EXT_MAPPING_SETTINGS,
    # `maya_dirmap` was originally with dash - `maya-dirmap`
    "maya_dirmap": DEFAULT_MAYA_DIRMAP_SETTINGS,
    "scriptsmenu": DEFAULT_SCRIPTSMENU_SETTINGS,
    "render_settings": DEFAULT_RENDER_SETTINGS,
    # "creators": DEFAULT_CREATORS_SETTINGS
}
