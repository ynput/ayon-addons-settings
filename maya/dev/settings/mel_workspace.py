from pydantic import Field

from ayon_server.settings import BaseSettingsModel


class MelWorkspaceModel(BaseSettingsModel):
    """Maya MEL Workspace."""
    mel_workspace: str = Field(title="Maya MEL Workspace", widget="textarea")


DEFAULT_MEL_WORKSPACE_SETTINGS = {
    "mel_workspace": ("""
workspace -fr "shaders" "renderData/shaders";
workspace -fr "images" "renders/maya";
workspace -fr "particles" "particles";
workspace -fr "mayaAscii" "";
workspace -fr "mayaBinary" "";
workspace -fr "scene" "";
workspace -fr "alembicCache" "cache/alembic";
workspace -fr "renderData" "renderData";
workspace -fr "sourceImages" "sourceimages";
workspace -fr "fileCache" "cache/nCache";
""")}
