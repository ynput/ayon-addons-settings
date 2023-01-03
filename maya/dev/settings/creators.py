"""Providing models and values for Maya Creators.

Note: This needs to be changed when switching to the new publisher in Maya.
"""
from pydantic import Field

from ayon_server.settings import BaseSettingsModel


def class_ref(cls):
    placeholder = "@classref@"
    for k, v in vars(cls).items():
        if v == placeholder:
            setattr(cls, k, cls)
    return cls


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
        "CreateVRayScene": {
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


@class_ref
class BaseMayaCreatorModel(BaseSettingsModel):
    cls = "@classref@"
    enabled: bool = Field(title="Enabled")
    defaults: str = Field(enum_resolver=DEFAULT_CREATORS_SETTINGS[cls.__name__]["defaults"])


@class_ref
class CreateModelModel(BaseMayaCreatorModel):
    write_color_sets: bool = Field(title="Write Color Sets")


class CreatorsModel(BaseSettingsModel):
    create_model: CreateModelModel = Field(default_factory=CreateModelModel)
