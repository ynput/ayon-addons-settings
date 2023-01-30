from pydantic import validator, Field
from ayon_server.settings import (
    BaseSettingsModel,
    ensure_unique_names,
    task_types_enum
)
from .common import KnobModel, validate_json_dict


def nuke_render_families_enum():
    """Return all nuke render families available in creators."""
    return [
        {"value": "render", "label": "Render"},
        {"value": "prerender", "label": "Prerender"},
        {"value": "image", "label": "Image"}
    ]


def nuke_families_enum():
    """Return all nuke families available in creators."""
    return [
        {"value": "nukenodes", "label": "Nukenodes"},
        {"value": "model", "label": "Model"},
        {"value": "camera", "label": "Camera"},
        {"value": "gizmo", "label": "Gizmo"},
        {"value": "source", "label": "Source"}
    ] + nuke_render_families_enum()


class NodeModel(BaseSettingsModel):
    # TODO: missing in host api
    name: str = Field(
        title="Node name"
    )
    # TODO: `nodeclass` rename to `nuke_node_class`
    nodeclass: str = Field(
        "",
        title="Node class"
    )
    dependent: str = Field(
        "",
        title="Incoming dependency"
    )
    """# TODO: Changes in host api:
    - Need complete rework of knob types in nuke integration.
    - We could not support v3 style of settings.
    """
    knobs: list[KnobModel] = Field(
        title="Knobs",
    )

    @validator("knobs")
    def ensure_unique_names(cls, value):
        """Ensure name fields within the lists have unique names."""
        ensure_unique_names(value)
        return value


class CollectInstanceDataModel(BaseSettingsModel):
    sync_workfile_version_on_families: list[str] = Field(
        default_factory=list,
        enum_resolver=nuke_families_enum,
        title="Sync workfile versions for familes"
    )


class ValidateCorrectAssetNameModel(BaseSettingsModel):
    enabled: bool = Field(title="Enabled")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ValidateContainersModel(BaseSettingsModel):
    enabled: bool = Field(title="Enabled")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ValidateKnobsModel(BaseSettingsModel):
    enabled: bool = Field(title="Enabled")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")
    knobs: str = Field(
        "{}",
        title="Knobs",
        widget="textarea",
    )

    @validator("knobs")
    def validate_json(cls, value):
        return validate_json_dict(value)


class ValidateGizmoModel(BaseSettingsModel):
    enabled: bool = Field(title="Enabled")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ValidateOutputResolutionModel(BaseSettingsModel):
    enabled: bool = Field(title="Enabled")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ValidateScriptModel(BaseSettingsModel):
    enabled: bool = Field(title="Enabled")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ExtractThumbnailModel(BaseSettingsModel):
    enabled: bool = Field(title="Enabled")
    use_rendered: bool = Field(title="Use rendered images")
    bake_viewer_process: bool = Field(title="Bake view process")
    bake_viewer_input_process: bool = Field(title="Bake viewer input process")
    """# TODO: needs to rewrite from v3 to ayon
    - `nodes` in v3 was dict but now `prenodes` is list of dict
    - also later `nodes` should be `prenodes`
    """

    nodes: list[NodeModel] = Field(
        title="Preceding nodes"
    )


class ExtractReviewDataModel(BaseSettingsModel):
    enabled: bool = Field(title="Enabled")


class ExtractReviewDataLutModel(BaseSettingsModel):
    enabled: bool = Field(title="Enabled")


class BakeingStreamFilterModel(BaseSettingsModel):
    task_types: list[str] = Field(
        default_factory=list,
        title="Task types",
        enum_resolver=task_types_enum
    )
    families: list[str] = Field(
        default_factory=list,
        enum_resolver=nuke_render_families_enum,
        title="Sync workfile versions for familes"
    )
    subsets: list[str] = Field(
        default_factory=list, title="Subsets")

class BakingStreamModel(BaseSettingsModel):
    name: str = Field(title="Output name")
    filter: BakeingStreamFilterModel = Field(
        title="Filter", default_factory=BakeingStreamFilterModel)
    extension: str = Field(title="File extension")
    read_raw: bool = Field(title="Read raw switch")
    viewer_process_override: str = Field(title="Viewer process override")
    bake_viewer_process: bool = Field(title="Bake view process")
    bake_viewer_input_process: bool = Field(title="Bake viewer input process")
    reformat_node_add: bool = Field(title="Add reformat node")
    reformat_node_config: list[KnobModel] = Field(
        title="Reformat node properties")
    add_custom_tags: list[str] = Field(
        title="Custom tags", default_factory=list)

class ExtractReviewDataMovModel(BaseSettingsModel):
    enabled: bool = Field(title="Enabled")
    viewer_lut_raw: bool = Field(title="Viewer lut raw")
    """# TODO: v3 api dict now list"""
    outputs: list[BakingStreamModel] = Field(
        title="Baking streams"
    )


class FSubmissionNoteModel(BaseSettingsModel):
    enabled: bool = Field(title="enabled")
    template: str = Field(title="Template")


class FSubmistingForModel(BaseSettingsModel):
    enabled: bool = Field(title="enabled")
    template: str = Field(title="Template")


class FVFXScopeOfWorkModel(BaseSettingsModel):
    enabled: bool = Field(title="enabled")
    template: str = Field(title="Template")


class ExctractSlateFrameParamModel(BaseSettingsModel):
    f_submission_note: FSubmissionNoteModel = Field(
        title="f_submission_note",
        default_factory=FSubmissionNoteModel
    )
    f_submitting_for: FSubmistingForModel = Field(
        title="f_submitting_for",
        default_factory=FSubmistingForModel
    )
    f_vfx_scope_of_work: FVFXScopeOfWorkModel = Field(
        title="f_vfx_scope_of_work",
        default_factory=FVFXScopeOfWorkModel
    )


class ExtractSlateFrameModel(BaseSettingsModel):
    viewer_lut_raw: bool = Field(title="Viewer lut raw")
    """# TODO: v3 api different model:
    - not possible to replicate v3 model:
        {"name": [bool, str]}
    - not it is:
        {"name": {"enabled": bool, "template": str}}
    """
    key_value_mapping: ExctractSlateFrameParamModel = Field(
        title="Key value mapping",
        default_factory=ExctractSlateFrameParamModel
    )


class IncrementScriptVersionModel(BaseSettingsModel):
    enabled: bool = Field(title="Enabled")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class PublishPuginsModel(BaseSettingsModel):
    CollectInstanceData: CollectInstanceDataModel = Field(
        title="Collect Instance Version",
        default_factory=CollectInstanceDataModel,
        section="Collectors"
    )
    ValidateCorrectAssetName: ValidateCorrectAssetNameModel = Field(
        title="Validate Correct Asset Name",
        default_factory=ValidateCorrectAssetNameModel,
        section="Validators"
    )
    ValidateContainers: ValidateContainersModel = Field(
        title="Validate Containers",
        default_factory=ValidateContainersModel
    )
    ValidateKnobs: ValidateKnobsModel = Field(
        title="Validate Knobs",
        default_factory=ValidateKnobsModel
    )
    ValidateOutputResolution: ValidateOutputResolutionModel = Field(
        title="Validate Output Resolution",
        default_factory=ValidateOutputResolutionModel
    )
    ValidateGizmo: ValidateGizmoModel = Field(
        title="Validate Gizmo",
        default_factory=ValidateGizmoModel
    )
    ValidateScript: ValidateScriptModel = Field(
        title="Validate Script",
        default_factory=ValidateScriptModel
    )
    ExtractThumbnail: ExtractThumbnailModel = Field(
        title="Extract Thumbnail",
        default_factory=ExtractThumbnailModel,
        section="Extractors"
    )
    ExtractReviewData: ExtractReviewDataModel = Field(
        title="Extract Review Data",
        default_factory=ExtractReviewDataModel
    )
    ExtractReviewDataLut: ExtractReviewDataLutModel = Field(
        title="Extract Review Data Lut",
        default_factory=ExtractReviewDataLutModel
    )
    ExtractReviewDataMov: ExtractReviewDataMovModel = Field(
        title="Extract Review Data Mov",
        default_factory=ExtractReviewDataMovModel
    )
    ExtractSlateFrame: ExtractSlateFrameModel = Field(
        title="Extract Slate Frame",
        default_factory=ExtractSlateFrameModel
    )
    # TODO: plugin should be renamed - `workfile` not `script`
    IncrementScriptVersion: IncrementScriptVersionModel = Field(
        title="Increment Workfile Version",
        default_factory=IncrementScriptVersionModel,
        section="Integrators"
    )


DEFAULT_PUBLISH_PLUGIN_SETTINGS = {
    "CollectInstanceData": {
        "sync_workfile_version_on_families": [
            "nukenodes",
            "camera",
            "gizmo",
            "source",
            "render",
            "write"
        ]
    },
    "ValidateCorrectAssetName": {
        "enabled": True,
        "optional": True,
        "active": True
    },
    "ValidateContainers": {
        "enabled": True,
        "optional": True,
        "active": True
    },
    "ValidateKnobs": {
        "enabled": False,
        "optional": True,
        "active": True,
        "knobs": "\n".join([
            '{',
            '    "render": {',
            '        "review": true',
            '    }',
            '}'
        ])
    },
    "ValidateOutputResolution": {
        "enabled": True,
        "optional": True,
        "active": True
    },
    "ValidateGizmo": {
        "enabled": True,
        "optional": True,
        "active": True
    },
    "ValidateScript": {
        "enabled": True,
        "optional": True,
        "active": True
    },
    "ExtractThumbnail": {
        "enabled": True,
        "use_rendered": True,
        "bake_viewer_process": True,
        "bake_viewer_input_process": True,
        "nodes": [
            {
                "name": "Reformat01",
                "nodeclass": "Reformat",
                "dependency": "",
                "knobs": [
                    {
                        "type": "text",
                        "name": "type",
                        "text": "to format"
                    },
                    {
                        "type": "text",
                        "name": "format",
                        "text": "HD_1080"
                    },
                    {
                        "type": "text",
                        "name": "filter",
                        "text": "Lanczos6"
                    },
                    {
                        "type": "boolean",
                        "name": "black_outside",
                        "boolean": True
                    },
                    {
                        "type": "boolean",
                        "name": "pbb",
                        "boolean": False
                    }
                ]
            }
        ]

    },
    "ExtractReviewData": {
        "enabled": False
    },
    "ExtractReviewDataLut": {
        "enabled": False
    },
    "ExtractReviewDataMov": {
        "enabled": True,
        "viewer_lut_raw": False,
        "outputs": [
            {
                "name": "baking",
                "filter": {
                    "task_types": [],
                    "families": [],
                    "subsets": []
                },
                "read_raw": False,
                "viewer_process_override": "",
                "bake_viewer_process": True,
                "bake_viewer_input_process": True,
                "reformat_node_add": False,
                "reformat_node_config": [
                    {
                        "type": "text",
                        "name": "type",
                        "text": "to format"
                    },
                    {
                        "type": "text",
                        "name": "format",
                        "text": "HD_1080"
                    },
                    {
                        "type": "text",
                        "name": "filter",
                        "text": "Lanczos6"
                    },
                    {
                        "type": "boolean",
                        "name": "black_outside",
                        "boolean": True
                    },
                    {
                        "type": "boolean",
                        "name": "pbb",
                        "boolean": False
                    }
                ],
                "extension": "mov",
                "add_custom_tags": []
            }
        ]
    },
    "ExtractSlateFrame": {
        "viewer_lut_raw": False,
        "key_value_mapping": {
            "f_submission_note": {
                "enabled": True,
                "template": "{comment}"
            },
            "f_submitting_for": {
                "enabled": True,
                "template": "{intent[value]}"
            },
            "f_vfx_scope_of_work": {
                "enabled": False,
                "template": ""
            }
        }
    },
    "IncrementScriptVersion": {
        "enabled": True,
        "optional": True,
        "active": True
    }
}
