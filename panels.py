import bpy


class IsometricSetupPanel(bpy.types.Panel):
    bl_label = "Isometric Scene Setup"
    bl_category = "Isometric"
    bl_idname = "VIEW3D_PT_isometric"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        pass


class ISOMETRIC_PT_scene(bpy.types.Panel):
    bl_label = "Scene"
    bl_idname = "VIEW3D_PT_isometric_scene"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Isometric"
    bl_parent_id = "VIEW3D_PT_isometric"

    def draw(self, context):
        layout = self.layout
        properties = context.scene.isometric_scene_properties

        layout.prop(
            properties,
            "ground_plane_size",
        )
        layout.prop(properties, "image_width")
        layout.prop(properties, "image_height")

        layout.operator("isometric.setup_scene", text="Setup Scene", icon="PLAY")


class ISOMETRIC_PT_normals(bpy.types.Panel):
    bl_label = "Normals Material"
    bl_idname = "VIEW3D_PT_isometric_normals"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Isometric"
    bl_parent_id = "VIEW3D_PT_isometric"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        layout.operator("isometric.render_2d_normals", text="Render", icon="PLAY")
