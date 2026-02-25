import bpy


class IsometricSetupPanel(bpy.types.Panel):
    bl_label = "Isometric Scene Setup"
    bl_category = "Isometric"
    bl_idname = "VIEW3D_PT_isometric"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):

        layout = self.layout

        layout.label(text="Scene Setup")
        layout.prop(context.scene.isometric_scene_properties, "clear_scene")
        layout.prop(context.scene.isometric_scene_properties, "ground_plane_size")


def register():
    bpy.utils.register_class(IsometricSetupPanel)


def unregister():
    bpy.utils.unregister_class(IsometricSetupPanel)
