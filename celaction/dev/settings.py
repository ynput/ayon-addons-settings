from ayon_server.settings import BaseSettingsModel, Field


class CollectRenderPathModel(BaseSettingsModel):
    output_extension: str = Field(
        "",
        title="Output render file extension"
    )
    anatomy_template_key_render_files: str = Field(
        "",
        title="Anatomy template key: render files"
    )
    anatomy_template_key_metadata: str = Field(
        "",
        title="Anatomy template key: metadata job file"
    )


class PublishPuginsModel(BaseSettingsModel):
    CollectRenderPath: CollectRenderPathModel = Field(
        default_factory=CollectRenderPathModel,
        title="Collect Render Path"
    )


class CelActionSettings(BaseSettingsModel):
    publish: PublishPuginsModel = Field(
        default_factory=PublishPuginsModel,
        title="Publish plugins",
    )


DEFAULT_VALUES = {
    "publish": {
        "CollectRenderPath": {
            "output_extension": "png",
            "anatomy_template_key_render_files": "render",
            "anatomy_template_key_metadata": "render"
        }
    }
}