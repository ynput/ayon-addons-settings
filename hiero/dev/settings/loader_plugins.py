from ayon_server.settings import Field, BaseSettingsModel


class LoadClipModel(BaseSettingsModel):
    enabled: bool = Field(
        True,
        title="Enabled"
    )

    families: list[str] = Field(
        default_factory=list,
        title="Families"
    )
    representations: list[str] = Field(
        default_factory=list,
        title="Representations"
    )

    clip_name_template: str = Field(
        "{asset}_{subset}<_{output}>",
        title="Clip name template"
    )


class LoaderPuginsModel(BaseSettingsModel):
    LoadClip: LoadClipModel = Field(
        default_factory=LoadClipModel,
        title="Load Clip"
    )

DEFAULT_FLAME_LOADER_SETTINGS = {
    "LoadClip": {
        "enabled": True,
        "families": [
            "render2d",
            "source",
            "plate",
            "render",
            "review"
        ],
        "representations": [
            "exr",
            "dpx",
            "jpg",
            "jpeg",
            "png",
            "h264",
            "mov",
            "mp4",
        ],
        "clip_name_template": "{asset}_{subset}<_{output}>"
    }
}