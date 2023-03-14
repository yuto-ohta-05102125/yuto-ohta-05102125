print("import_filepath:",end="")
IN_filepath = input()
print("export_filepath:",end="")
EX_filepath = input()

import bpy

#デフォルトで存在するCubeを削除する
bpy.context.scene.collection.children['Collection'].objects.unlink(bpy.data.objects['Cube'])

#wrlファイルをインポートする
def import_file_wrl(in_filepath =""):
    bpy.ops.import_scene.x3d(
        filepath=in_filepath,
        filter_glob="*.wrl",
        axis_forward="Z",
        axis_up="Y"
    )
    
import_file_wrl(in_filepath = IN_filepath)

#インポートした3Dモデルの全選択状態を解除する
bpy.ops.object.select_all(action='DESELECT')

#3Dモデルの一部であるShape_IndexedFaceSetをアクティブ状態にする
bpy.context.view_layer.objects.active = bpy.data.objects["Shape_IndexedFaceSet"]

#3Dモデルの全てを選択状態にする
bpy.ops.object.select_all(action='SELECT')

#ARMATUREを有効にして、3Dモデルを親子関係にする
def object_parent_set():
    bpy.ops.object.parent_set(
        type='ARMATURE',
        keep_transform=True
    )
object_parent_set()

#global_scaleとobject_typesをデフォルトと変更した状態でFBXファイルとしてエクスポートする
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

import os

#上書き設定
if os.path.exists(EX_filepath):
    confirm = input("ファイルが存在します。上書きしてもよろしいですか？(y/n): ")
    if confirm.lower() != "y":
        print("処理を中止しました。")
        exit()
