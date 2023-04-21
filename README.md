# SWTOR Area Assembler
## by ZeroGravitas and Crunch
swtor_area_assembler is a Blender addon that imports Jedipedia.com's **[File Reader](https://swtor.jedipedia.net/reader)**-exported .json location data into Blender and parses it to auto-import and assemble the area's objects. It shows up in Blender's Import menu. If it appears greyed out, that means it lacks one or both of the following:

* The latest version of SWTOR Slicers' [.gr2 Importer Addon](https://github.com/SWTOR-Slicers/Granny2-Plug-In-Blender-2.8x),
in order to be able to import SWTOR objects into Blender. If you are still using the Legacy version, you can have both installed and coexisting. Just activate the Modern one before using the swtor_area_assembler addon.
* Setting in the addon's preferences the path to a "resources" folder in a SWTOR assets extraction produced by apps such as Slicers GUI or EasyMYP.

It is recommended to toggle Blender's System Console to watch the addon's progress when in use, as there are no other progress indicators yet.

Download the latest version of the Addon from **[here](https://github.com/SWTOR-Slicers/SWTOR-Area-Assembler/releases)**.

Provisional instructions on how to produce the requisite area data .json files in **[this PDF](https://raw.githubusercontent.com/SWTOR-Slicers/SWTOR-Area-Assembler/main/How%20to%20export%20SWTOR%20area%20data.pdf)**.

___

**v.1.1.2:**
Minor per area-Collections changes:
* Sub-Collections order is now Lights - Terrain - Objects.
* No Terrain Collection if there isn't any terrain object.

**v.1.1.1:**

In order to deal with two kinds of enormous area imports that leave Blender in a super-laggy state, the addon provides with these two new options:

* **Hide Objects After Importing**:
    Imported Area objects are hidden ('eye' icon in Outliner, 'h' shortcut) to keep Blender more responsive when having massive amounts of objects per individual Collections. Lag could persist if the Outliner is overloaded, but it should be far more tolerable.
    
     **Recommended when importing .json files weighting several MegaBytes each.**

* **Exclude Collections After Importing**:
    Resulting Collections are excluded (checkbox in Outliner, 'e' shortcut') to keep Blender fully responsive and be able to manage them without lag. Excluded Collections won't list their objects in the Outliner: that's normal.

    **Recommended when importing a massive number of areas, such as whole worlds.**

(Excluding Collections resets the hide/show state of the Collections' contents. The **Hide Objects After Importing** option won't have an effect if the **Exclude Collections After Importing** option is on)
