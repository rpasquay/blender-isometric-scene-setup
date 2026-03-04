bl_info = {
    "name": "Isometric Scene Setup",
    "author": "Rafael Pasquay",
    "description": "",
    "blender": (2, 80, 0),
    "version": (0, 0, 1),
    "location": "",
    "warning": "",
    "category": "Generic",
}

import bpy

from .properties import IsometricSceneProperties
from .operators import ISOMETRIC_OT_setup_scene, ISOMETRIC_OT_render_2d_normals
from .panels import IsometricSetupPanel, ISOMETRIC_PT_scene, ISOMETRIC_PT_normals
from . import properties

classes = (
    IsometricSceneProperties,
    ISOMETRIC_OT_setup_scene,
    ISOMETRIC_OT_render_2d_normals,
    IsometricSetupPanel,
    ISOMETRIC_PT_scene,
    ISOMETRIC_PT_normals,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    properties.register()


def unregister():
    properties.unregister()
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
