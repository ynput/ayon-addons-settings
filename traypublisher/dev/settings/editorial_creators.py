from pydantic import Field

from ayon_server.settings import BaseSettingsModel


class ClipNameTokenizerItem(BaseSettingsModel):
    _layout = "expanded"
    # TODO was 'dict-modifiable', is list of dicts now, must be fixed in code
    name: str = Field('#TODO', title="Tokenizer name")
    regex: str = Field('', title="Tokenizer regex")


task_types_enum = [
    {"label": "Generic", "value": "Generic"},
    {"label": "Art", "value": "Art"},
    {"label": "Modeling", "value": "Modeling"},
    {"label": "Texture", "value": "Texture"},
    {"label": "Lookdev", "value": "Lookdev"},
    {"label": "Rigging", "value": "Rigging"},
    {"label": "Edit", "value": "Edit"},
    {"label": "Layout", "value": "Layout"},
    {"label": "Setdress", "value": "Setdress"},
    {"label": "Animation", "value": "Animation"},
    {"label": "FX", "value": "FX"},
    {"label": "Lighting", "value": "Lighting"},
    {"label": "Paint", "value": "Paint"},
    {"label": "Compositing", "value": "Compositing"},
    {"label": "Roto", "value": "Roto"},
    {"label": "Matchmove", "value": "Matchmove"}
]


class ShotAddTasksItem(BaseSettingsModel):
    _layout = "expanded"
    # TODO was 'dict-modifiable', is list of dicts now, must be fixed in code
    name: str = Field('', title="Key")
    task_type: list[str] = Field(
                                title="Task type",
                                default_factory=list,
                                enum_resolver=lambda: task_types_enum)


class ShotRenameSubmodel(BaseSettingsModel):
    enabled: bool = True

    shot_rename_template: str = Field(
        '',
        title="Shot rename template"
    )


parent_type_enum = [
    {"value": "Project", "label": "Project"},
    {"value": "Folder", "label": "Folder"},
    {"value": "Episode", "label": "Episode"},
    {"value": "Sequence", "label": "Sequence"},
]


class TokenToParentConvertorItem(BaseSettingsModel):
    # TODO - was 'type' must be renamed in code to `parent_type`
    parent_type: str = Field(
        "Project",
        enum_resolver=lambda: parent_type_enum
    )
    name: str = Field(
        '',
        title="Parent token name",
        description="Unique name used in `Parent path template`"
    )
    value: str = Field(
        '',
        title="Parent token value",
        description="Template where any text, Anatomy keys and Tokens could be used"  # noqa
    )


class ShotHierchySubmodel(BaseSettingsModel):
    enabled: bool = True

    parents_path: str = Field(
        '',
        title="Parents path template",
        description="Using keys from \"Token to parent convertor\" or tokens directly"  # noqa
    )

    parents: list[TokenToParentConvertorItem] = Field(
        default_factory=TokenToParentConvertorItem,
        title="Token to parent convertor"
    )


output_file_type = [
    {"value": ".mp4", "label": "MP4"},
    {"value": ".mov", "label": "MOV"},
    {"value": ".wav", "label": "WAV"}
]


class FamilyPresetItem(BaseSettingsModel):
    family: str = Field(
        '',
        title="Family"
    )

    # TODO ? in v3 shows up grayed out  'inherited'??
    variant: str = Field(
        '',
        title='Variant'
    )

    review: bool = Field(
        False,
        title="Review"
    )

    output_file_type: str = Field(
        ".mp4",
        enum_resolver=lambda: output_file_type
    )


class ShotSubsetCreator(BaseSettingsModel):
    # TODO collapsible-wrap is not implemented, this one introduces additional
    # level with key >> breaks defaults template >> template in main modified

    family_presets: list[FamilyPresetItem] = Field(
        default_factory=FamilyPresetItem
    )


class ShotMetadataCreator(BaseSettingsModel):
    # TODO collapsible-wrap is not implemented, this one introduces additional
    # level with key >> breaks defaults template >> template in main modified

    clip_name_tokenizer: list[ClipNameTokenizerItem] = Field(
        default_factory=ClipNameTokenizerItem,
        description="Using Regex expression to create tokens. \nThose can be used later in \"Shot rename\" creator \nor \"Shot hierarchy\". \n\nTokens should be decorated with \"_\" on each side",  # noqa
    )

    shot_rename: ShotRenameSubmodel = Field(
        title="Shot Rename",
        default_factory=ShotRenameSubmodel
    )

    shot_hierarchy: ShotHierchySubmodel = Field(
        title="Shot Hierarchy",
        default_factory=ShotHierchySubmodel
    )

    shot_add_tasks: list[ShotAddTasksItem] = Field(
        title="Add tasks to shot",
        default_factory=ShotAddTasksItem
    )


class EditorialSimpleCreatorPlugin(BaseSettingsModel):
    default_variants: list[str] = Field(default_factory=list,
                                        title="Default Variants")

    shot_metadata_creator: ShotMetadataCreator = Field(
        title="Shot metadata creator",
        default_factory=ShotMetadataCreator,
    )

    shot_subset_creator: ShotSubsetCreator = Field(
        title="Shot's subset creator",
        default_factory=ShotSubsetCreator
    )


class TraypublisherEditorialCreatorPlugins(BaseSettingsModel):
    editorial_simple: EditorialSimpleCreatorPlugin = Field(
        title="Editorial simple creator",
        default_factory=EditorialSimpleCreatorPlugin,
    )
