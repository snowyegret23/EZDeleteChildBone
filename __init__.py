bl_info = {
    "name": "EZDeleteChildBone",
    "author": "Snowyegret",
    "version": (1, 0),
    "blender": (3, 6, 0),
    "location": "View3D > Sidebar > EZDeleteChildBone",
    "description": "Delete all child bones of selected bones",
    "category": "Rigging",
}

import bpy
from . import ezdeletecb_operation
from . import ezdeletecb_panel

def register():
    ezdeletecb_operation.register()
    ezdeletecb_panel.register()

def unregister():
    ezdeletecb_operation.unregister()
    ezdeletecb_panel.unregister()

if __name__ == "__main__":
    register()