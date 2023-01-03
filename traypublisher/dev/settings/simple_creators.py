from pydantic import Field

from ayon_server.settings import BaseSettingsModel


class SimpleCreatorPlugin(BaseSettingsModel):
    _layout = "expanded"
    family: str = Field('',
                        title="Family")

    identifier: str = Field('',              # TODO add placeholder
                            title="Identifier")

    label: str = Field('',
                       title="Label")

    icon: str = Field('',
                      title="Icon")

    default_variants: list[str] = Field(default_factory=list,
                                        title="Default Variants")

    description: str = Field(
        '',
        title="Description",
        widget="textarea"
    )

    detailed_description: str = Field(
        '',
        title="Detailed Description",
        widget="textarea"
    )

    allow_multiple_items: bool = Field(
        False,
        title="Allow multiple items"
    )

    extensions: list[str] = Field(
        default_factory=list,
        title="Extensions"
    )

