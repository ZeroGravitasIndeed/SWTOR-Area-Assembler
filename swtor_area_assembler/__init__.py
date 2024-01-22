import sys
import importlib

import bpy

# Add-on Metadata

bl_info = {
    "name": "SWTOR Area Assembler",
    "author": "ZeroGravitas & Crunch",
    "version": (1, 4, 0),
    "blender": (3, 6, 0),
    "category": "SWTOR",
    "location": "3D View > Sidebar > SWTOR Area Tools panel",
    "description": "Imports Jedipedia.net-exported SWTOR .DAT Files converted to .JSON Format",
    "doc_url": "https://github.com/SWTOR-Slicers/WikiPedia/wiki/Assembling-SWTOR-Game-Areas-via-the-SWTOR-Area-Assembler-Addon-for-Blender",
    "tracker_url": "",
}

# Add-on modules loader: 
# Simplifies coding the loading of the modules to keeping a list of their names
# (See https://b3d.interplanety.org/en/creating-multifile-add-on-for-blender/ )

# Determine Blender version
blender_version_major_number, blender_version_minor_number , _ = bpy.app.version

if blender_version_major_number == 4:
    modulesNames = [
        'preferences',
        'area_import_4',
        'process_named_mats_4',
        'area_collections_exclude_include',
        'ui',
        ]
else:
    modulesNames = [
        'preferences',
        'area_import',
        'process_named_mats',
        'area_collections_exclude_include',
        'ui',
        ]


modulesFullNames = {}
for currentModuleName in modulesNames:
    modulesFullNames[currentModuleName] = ('{}.{}'.format(__name__, currentModuleName))

for currentModuleFullName in modulesFullNames.values():
    if currentModuleFullName in sys.modules:
        importlib.reload(sys.modules[currentModuleFullName])
    else:
        globals()[currentModuleFullName] = importlib.import_module(currentModuleFullName)
        setattr(globals()[currentModuleFullName], 'modulesNames', modulesFullNames)


def register():
    for currentModuleName in modulesFullNames.values():
        if currentModuleName in sys.modules:
            if hasattr(sys.modules[currentModuleName], 'register'):
                sys.modules[currentModuleName].register()

def unregister():
    for currentModuleName in modulesFullNames.values():
        if currentModuleName in sys.modules:
            if hasattr(sys.modules[currentModuleName], 'unregister'):
                sys.modules[currentModuleName].unregister()
 
if __name__ == "__main__":
    register()#
