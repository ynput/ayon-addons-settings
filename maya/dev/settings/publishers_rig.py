from pydantic import Field

from ayon_server.settings import BaseSettingsModel

class ValidateRigContentsModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateRigContents")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ValidateRigJointsHiddenModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateRigJointsHidden")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ValidateRigControllersModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateRigControllers")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ValidateAnimationContentModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateAnimationContent")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ValidateOutRelatedNodeIdsModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateOutRelatedNodeIds")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ValidateRigControllersArnoldAttributesModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateRigControllersArnoldAttributes")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ValidateSkeletalMeshHierarchyModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateSkeletalMeshHierarchy")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ValidateSkinclusterDeformerSetModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateSkinclusterDeformerSet")
    optional: bool = Field(title="Optional")
    active: bool = Field(title="Active")


class ValidateRigOutSetNodeIdsModel(BaseSettingsModel):
    enabled: bool = Field(title="ValidateSkinclusterDeformerSet")
    optional: bool = Field(title="Optional")
    allow_history_only: bool = Field(title="Allow history only")


class RigPublishSetting(BaseSettingsModel):
    ValidateRigContents: ValidateRigContentsModel = Field(
        default_factory=ValidateRigContentsModel,
        title="Validate Rig Contents"
    )
    ValidateRigJointsHidden: ValidateRigJointsHiddenModel = Field(
        default_factory=ValidateRigJointsHiddenModel,
        title="Validate Rig Joints Hidden"
    )
    ValidateRigControllers: ValidateRigControllersModel = Field(
        default_factory=ValidateRigControllersModel,
        title="Validate Rig Controllers"
    )
    ValidateAnimationContent: ValidateAnimationContentModel = Field(
        default_factory=ValidateAnimationContentModel,
        title="Validate Animation Content"
    )
    ValidateOutRelatedNodeIds: ValidateOutRelatedNodeIdsModel = Field(
        default_factory=ValidateOutRelatedNodeIdsModel,
        title="Validate Animation Out Set Related Node Ids"
    )
    ValidateRigControllersArnoldAttributes: ValidateRigControllersArnoldAttributesModel = Field(
        default_factory=ValidateRigControllersArnoldAttributesModel,
        title="Validate Rig Controllers (Arnold Attributes)"
    )
    ValidateSkeletalMeshHierarchy: ValidateSkeletalMeshHierarchyModel = Field(
        default_factory=ValidateSkeletalMeshHierarchyModel,
        title="Validate Skeletal Mesh Top Node"
    )
    ValidateSkinclusterDeformerSet: ValidateSkinclusterDeformerSetModel = Field(
        default_factory=ValidateSkinclusterDeformerSetModel,
        title="Validate Skincluster Deformer Relationships"
    )
    ValidateRigOutSetNodeIds: ValidateRigOutSetNodeIdsModel = Field(
        default_factory=ValidateRigOutSetNodeIdsModel,
        title="Validate Rig Out Set Node Ids"
    )


DEFAULT_RIG_PUBLISH_SETTING = {
    "ValidateRigContents": {
        "enabled": False,
        "optional": True,
        "active": True
    },
    "ValidateRigJointsHidden": {
        "enabled": False,
        "optional": True,
        "active": True
    },
    "ValidateRigControllers": {
        "enabled": False,
        "optional": True,
        "active": True
    },
    "ValidateAnimationContent": {
        "enabled": True,
        "optional": False,
        "active": True
    },
    "ValidateOutRelatedNodeIds": {
        "enabled": True,
        "optional": False,
        "active": True
    },
    "ValidateRigControllersArnoldAttributes": {
        "enabled": True,
        "optional": False,
        "active": True
    },
    "ValidateSkeletalMeshHierarchy": {
        "enabled": True,
        "optional": False,
        "active": True
    },
    "ValidateSkinclusterDeformerSet": {
        "enabled": True,
        "optional": False,
        "active": True
    },
    "ValidateRigOutSetNodeIds": {
        "enabled": True,
        "optional": False,
        "allow_history_only": False
    },
}