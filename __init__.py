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

from . import panels
from . import properties


def register():
    properties.register()
    panels.register()


def unregister():
    properties.unregister()
    panels.unregister()
