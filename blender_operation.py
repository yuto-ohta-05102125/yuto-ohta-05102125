print("import_filepath:",end="")
IN_filepath = input()
print("export_filepath:",end="")
EX_filepath = input()

import bpy

bpy.context.scene.collection.children['Collection'].objects.unlink(bpy.data.objects['Cube'])

def import_file_wrl(in_filepath =""):
    bpy.ops.import_scene.x3d(
        filepath=in_filepath,
        filter_glob="*.wrl",
        axis_forward="Z",
        axis_up="Y"
    )
    
import_file_wrl(in_filepath = IN_filepath)

bpy.ops.object.select_all(action='DESELECT')

bpy.context.view_layer.objects.active = bpy.data.objects["Shape_IndexedFaceSet"]
bpy.ops.object.select_all(action='SELECT')


def object_parent_set():
    bpy.ops.object.parent_set(
        type='ARMATURE',
        keep_transform=True
    )
object_parent_set()

def export_file_fbx(ex_filepath=""):
    
    bpy.ops.export_scene.fbx(
        filepath=ex_filepath,
        check_existing=True,
        filter_glob="*.fbx",
        use_selection=False,
        use_active_collection=False,
        global_scale=0.01,
        apply_unit_scale=True,
        apply_scale_options='FBX_SCALE_NONE',
        bake_space_transform=False,
        object_types={'ARMATURE', 'MESH'},
        use_mesh_modifiers=True,
        use_mesh_modifiers_render=True,
        mesh_smooth_type='OFF',
        use_subsurf=False,
        use_mesh_edges=False,
        use_tspace=False,
        use_custom_props=False,
        add_leaf_bones=True,
        primary_bone_axis='Y',
        secondary_bone_axis='X',
        use_armature_deform_only=False,
        armature_nodetype='NULL',
        bake_anim=True,
        bake_anim_use_all_bones=True,
        bake_anim_use_nla_strips=True,
        bake_anim_use_all_actions=True,
        bake_anim_force_startend_keying=True,
        bake_anim_step=1.0,
        bake_anim_simplify_factor=1.0,
        path_mode='AUTO',
        embed_textures=False,
        batch_mode='OFF',
        use_batch_own_dir=True,
        use_metadata=True,
        axis_forward='-Z',
        axis_up='Y'
    )
    return


export_file_fbx(ex_filepath = EX_filepath)