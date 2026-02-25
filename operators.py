import bpy


class ISOMETRIC_OT_setup_scene(bpy.types.Operator):
    bl_idname = "isometric.setup_scene"
    bl_label = "Setup Scene"

    def execute(self, context):
        self.create_ground_plane()
        self.create_camera()
        self.configure_scale()
        self.configure_film()

    def create_ground_plane(self):
        # TODO create ground plane of specified size
        pass

    def create_camera(self):
        # TODO create camera with correct location and rotation
        pass

    def configure_scale(self):
        # TODO configure isometric scale
        pass

    def configure_film(self):
        # TODO configure film resolution
        pass


class ISOMETRIC_OT_render_2d_normals(bpy.types.Operator):
    bl_idname = "isometric.render_2d_normals"
    bl_label = "Render 2D Normals"

    def execute(self, context):
        self.render()

    def render(self):
        # TODO render scene but assign special material to all objects (temporarely)
        pass
