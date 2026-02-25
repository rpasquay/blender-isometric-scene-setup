import bpy


class IsometricSceneProperties(bpy.types.PropertyGroup):
    clear_scene: bpy.props.BoolProperty(  # type: ignore[valid-type]
        name="Clear Scene",
        description="Deletes all objects befor setting up the scene",
        default=False,
    )
    ground_plane_size: bpy.props.FloatProperty(  # type: ignore[valid-type]
        name="Side Length",
        description="Length of the sides of the quadratic ground plane.",
        default=2.0,
        min=1.0,
    )


def register():
    bpy.utils.register_class(IsometricSceneProperties)
    bpy.types.Scene.isometric_scene_properties = bpy.props.PointerProperty(
        type=IsometricSceneProperties
    )


def unregister():
    del bpy.types.Scene.isometric_scene_properties
    bpy.utils.unregister_class(IsometricSceneProperties)
