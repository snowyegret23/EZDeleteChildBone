import bpy

class EZDELETECB_PT_main_panel(bpy.types.Panel):
    bl_label = "EZDeleteChildBone"
    bl_idname = "EZDELETECB_PT_main_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'EZDeleteChildBone'

    def draw(self, context):
        layout = self.layout
        layout.operator("ezdeletecb.delete_child_bones")

def register():
    bpy.utils.register_class(EZDELETECB_PT_main_panel)

def unregister():
    bpy.utils.unregister_class(EZDELETECB_PT_main_panel)