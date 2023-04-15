# SWTOR Area Assembler
## by ZeroGravitas and Crunch
swtor_area_assembler is a Blender addon that imports Jedipedia.com's **[File Reader](https://swtor.jedipedia.net/reader)**-exported .json location data into Blender and parses it to auto-import and assemble the area's objects. It shows up in Blender's Import menu. If it appears greyed out, that means it lacks one or both of the following:

* The latest version of SWTOR Slicers' [.gr2 Importer Addon](https://github.com/SWTOR-Slicers/Granny2-Plug-In-Blender-2.8x),
in order to be able to import SWTOR objects into Blender. If you are still using the Legacy version, you can have both installed and coexisting. Just activate the Modern one before using the swtor_area_assembler addon.
* Setting at the addon's preferences the path to a "resources" folder in a SWTOR assets extraction produced by apps such as Slicers GUI or EasyMYP.

It is recommended to toggle Blender's System Console to watch the addon's progress when in use, as there are no other progress indicators yet.

Download the latest version of the Addon from **[here](https://github.com/SWTOR-Slicers/SWTOR-Area-Assembler/releases)**.

Provisional instructions on how to produce the requisite area data .json files in **[this PDF](https://raw.githubusercontent.com/SWTOR-Slicers/SWTOR-Area-Assembler/main/How%20to%20export%20SWTOR%20area%20data.pdf)**.

___
v.1.1.0:
- New Hide Collections In Viewport After Importing option. When importing, it unticks the checkboxes of the per-location (.json file) Collections. Meant for massive importations of location data, such as when importing whole SWTOR worlds (a Dromund Kaas, a Coruscant). By disabling the Collections in the View Layer, Blender won't get stuck under the weight of so many objects to visualize and will let us save the project immediately or do some organization without lagging hard.

- Basic support for importing pre-generated terrain patches (that requires a heightmap-to-.obj tool that is still in progress.
