from pydantic import Field

from ayon_server.settings import BaseSettingsModel

class CreateLookModel(BaseSettingsModel):
    enabled: bool = Field(title="Enabled")
    make_tx: bool = Field(title="Make tx files")
    defaults: list[str] = Field(default_factory=["Main"], title="Default Subsets")


class CreateRenderModel(BaseSettingsModel):
    enabled: bool = Field(title="Enabled")
    defaults: list[str] = Field(
        default_factory=["Main"],
        title="Default Subsets"
    )


class CreateUnrealStaticMeshModel(BaseSettingsModel):
    enabled: bool = Field(title="Enabled")
    defaults: list[str] = Field(
        default_factory=["", "_Main"],
        title="Default Subsets"
    )
    static_mesh_prefixes: str = Field("S", title="Static Mesh Prefix")
    collision_prefixes: list[str] = Field(
        default_factory=["UBX", "UCP", "USP", "UCX"],
        title="Collision Prefixes"
    )


class CreateUnrealSkeletalMeshModel(BaseSettingsModel):
    enabled: bool = Field(title="Enabled")
    defaults: list[str] = Field(default_factory=[],title="Default Subsets")
    joint_hints: str = Field("jnt_org", title="Joint root hint")


class CreateMultiverseLookModel(BaseSettingsModel):
    enabled: bool = Field(title="Enabled")
    publish_mip_map: bool = Field(title="publish_mip_map")


class CreateAnimationModel(BaseSettingsModel):
    enabled: bool = Field(title="Enabled")
    write_color_sets: bool = Field(title="Write Color Sets")
    write_face_sets: bool = Field(title="Write Face Sets")
    defaults: list[str] = Field(
        default_factory=["Main"],
        title="Default Subsets"
    )


class CreateModelModel(BaseSettingsModel):
    enabled: bool = Field(title="Enabled")
    write_color_sets: bool = Field(title="Write Color Sets")
    write_face_sets: bool = Field(title="Write Face Sets")
    defaults: list[str] = Field(
        default_factory=["Main", "Proxy", "Sculpt"],
        title="Default Subsets"
    )


class CreatePointCacheModel(BaseSettingsModel):
    enabled: bool = Field(title="Enabled")
    write_color_sets: bool = Field(title="Write Color Sets")
    write_face_sets: bool = Field(title="Write Face Sets")
    defaults: list[str] = Field(
        default_factory=["Main"],
        title="Default Subsets"
    )


class CreateMultiverseUsdModel(BaseSettingsModel):
    enabled: bool = Field(title="Enabled")
    defaults: list[str] = Field(
        default_factory=["Main"],
        title="Default Subsets"
    )


class CreateMultiverseUsdCompModel(BaseSettingsModel):
    enabled: bool = Field(title="Enabled")
    defaults: list[str] = Field(
        default_factory=["Main"],
        title="Default Subsets"
    )


class CreateMultiverseUsdOverModel(BaseSettingsModel):
    enabled: bool = Field(title="Enabled")
    defaults: list[str] = Field(
        default_factory=["Main"],
        title="Default Subsets"
    )


class CreateAssModel(BaseSettingsModel):
    enabled: bool = Field(title="Enabled")
    defaults: list[str] = Field(
        default_factory=["Main"],
        title="Default Subsets"
    )


class CreateAssemblyModel(BaseSettingsModel):
    enabled: bool = Field(title="Enabled")
    defaults: list[str] = Field(
        default_factory=["Main"],
        title="Default Subsets"
    )


class CreateCameraModel(BaseSettingsModel):
    enabled: bool = Field(title="Enabled")
    defaults: list[str] = Field(
        default_factory=["Main"],
        title="Default Subsets"
    )


class CreateLayoutModel(BaseSettingsModel):
    enabled: bool = Field(title="Enabled")
    defaults: list[str] = Field(
        default_factory=["Main"],
        title="Default Subsets"
    )


class CreateMayaSceneModel(BaseSettingsModel):
    enabled: bool = Field(title="Enabled")
    defaults: list[str] = Field(
        default_factory=["Main"],
        title="Default Subsets"
    )


class CreateRenderSetupModel(BaseSettingsModel):
    enabled: bool = Field(title="Enabled")
    defaults: list[str] = Field(
        default_factory=["Main"],
        title="Default Subsets"
    )


class CreateReviewModel(BaseSettingsModel):
    enabled: bool = Field(title="Enabled")
    defaults: list[str] = Field(
        default_factory=["Main"],
        title="Default Subsets"
    )


class CreateRigModel(BaseSettingsModel):
    enabled: bool = Field(title="Enabled")
    defaults: list[str] = Field(
        default_factory=["Main", "Sim", "Cloth"],
        title="Default Subsets"
    )


class CreateSetDressModel(BaseSettingsModel):
    enabled: bool = Field(title="Enabled")
    defaults: list[str] = Field(
        default_factory=["Main", "Anim"],
        title="Default Subsets"
    )


class CreateVrayProxyModel(BaseSettingsModel):
    enabled: bool = Field(title="Enabled")
    defaults: list[str] = Field(
        default_factory=["Main"],
        title="Default Subsets"
    )


class CreateVraySceneModel(BaseSettingsModel):
    enabled: bool = Field(title="Enabled")
    defaults: list[str] = Field(
        default_factory=["Main"],
        title="Default Subsets"
    )


class CreateYetiRigModel(BaseSettingsModel):
    enabled: bool = Field(title="Enabled")
    defaults: list[str] = Field(
        default_factory=["Main"],
        title="Default Subsets"
    )


class CreatorsModel(BaseSettingsModel):
    CreateLook: CreateLookModel = Field(
        default_factory=CreateLookModel,
        title="Create Look"
    )
    CreateRender: CreateRenderModel = Field(
        default_factory=CreateRenderModel,
        title="Create Render"
    )
    # "-" is not compatible in the new model
    CreateUnrealStaticMesh: CreateUnrealStaticMeshModel = Field(
        default_factory=CreateUnrealStaticMeshModel,
        title="Create Unreal_Static Mesh"
    )
    # "-" is not compatible in the new model
    CreateUnrealSkeletalMesh: CreateUnrealSkeletalMeshModel = Field(
        default_factory=CreateUnrealSkeletalMeshModel,
        title="Create Unreal_Skeletal Mesh"
    )
    CreateMultiverseLook: CreateMultiverseLookModel = Field(
        default_factory=CreateMultiverseLookModel,
        title="Create Multiverse Look"
    )
    CreateAnimation: CreateAnimationModel = Field(
        default_factory=CreateAnimationModel,
        title="Create Animation"
    )
    CreateModel: CreateModelModel = Field(
        default_factory=CreateModelModel,
        title="Create Model"
    )
    CreatePointCache: CreatePointCacheModel = Field(
        default_factory=CreatePointCacheModel,
        title="Create Point Cache"
    )
    CreateMultiverseUsd : CreateMultiverseUsdModel = Field(
        default_factory=CreateMultiverseUsdModel,
        title="Create Multiverse USD"
    )
    CreateMultiverseUsdComp: CreateMultiverseUsdCompModel = Field(
        default_factory=CreateMultiverseUsdCompModel,
        title="Create Multiverse USD Composition"
    )
    CreateMultiverseUsdOver: CreateMultiverseUsdOverModel = Field(
        default_factory=CreateMultiverseUsdOverModel,
        title="Create Multiverse USD Override"
    )
    CreateAss: CreateAssModel = Field(
        default_factory=CreateAssModel,
        title="Create Ass"
    )
    CreateAssembly: CreateAssemblyModel = Field(
        default_factory=CreateAssemblyModel,
        title="Create Assembly"
    )
    CreateCamera: CreateCameraModel = Field(
        default_factory=CreateCameraModel,
        title="Create Camera"
    )
    CreateLayout: CreateLayoutModel = Field(
        default_factory=CreateLayoutModel,
        title="Create Layout"
    )
    CreateMayaScene: CreateMayaSceneModel = Field(
        default_factory=CreateMayaSceneModel,
        title="Create Maya Scene"
    )
    CreateRenderSetup: CreateRenderSetupModel = Field(
        default_factory=CreateRenderSetupModel,
        title="Create Render Setup"
    )
    CreateReview: CreateReviewModel = Field(
        default_factory=CreateReviewModel,
        title="Create Review"
    )
    CreateRig: CreateRigModel = Field(
        default_factory=CreateRigModel,
        title="Create Rig"
    )
    CreateSetDress: CreateSetDressModel = Field(
        default_factory=CreateSetDressModel,
        title="Create Set Dress"
    )
    CreateVrayProxy: CreateVrayProxyModel = Field(
        default_factory=CreateVrayProxyModel,
        title="Create VRay Proxy"
    )
    CreateVrayScene: CreateVraySceneModel = Field(
        default_factory=CreateVraySceneModel,
        title="Create VRay Scene"
    )
    CreateYetiRig: CreateYetiRigModel = Field(
        default_factory=CreateYetiRigModel,
        title="Create Yeti Rig"
    )


DEFAULT_CREATORS_SETTINGS = {
        "CreateLook": {
            "enabled": True,
            "make_tx": True,
            "defaults": [
                "Main"
            ]
        },
         "CreateRender": {
            "enabled": True,
            "defaults": [
                "Main"
            ]
        },
        "CreateUnrealStaticMesh": {
            "enabled": True,
            "defaults": [
                "",
                "_Main"
            ],
            "static_mesh_prefix": "S",
            "collision_prefixes": [
                "UBX",
                "UCP",
                "USP",
                "UCX"
            ]
        },
        "CreateUnrealSkeletalMesh": {
            "enabled": True,
            "defaults": [],
            "joint_hints": "jnt_org"
        },
        "CreateMultiverseLook": {
            "enabled": True,
            "publish_mip_map": True
        },
        "CreateAnimation": {
            "enabled": True,
            "write_color_sets": False,
            "write_face_sets": False,
            "defaults": [
                "Main"
            ]
        },
        "CreateModel": {
            "enabled": True,
            "write_color_sets": False,
            "write_face_sets": False,
            "defaults": [
                "Main",
                "Proxy",
                "Sculpt"
            ]
        },
        "CreatePointCache": {
            "enabled": True,
            "write_color_sets": False,
            "write_face_sets": False,
            "defaults": [
                "Main"
            ]
        },
        "CreateMultiverseUsd": {
            "enabled": True,
            "defaults": [
                "Main"
            ]
        },
        "CreateMultiverseUsdComp": {
            "enabled": True,
            "defaults": [
                "Main"
            ]
        },
        "CreateMultiverseUsdOver": {
            "enabled": True,
            "defaults": [
                "Main"
            ]
        },
        "CreateAss": {
            "enabled": True,
            "defaults": [
                "Main"
            ]
        },
        "CreateAssembly": {
            "enabled": True,
            "defaults": [
                "Main"
            ]
        },
        "CreateCamera": {
            "enabled": True,
            "defaults": [
                "Main"
            ]
        },
        "CreateLayout": {
            "enabled": True,
            "defaults": [
                "Main"
            ]
        },
        "CreateMayaScene": {
            "enabled": True,
            "defaults": [
                "Main"
            ]
        },
        "CreateRenderSetup": {
            "enabled": True,
            "defaults": [
                "Main"
            ]
        },
        "CreateReview": {
            "enabled": True,
            "defaults": [
                "Main"
            ]
        },
        "CreateRig": {
            "enabled": True,
            "defaults": [
                "Main",
                "Sim",
                "Cloth"
            ]
        },
        "CreateSetDress": {
            "enabled": True,
            "defaults": [
                "Main",
                "Anim"
            ]
        },
        "CreateVrayProxy": {
            "enabled": True,
            "defaults": [
                "Main"
            ]
        },
        "CreateVrayScene": {
            "enabled": True,
            "defaults": [
                "Main"
            ]
        },
        "CreateYetiRig": {
            "enabled": True,
            "defaults": [
                "Main"
            ]
        }
    }
