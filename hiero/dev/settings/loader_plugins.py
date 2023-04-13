from pydantic import Field
from ayon_server.settings import BaseSettingsModel


class LoadClipModel(BaseSettingsModel):
    enabled: bool = Field(
        True,
        title="Enabled"
    )
    families: list[str] = Field(
        default_factory=list,
        title="Families"
    )
    clip_name_template: str = Field(
        title="Clip name template"
    )


class LoaderPuginsModel(BaseSettingsModel):
    LoadClip: LoadClipModel = Field(
        default_factory=LoadClipModel,
        title="Load Clip"
    )


DEFAULT_LOADER_PLUGINS_SETTINGS = {
    "LoadClip": {
        "enabled": True,
        "families": [
            "render2d",
            "source",
            "plate",
            "render",
            "review"
        ],
        "clip_name_template": "{asset}_{subset}_{representation}"
    }
}
