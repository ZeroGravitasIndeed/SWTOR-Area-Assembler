# SWTOR Area Assembler
## by ZeroGravitas and Crunch
The **SWTOR Area Assembler** is a Blender add-on that imports and assembles Star Wars: The Old Republic (SWTOR) game locations. It reads Jedipedia.com's **[File Reader](https://swtor.jedipedia.net/reader)**-exported .json area data to auto-import and assemble the area's objects.

**(This tool is also available as part of the [ZeroGravitas SWTOR Tools Add-on](https://github.com/SWTOR-Slicers/ZG-SWTOR-Tools))**

### Full usage guide **[here](https://github.com/SWTOR-Slicers/WikiPedia/wiki/Assembling-SWTOR-Game-Areas-via-the-SWTOR-Area-Assembler-Addon-for-Blender)**.

### Download the latest version of the Addon from **[here](https://github.com/SWTOR-Slicers/SWTOR-Area-Assembler/releases)**.

___

## CHANGELOG:

**v.1.4.0: NEW SIDEBAR USER INTERFACE. BLENDER 4.0-COMPATIBLE (see caveat). Materials Processor and Collections tools.**
* New panel-based UI (in the 3D View's Sidebar), to keep pace with the ZeroGravitas SWTOR Tools version.
* Blender 4.0-compatible (as long as a 4.0-compatible version of the .gr2 Importer Add-on is installed, too).
* Auto-texturing by default.
* New Named Materials Processor Tool.
* New Collections Visibility Tool.
---

**V.1.3.2: LAST IMPORT MENU-BASED VERSION.** Further versions will use a Panel in the Sidebar.

* **Addon-crashing bug corrected**: FXspec-driven elements in .dyn objects weren't being properly filtered out and could crash the importing process (we are still looking at how to handle them in some minimum fashion).
* There's still an issue with some collision objects being parents of others. Somehow they are being filtered out even when not meant to. Investigating…
___
**V.1.3.1: Addon-crashing bug corrected:**
Extensions in .json entries' filepaths weren't thorough enough. Now they are.
* There's still an issue with some collision objects being parents of others. Somehow they are being filtered out even when not meant to. Investigating…
___
**v.1.3.0: Support for placeables:**
Importing of placeables, both static (.plc directly mentioning .gr2 and .mag) and dynamic (.plc mentioning .dyn that in turn contain .gr2 and .mag). That means that objects such as GTN booths, holoprojectors, spaceship cockpit's seats, etc. that weren't appearing in the imported scenes show up now.

Some caveats:
* **The addon's size has grown up to 17 MB!!!** That's because it houses a compressed export of SWTOR's .dyn objects nodetree (dyn.zip). **THERE'S NO NEED TO DECOMPRESS IT**: the addon reads its internal zipped data. We are thinking about future strategies to make such kinds of data available to all addons and avoid duplication.
* There are some object types still unsupported, such as .fxp ones that will be difficult to do other than just dropping their meshes into the scene to make them available, no guarantees about proper transformations. Giving notice of anything missing or weird in our Discord would be appreciated.
* There could be crashes. We seem to be trapping all errors so far. Fingers crossed.
---
**v.1.2.0: New importing options:**
* Show Full Report In Terminal: from now on, the console output will limit itself to a single line of progress per stage of the importing process unless errors are reported. The old barrage of progress reports becomes an option.
* Separate Object Types in SubCollections: creating and sorting objects into Objects, Terrains, and Lights SubCollections is now optional.
* Lights generation's defaults change to not creating them.
---
**v.1.1.3:**

* Added trapping for lack of terrain folder to avoid scary error messages.
---
**v.1.1.2:**
Minor per area-Collections changes:
* Sub-Collections order is now Lights - Terrain - Objects.
* No Terrain Collection if there isn't any terrain object.
* Lights generation's defaults change to not creating them.
---
**v.1.1.1:**

In order to deal with two kinds of enormous area imports that leave Blender in a super-laggy state, the addon provides with these two new options:

* **Hide Objects After Importing**:
    Imported Area objects are hidden ('eye' icon in Outliner, 'h' shortcut) to keep Blender more responsive when having massive amounts of objects per individual Collections. Lag could persist if the Outliner is overloaded, but it should be far more tolerable.
    
     **Recommended when importing .json files weighting several MegaBytes each.**

* **Exclude Collections After Importing**:
    Resulting Collections are excluded (checkbox in Outliner, 'e' shortcut') to keep Blender fully responsive and be able to manage them without lag. Excluded Collections won't list their objects in the Outliner: that's normal.

    **Recommended when importing a massive number of areas, such as whole worlds.**
    
    (Excluding Collections resets the hide/show state of the Collections' contents. The **Hide Objects After Importing** option won't have an effect if the **Exclude Collections After Importing** option is on)