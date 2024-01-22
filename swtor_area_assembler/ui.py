import bpy
import addon_utils
from pathlib import Path


class SWTOR_PT_files_tools(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "SWTOR Area Tools"
    bl_label = "SWTOR Area Tools"

    def draw(self, context):

        # Checks:
        
        # Extracted SWTOR assets' "resources" folder. 
        swtor_resources_folderpath = bpy.context.preferences.addons[__package__].preferences.swtor_resources_folderpath
        resources_folder_exists = ( Path(swtor_resources_folderpath) / "art/shaders/materials").exists()
        
        # .gr2 Importer Addon
        modern_gr2_addon_is_enabled = addon_utils.check("io_scene_gr2")[1]
        legacy_gr2_addon_is_enabled = addon_utils.check("io_scene_gr2_legacy")[1]






        # Checks and Status display
        
        layout = self.layout

        # Show whether the 'resources' folder is set correctly in Preferences.
        swtor_addon_status = layout.column(align=True)
        swtor_addon_status.scale_y = 0.75
        
        swtor_addon_status.alert = False  # Reset alert
        if resources_folder_exists:
            swtor_addon_status.label(text="• 'resources' Folder: SET")
        else:
            swtor_addon_status.alert = True
            swtor_addon_status.label(text="• 'resources' Folder: NOT SET")


        swtor_addon_status.alert = False  # Reset alert
        if modern_gr2_addon_is_enabled is True:
            swtor_addon_status.label(text="• .gr2 Add-on: SET")
        else:
            swtor_addon_status.alert = True
            swtor_addon_status.label(text="• .gr2 Add-on: NOT SET")


        swtor_addon_status.alert = False  # Reset alert
        if resources_folder_exists is False or modern_gr2_addon_is_enabled is False:
            swtor_addon_status.label(text=" ")
            swtor_addon_status.label(text="Check the Area Assembler's")
            swtor_addon_status.label(text="requirements in its Tooltips.")






        # CHECKS:
        # Extracted SWTOR assets' "resources" folder. 
        swtor_resources_folderpath = bpy.context.preferences.addons[__package__].preferences.swtor_resources_folderpath
        resources_folder_exists = ( Path(swtor_resources_folderpath) / "art/shaders/materials").exists()
        # .gr2 Importer Addon
        modern_gr2_addon_is_enabled = addon_utils.check("io_scene_gr2")[1]




        # character_assembler UI
        tool_section = layout.box().column(align=True)
        tool_section.scale_y = 1.0
        tool_section.enabled = resources_folder_exists
        tool_section.alert = tool_section.enabled is False
        
        tool_section.label(text="SWTOR Area Assembler")
        tool_section.operator("swtor.area_assembler", text="Select Area .json' Files")

        tool_section_props = tool_section.column(align=True)
        tool_section_props.scale_y = 0.80
        tool_section_props.prop(context.scene, "SAA_ApplyFinalRotation",    text="Apply Final Rotation")
        tool_section_props.prop(context.scene, "SAA_ApplyMaterials",        text="Process Named Materials")
        tool_section_props.prop(context.scene, "SAA_ApplySceneScale",       text="Apply x10 Scene Scale")
        tool_section_props.prop(context.scene, "SAA_SkipDBOObjects",        text="Skip dbo Objects")
        tool_section_props.prop(context.scene, "SAA_CreateSceneLights",     text="Create Scene Lights")
        tool_section_props.prop(context.scene, "SAA_CollectionObjects",     text="Collect Objects By Type")
        tool_section_props.prop(context.scene, "SAA_MergeMultiMeshObjects", text="Merge Multi-Mesh Objects")
        tool_section_props.prop(context.scene, "SAA_ShowFullReport",        text="Full Report In Terminal")
        tool_section_props.label(text="")
        tool_section_props.label(text="To keep Blender responsive")
        tool_section_props.label(text="after importing massive areas:")
        tool_section_props.prop(context.scene, "SAA_HideAfterImport",       text="Hide Objects",)
        tool_section_props.prop(context.scene, "SAA_ExcludeAfterImport",    text="Hide Collections' Contents",)




        # PROCESS NAMED MATERIALS UI
        tool_section = layout.box().column(align=True)
        tool_section.enabled = resources_folder_exists
        tool_section.alert = tool_section.enabled is False

        tool_section.label(text="Process Named Materials In")

        split = tool_section.split(factor= 0.75, align=True)
        col_left, col_right = split.column(align=True), split.column(align=True)

        process_mats_sel = col_left.operator("swtor.process_named_mats", text="Selected Objects")
        col_left.enabled = len(bpy.context.selected_objects) != 0
        process_mats_sel.use_selection_only = True

        process_mats_all = col_right.operator("swtor.process_named_mats", text="All")
        col_right.enabled = len(bpy.data.objects) != 0
        process_mats_all.use_selection_only = False

        process_mats_sel = tool_section.prop(context.scene, "use_overwrite_bool", text="Overwrite Materials")
        process_mats_all = tool_section.prop(context.scene, "use_collect_colliders_bool", text="Collect Collider Objects")
        
        
        
        
        # exclude_all_collections UI
        tool_section = layout.box().column(align=False)
        tool_section.label(text="Outliner Collections' Visibility")

        split = tool_section.split(factor= 0.70, align=True)
        col_left, col_right = split.column(align=True).row(align=True), split.column(align=True).row(align=True)
        disable_all = col_left.operator("swtor.exclude_include_collections", text="Disable Selected")
        disable_all.action = "DISABLE_SEL"
        disable_sel = col_right.operator("swtor.exclude_include_collections", text="All")
        disable_sel.action = "DISABLE_ALL"
        
        split = tool_section.split(factor= 0.70, align=True)
        col_left, col_right = split.column(align=True).row(align=True), split.column(align=True).row(align=True)
        disable_all = col_left.operator("swtor.exclude_include_collections", text="Enable Selected")
        disable_all.action = "ENABLE_SEL"
        disable_sel = col_right.operator("swtor.exclude_include_collections", text="All")
        disable_sel.action = "ENABLE_ALL"

        tool_section.prop(context.scene, "SAAEAC_recursive", text="Children Of Selected Too")
        


 
 
 
 
 
        

# Registrations

classes = [
    SWTOR_PT_files_tools,
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

    
if __name__ == "__main__":
    register()