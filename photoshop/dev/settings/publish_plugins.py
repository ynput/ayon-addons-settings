from pydantic import Field

from ayon_server.settings import BaseSettingsModel


create_flatten_image_enum = [
    {"value": "flatten_with_images", "label": "Flatten with images"},
    {"value": "flatten_only", "label": "Flatten only"},
    {"value": "no", "label": "No"},
]


color_code_enum = [
    {"value": "red", "label": "Red"},
    {"value": "orange", "label": "Orange"},
    {"value": "yellowColor", "label": "Yellow"},
    {"value": "grain", "label": "Green"},
    {"value": "blue", "label": "Blue"},
    {"value": "violet", "label": "Violet"},
    {"value": "gray", "label": "Gray"},
]


class ColorCodeMappings(BaseSettingsModel):
    color_code: list[str] = Field(
        title="Color codes for layers",
        default_factory=list,
        enum_resolver=lambda: color_code_enum,
    )

    layer_name_regex: list[str] = Field(
        "",
        title="Layer name regex"
    )

    family: str = Field(
        "",
        title="Resulting family"
    )

    subset_template_name: str = Field(
        "",
        title="Subset template name"
    )


class ExtractedOptions(BaseSettingsModel):
    tags: list[str] = Field(
        title="Tags",
        default_factory=list
    )


class CollectColorCodedInstancesPlugin(BaseSettingsModel):
    """Set color for publishable layers, set its resulting family and template
    for subset name. \n Can create flatten image from published instances.
    (Applicable only for remote publishing!)"""
    create_flatten_image: str = Field(
        "",
        title="Create flatten image",
        enum_resolver=lambda: create_flatten_image_enum,
    )

    flatten_subset_template: str = Field(
        "",
        title="Subset template for flatten image"
    )

    color_code_mapping: list[ColorCodeMappings] = Field(
        title="Color code mappings",
        default_factory=ColorCodeMappings,
    )


class CollectInstancesPlugin(BaseSettingsModel):
    """Name for flatten image created if no image instance present"""
    flatten_subset_template: str = Field(
        "",
        title="Subset template for flatten image",
        description="Name for flatten image created if no image " 
                    "instance present"

    )


class CollectReviewPlugin(BaseSettingsModel):
    """Should review subset be created"""
    active: bool = Field(True, title="Active")


class CollectVersionPlugin(BaseSettingsModel):
    """Synchronize version for image and review instances by workfile version"""  # noqa
    enabled: bool = Field(True, title="Enabled")


class ValidateContainersPlugin(BaseSettingsModel):
    """Check that workfile contains latest version of loaded items"""  # noqa
    _isGroup = True
    enabled: bool = True
    optional: bool = Field(False, title="Optional")
    active: bool = Field(True, title="Active")


class ValidateNamingPlugin(BaseSettingsModel):
    """Validate naming of subsets and layers"""  # noqa
    invalid_chars: str = Field(
        '',
        title="Regex pattern of invalid characters"
    )

    replace_char: str = Field(
        '',
        title="Replacement character"
    )


class ExtractImagePlugin(BaseSettingsModel):
    """Currently only jpg and png are supported"""
    formats: list[str] = Field(
        title="Extract Formats",
        default_factory=list,
    )


class ExtractReviewPlugin(BaseSettingsModel):
    make_image_sequence: bool = Field(
        False,
        title="Make an image sequence instead of flatten image"
    )

    max_downscale_size: int = Field(
        8192,
        title="Maximum size of sources for review",
        description="FFMpeg can only handle limited resolution for creation of review and/or thumbnail",  # noqa
        gt=300,  # greater than
        le=16384,  # less or equal
    )

    jpg_options: ExtractedOptions = Field(
        title="Extracted jpg Options",
        default_factory=ExtractedOptions
    )

    mov_options: ExtractedOptions = Field(
        title="Extracted mov Options",
        default_factory=ExtractedOptions
    )


class PhotoshopPublishPlugins(BaseSettingsModel):
    CollectColorCodedInstances: CollectColorCodedInstancesPlugin = Field(
        title="Collect Color Coded Instances",
        default_factory=CollectColorCodedInstancesPlugin,
    )

    CollectInstances: CollectInstancesPlugin = Field(
        title="Collect Instances",
        default_factory=CollectInstancesPlugin,
    )

    CollectReview: CollectReviewPlugin = Field(
        title="Collect Review",
        default_factory=CollectReviewPlugin,
    )

    CollectVersion: CollectVersionPlugin = Field(
        title="Create Image",
        default_factory=CollectVersionPlugin,
    )

    ValidateContainers: ValidateContainersPlugin = Field(
        title="Validate Containers",
        default_factory=ValidateContainersPlugin,
    )

    ValidateNaming: ValidateNamingPlugin = Field(
        title="Validate naming of subsets and layers",
        default_factory=ValidateNamingPlugin,
    )

    ExtractImage: ExtractImagePlugin = Field(
        title="Extract Image",
        default_factory=ExtractImagePlugin,
    )

    ExtractReview: ExtractReviewPlugin = Field(
        title="Extract Review",
        default_factory=ExtractReviewPlugin,
    )


