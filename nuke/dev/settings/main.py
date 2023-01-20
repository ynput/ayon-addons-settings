from pydantic import validator, Field

from ayon_server.settings import (
    BaseSettingsModel,
    ensure_unique_names
)


from .general import (
    GeneralSettings,
    DEFAULT_GENERAL_SETTINGS
)

from .imageio import (
    ImageIOSettings,
    DEFAULT_IMAGEIO_SETTINGS
)

from .dirmap import (
    DirmapSettings,
    DEFAULT_DIRMAP_SETTINGS
)

from .scriptsmenu import (
    ScriptsmenuSettings,
    DEFAULT_SCRIPTSMENU_SETTINGS
)

from .gizmo import (
    GizmoSettings,
    DEFAULT_GIZMO_SETTINGS
)

from .create_plugins import (
    CreatorPluginsSettings,
    DEFAULT_CREATE_SETTINGS
)

from .publish_plugins import (
    PublisherPluginsSettings,
    DEFAULT_PUBLISH_SETTINGS
)

from .loader_plugins import (
    LoaderPluginsSettings,
    DEFAULT_LOAD_SETTINGS
)

from .workfile_builder import (
    WorkfileBuilderSettings,
    DEFAULT_WORKFILE_BUILDER_SETTINGS
)

from .templated_workfile_build import (
    TemplatedWorkfileBuildSettings,
    DEFAULT_TEMPLATED_WORKFILE_BUILD_SETTINGS
)

from .filters import PublishFiltersModel


class NukeSettings(BaseSettingsModel):
    """Nuke addon settings."""

    general: GeneralSettings = Field(
        default_factory=GeneralSettings,
        title="General",
    )

    imageio: ImageIOSettings = Field(
        default_factory=ImageIOSettings,
        title="Color Management (imageio)",
    )

    # TODO: used to be `nuke-dirmap`
    dirmap: DirmapSettings = Field(
        default_factory=DirmapSettings,
        title="Nuke Directory Mapping",
    )

    scriptsmenu: ScriptsmenuSettings = Field(
        default_factory=ScriptsmenuSettings,
        title="Scripts Menu Definition",
    )

    gizmo: GizmoSettings = Field(
        default_factory=GizmoSettings,
        title="Gizmo Menu",
    )

    create: CreatorPluginsSettings = Field(
        default_factory=CreatorPluginsSettings,
        title="Creator Plugins",
    )

    publish: PublisherPluginsSettings = Field(
        default_factory=PublisherPluginsSettings,
        title="Publish Plugins",
    )

    load: LoaderPluginsSettings = Field(
        default_factory=LoaderPluginsSettings,
        title="Loader Plugins",
    )

    workfile_builder: WorkfileBuilderSettings = Field(
        default_factory=WorkfileBuilderSettings,
        title="Workfile Builder",
    )

    templated_workfile_build: TemplatedWorkfileBuildSettings = Field(
        default_factory=TemplatedWorkfileBuildSettings,
        title="Templated Workfile Build",
    )

    filters: list[PublishFiltersModel] = Field(
        default_factory=list
    )

    @validator("filters")
    def ensure_unique_names(cls, value):
        """Ensure name fields within the lists have unique names."""
        ensure_unique_names(value)
        return value


DEFAULT_VALUES = {
    "general": DEFAULT_GENERAL_SETTINGS,
    "imageio": DEFAULT_IMAGEIO_SETTINGS,
    "dirmap": DEFAULT_DIRMAP_SETTINGS,
    "scriptsmenu": DEFAULT_SCRIPTSMENU_SETTINGS,
    "gizmo": DEFAULT_GIZMO_SETTINGS,
    "create": DEFAULT_CREATE_SETTINGS,
    "publish": DEFAULT_PUBLISH_SETTINGS,
    "load": DEFAULT_LOAD_SETTINGS,
    "workfile_builder": DEFAULT_WORKFILE_BUILDER_SETTINGS,
    "templated_workfile_build": DEFAULT_TEMPLATED_WORKFILE_BUILD_SETTINGS
}
