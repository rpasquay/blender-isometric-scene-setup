import bpy


class IsometricSceneProperties(bpy.types.PropertyGroup):
    clear_scene: bpy.props.BoolProperty(  # type: ignore[valid-type]
        name="Clear Scene",
        description="Deletes all objects befor setting up the scene",
        default=False,
    )
    ground_plane_size: bpy.props.FloatProperty(  # type: ignore[valid-type]
        name="Ground Plane Side Length",
        description="Length of the sides of the quadratic ground plane.",
        default=2.0,
        min=1.0,
        subtype="DISTANCE",
    )
    image_width: bpy.props.IntProperty(  # type: ignore[valid-type]
        name="Image Width",
        description="Desired isometric tile widt",
        default=512,
        min=1,
        subtype="PIXEL",
    )
    image_height: bpy.props.IntProperty(  # type: ignore[valid-type]
        name="Image Height",
        description="Desired isometric tile height",
        default=512,
        min=1,
        subtype="PIXEL",
    )


def register():
    bpy.types.Scene.isometric_scene_properties = bpy.props.PointerProperty(
        type=IsometricSceneProperties
    )


def unregister():
    del bpy.types.Scene.isometric_scene_properties
