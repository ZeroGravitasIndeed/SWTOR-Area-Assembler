# SWTOR Area Assembler
swtor_area_assembler is a Blender addon that imports Jedipedia.com's File Reader-exported .json location data into Blender and parses it to auto-import and assemble the area's objects. It shows up in Blender's Import menu. If it appears greyed out, that means it lacks one or both of the following:

* The latest version of SWTOR Slicers' [.gr2 Importer Addon](https://github.com/SWTOR-Slicers/Granny2-Plug-In-Blender-2.8x),
in order to be able to import SWTOR objects into Blender. If you are still using the Legacy version, you can have both installed and coexisting. Just activate the Modern one before using the swtor_area_assembler addon.
* Setting at the addon's preferences the path to a "resources" folder in a SWTOR assets extraction produced by apps such as Slicers GUI or EasyMYP.

It is recommended to toggle Blender's System Console to watch the addon's progress when in use, as there are no other progress indicators yet.

(This is very WIPish. Lots of error catching and quality of life stuff to add yet. Also, this repo lacks any github discipline: it's mostly a code posting area)
