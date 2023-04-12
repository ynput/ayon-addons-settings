from ayon_server.settings import Field, BaseSettingsModel


class LoadClipModel(BaseSettingsModel):
    enabled: bool = Field(True)

    families: list[str] = Field(
        default_factory=list,
        title="Families"
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
    layer_rename_template: str = Field("", title="Layer name template")
    layer_rename_patterns: list[str] = Field(
        default_factory=list,
        title="Layer rename patters",
    )


class LoadClipBatchModel(BaseSettingsModel):
    enabled: bool = Field(True)
    families: list[str] = Field(
        default_factory=list,
        title="Families"
    )
    reel_name: str = Field(
        "OP_LoadedReel",
        title="Reel name"
    )
    clip_name_template: str = Field(
        "{batch}_{asset}_{subset}<_{output}>",
        title="Clip name template"
    )
    layer_rename_template: str = Field("", title="Layer name template")
    layer_rename_patterns: list[str] = Field(
        default_factory=list,
        title="Layer rename patters",
    )


class LoaderPluginsModel(BaseSettingsModel):
    LoadClip: LoadClipModel = Field(
        default_factory=LoadClipModel,
        title="Load Clip"
    )
    LoadClipBatch: LoadClipBatchModel = Field(
        default_factory=LoadClipBatchModel,
        title="Load as clip to current batch"
    )


DEFAULT_LOADER_SETTINGS = {
    "LoadClip": {
        "enabled": True,
        "families": [
            "render2d",
            "source",
            "plate",
            "render",
            "review"
        ],
        "reel_group_name": "OpenPype_Reels",
        "reel_name": "Loaded",
        "clip_name_template": "{asset}_{subset}<_{output}>",
        "layer_rename_template": "{asset}_{subset}<_{output}>",
        "layer_rename_patterns": [
            "rgb",
            "rgba"
        ]
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
        "reel_name": "OP_LoadedReel",
        "clip_name_template": "{batch}_{asset}_{subset}<_{output}>",
        "layer_rename_template": "{asset}_{subset}<_{output}>",
        "layer_rename_patterns": [
            "rgb",
            "rgba"
        ]
    }
}
