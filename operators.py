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
            config.image_height, config.ground_plane_size
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

    def _get_camera_config(self, image_height, ground_plane_size):
        alpha = CAMERA_ROTATION_X
        beta = math.radians(90) - alpha
        sqrt_2 = math.sqrt(2)
        half = 0.5
        diagonal = sqrt_2 * ground_plane_size

        camera_position_xy = half * (math.sin(beta) * image_height - diagonal)
        camera_position_x = sqrt_2 * camera_position_xy
        camera_position_y = sqrt_2 * camera_position_xy
        camera_position_z = half * ground_plane_size * math.cos(beta)

        return CameraConfig(
            location_x=camera_position_x,
            location_y=camera_position_y,
            location_z=camera_position_z,
            scale_factor=diagonal,
        )


class ISOMETRIC_OT_render_2d_normals(bpy.types.Operator):
    bl_idname = "isometric.render_2d_normals"
    bl_label = "Render 2D Normals"

    def execute(self, context):
        self._render()

    def _render(self):
        # TODO render scene but assign special material to all objects (temporarely)
        return {"FINISHED"}
