| **Updated to 2.0** |
|:-------------------|

BlenderFDS is based on Blender. You do not need to be a Blender power user to use BlenderFDS, but it is much better if you are already familiar with its particular interface and you are able to quickly build simple architectural models. See the list of resources provided in the [Learning Blender](LearningBlender.md) page for help.

Before starting the detailed description of BlenderFDS UI, let's give a quick look to the default Blender user interface organization.




---


# General Blender UI organization #

Before starting, please watch this screencast:

http://www.blendercookie.com/getting-started-with-blender-navigation-and-interface/

and read the first part of Blender User Manual:

http://wiki.blender.org/index.php/Doc:2.6/Manual

The Blender UI is composed of `editors`, `headers`, `context buttons`, `panels`, and `controls`.

The `editors` are non-overlapping parts of the UI that divide the Blender application window. There are several types of `editors`, which respond to specific functions. Each editor has its own `header`. An `header` is a menubar positioned either at the top or at the bottom of its hosting `editor`.

![http://lh5.ggpht.com/_iTIkwVoSUm0/S9Q9XPLQ0sI/AAAAAAAAAPc/htwJl2k8C3A/650px-Ui-organization.jpg](http://lh5.ggpht.com/_iTIkwVoSUm0/S9Q9XPLQ0sI/AAAAAAAAAPc/htwJl2k8C3A/650px-Ui-organization.jpg)

The previous figure shows a typical Blender application windows divided into the following `editors`:
  * `3D view editor`, positioned at the upper left side. It shows a 3D view of the `scene`.
  * `outliner editor` at the upper right side, that lists the created Blender entities and their relations.
  * `properties editor` at the bottom right side of the application window. This editor groups options and properties of active Blender entities.
  * `timeline editor` at the bottom left side of the interface. This is not used for BlenderFDS and can be closed.

## Split and combine `editors` ##

In the upper right hand corner of each editor is the `editor splitter widget`. It looks like a little ridged thumb grip. When you hover over it, your cursor changes to a cross: left-click and drag it to split and combine `editors`.

## Fold and unfold `headers` ##

To hide an `editor header`, just drag the header down till it folds. To unhide it, click on those small white `+` icon that you see on the sides.

# The `3D view editor` #

The `3D view editor` is used for viewing and editing `scenes`.

The `tool shelf` and the `properties` of the `3D view editor` can be unfolded by clicking on the small white `+` icon at the upper left and upper right corners of the `editor`.

![https://lh6.googleusercontent.com/_iTIkwVoSUm0/TXdTEJ_CzzI/AAAAAAAAAZk/Z07IyOIQnKA/s640/blender%203D%20view%20editor.png](https://lh6.googleusercontent.com/_iTIkwVoSUm0/TXdTEJ_CzzI/AAAAAAAAAZk/Z07IyOIQnKA/s640/blender%203D%20view%20editor.png)

# The `outliner editor` #

The `outliner editor` is a hierarchical diagram displaying a list of all Blender entities, their parents and progeny. It is used for easily navigating complex `scenes`:

![https://lh5.googleusercontent.com/-a1wOmS4D37g/TjAWhydxt3I/AAAAAAAAAfU/pMm70faQyWY/s463/outliner-window.png](https://lh5.googleusercontent.com/-a1wOmS4D37g/TjAWhydxt3I/AAAAAAAAAfU/pMm70faQyWY/s463/outliner-window.png)

# The `properties editor` #

The `properties editor` displays options and properties of active Blender entities. The properties are grouped in homogeneous `panels`. The `context buttons` at the top of the `editor` let the user select the `panels` that are to be shown depending on the desired context.

Every `Panel` contains `controls`, that let the user handle options and properties.

## BlenderFDS adds FDS-specific `panels` ##

Depending on the chosen context, BlenderFDS adds several FDS-specific `panels` to the `properties editor`.

![https://lh3.googleusercontent.com/_iTIkwVoSUm0/TXdOE_xsFTI/AAAAAAAAAZY/ICb_ZgaykMg/s640/blender%20context%20and%20panels.png](https://lh3.googleusercontent.com/_iTIkwVoSUm0/TXdOE_xsFTI/AAAAAAAAAZY/ICb_ZgaykMg/s640/blender%20context%20and%20panels.png)

When opening a new Blender file, the BlenderFDS `panels` are listed as the last ones at the bottom of the `properties editor`, and can be hidden under the pile of the other default `panels`. If needed, the user can easily reorder the pile by dragging the hidden `panels` to the top of the list.

![https://lh3.googleusercontent.com/_iTIkwVoSUm0/TXdTxQ86rfI/AAAAAAAAAZ0/HW3EtF4QWS0/blender%20dragging%20panel.png](https://lh3.googleusercontent.com/_iTIkwVoSUm0/TXdTxQ86rfI/AAAAAAAAAZ0/HW3EtF4QWS0/blender%20dragging%20panel.png)