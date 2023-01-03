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

    reel_group_name: str = Field(
        "OpenPype_Reels",
        title="Reel group name"
    )
    reel_name: str = Field(
        "Loaded",
        title="Reel name"
    )

    clip_name_template: str = Field(
        "{asset}_{subset}<_{output}>",
        title="Clip name template"
    )


class LoadClipBatchModel(BaseSettingsModel):
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

    reel_name: str = Field(
        "OP_LoadedReel",
        title="Reel name"
    )

    clip_name_template: str = Field(
        "{batch}_{asset}_{subset}<_{output}>",
        title="Clip name template"
    )


class LoaderPuginsModel(BaseSettingsModel):
    load_clip: LoadClipModel = Field(
        default_factory=LoadClipModel,
        title="Load Clip"
    )
    load_clip_batch: LoadClipBatchModel = Field(
        default_factory=LoadClipBatchModel,
        title="Load as clip to current batch"
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
            "exr16fpdwaa"
        ],
        "reel_group_name": "OpenPype_Reels",
        "reel_name": "Loaded",
        "clip_name_template": "{asset}_{subset}<_{output}>"
    },
    "LoadClipBatch": {
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
            "exr16fpdwaa"
        ],
        "reel_name": "OP_LoadedReel",
        "clip_name_template": "{batch}_{asset}_{subset}<_{output}>"
    }
}