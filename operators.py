import bpy
import math
from dataclasses import dataclass

CAMERA_ROTATION_X = math.radians(60)
CAMERA_ROTATION_Y = 0
CAMERA_ROTATION_Z = math.radians(45)
CAMERA_NAME = "IsometricCamera"
CAMERA_TYPE = "ORTHO"


@dataclass(frozen=True)
class SceneConfig:
    image_width: int
    image_height: int
    ground_plane_size: float


@dataclass(frozen=True)
class CameraConfig:
    location_x: float
    location_y: float
    location_z: float
    scale_factor: float


class ISOMETRIC_OT_setup_scene(bpy.types.Operator):
    bl_idname = "isometric.setup_scene"
    bl_label = "Setup Scene"

    def execute(self, context):
        config = self._get_scene_config(context)
        self._create_ground_plane(config.ground_plane_size)
        camera_config = self._get_camera_config(
            config.image_width, config.image_height, config.ground_plane_size
        )
        self._create_camera(context, camera_config)
        self._configure_film(context, config.image_width, config.image_height)
        return {"FINISHED"}

    def _create_ground_plane(self, ground_plane_size):
        bpy.ops.mesh.primitive_plane_add(
            size=ground_plane_size,
            enter_editmode=False,
            align="WORLD",
            location=(0, 0, 0),
            scale=(1, 1, 1),
        )

    def _create_camera(self, context, config: CameraConfig):
        camera_data = bpy.data.cameras.new(name=CAMERA_NAME)
        camera_data.type = CAMERA_TYPE
        camera_data.ortho_scale = config.scale_factor

        camera_object = bpy.data.objects.new(name=CAMERA_NAME, object_data=camera_data)
        camera_object.location = (
            config.location_x,
            config.location_y,
            config.location_z,
        )
        camera_object.rotation_euler = (
            CAMERA_ROTATION_X,
            CAMERA_ROTATION_Y,
            CAMERA_ROTATION_Z,
        )
        context.collection.objects.link(camera_object)
        context.scene.camera = camera_object

    def _configure_film(self, context, image_width, image_height):
        context.scene.render.resolution_x = image_width
        context.scene.render.resolution_y = image_height

    def _get_scene_config(self, context):
        properties = context.scene.isometric_scene_properties
        return SceneConfig(
            image_width=properties.image_width,
            image_height=properties.image_height,
            ground_plane_size=properties.ground_plane_size,
        )

    def _get_camera_config(self, image_width, image_height, ground_plane_size):
        diagonal = math.sqrt(2) * ground_plane_size
        camera_position_z = (
            diagonal * image_height / (2 * image_width * math.sin(CAMERA_ROTATION_X))
        )

        return CameraConfig(
            location_x=0.5 * ground_plane_size,
            location_y=-0.5 * ground_plane_size,
            location_z=camera_position_z,
            scale_factor=diagonal,
        )


class ISOMETRIC_OT_render_2d_normals(bpy.types.Operator):
    bl_idname = "isometric.render_2d_normals"
    bl_label = "Render 2D Normals"

    def execute(self, context):
        if context.scene.camera is None:
            self.report({"ERROR"}, "No camera in scene")
            return {"CANCELLED"}

        self._render(context)
        return {"FINISHED"}

    def _render(self, context):
        mat = self._create_material()
        view_layer = context.scene.view_layers["ViewLayer"]
        view_layer.material_override = mat

        bpy.ops.render.render()

        view_layer.material_override = None
        bpy.data.materials.remove(bpy.data.materials["CameraNormal"])

        bpy.ops.render.view_show("INVOKE_DEFAULT")

    def _create_material(self):
        mat = bpy.data.materials.new(name="CameraNormal")
        mat.use_nodes = True
        nodes = mat.node_tree.nodes
        links = mat.node_tree.links

        # clear defaults
        nodes.clear()

        # Geometry node -> Normal output
        geo = nodes.new("ShaderNodeNewGeometry")

        # Vector Transform: World -> Camera
        transform = nodes.new("ShaderNodeVectorTransform")
        transform.vector_type = "NORMAL"
        transform.convert_from = "WORLD"
        transform.convert_to = "CAMERA"

        # Multiply by (1, 1, -1) - flip Z
        flip_z = nodes.new("ShaderNodeVectorMath")
        flip_z.operation = "MULTIPLY"
        flip_z.inputs[1].default_value = (1.0, 1.0, -1.0)

        # Multiply by 0.5
        scale = nodes.new("ShaderNodeVectorMath")
        scale.operation = "SCALE"
        scale.inputs["Scale"].default_value = 0.5

        # Add 0.5 → (0.5, 0.5, 0.5)
        offset = nodes.new("ShaderNodeVectorMath")
        offset.operation = "ADD"
        offset.inputs[1].default_value = (0.5, 0.5, 0.5)

        # Material Output
        output = nodes.new("ShaderNodeOutputMaterial")

        # Link the chain
        links.new(geo.outputs["Normal"], transform.inputs["Vector"])
        links.new(transform.outputs["Vector"], flip_z.inputs[0])
        links.new(flip_z.outputs["Vector"], scale.inputs[0])
        links.new(scale.outputs["Vector"], offset.inputs[0])
        links.new(offset.outputs["Vector"], output.inputs["Surface"])

        return mat
