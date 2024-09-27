import bpy

class EZDELETECB_OT_delete_child_bones(bpy.types.Operator):
    bl_idname = "ezdeletecb.delete_child_bones"
    bl_label = "Delete Child Bones"
    bl_description = "Delete all child bones of selected bones"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if context.mode != 'EDIT_ARMATURE':
            self.report({'WARNING'}, "Must be in Edit Mode")
            return {'CANCELLED'}

        armature = context.active_object
        if armature.type != 'ARMATURE':
            self.report({'WARNING'}, "Active object must be an Armature")
            return {'CANCELLED'}

        selected_bones = [bone.name for bone in armature.data.edit_bones if bone.select]

        total_deleted = 0

        for bone_name in selected_bones:
            bpy.ops.armature.select_all(action='DESELECT')
            bone = armature.data.edit_bones[bone_name]
            bone.select = True
            armature.data.edit_bones.active = bone
            
            bpy.ops.armature.select_similar(type='CHILDREN')

            selected_count = len([b for b in armature.data.edit_bones if b.select]) - 1

            bpy.ops.armature.delete()
            
            total_deleted += selected_count

        self.report({'INFO'}, f"Deleted {total_deleted} child bones.")
        return {'FINISHED'}

def register():
    bpy.utils.register_class(EZDELETECB_OT_delete_child_bones)

def unregister():
    bpy.utils.unregister_class(EZDELETECB_OT_delete_child_bones)