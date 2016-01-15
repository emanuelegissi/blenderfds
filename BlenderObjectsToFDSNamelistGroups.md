| **Updated to 2.0** |
|:-------------------|

Each Blender `object` is exported as one or more FDS namelist groups sharing the same parameters. The FDS parameters assigned to each `object` are specified in the `object properties panel`. Different options and properties are displayed depending on the associated FDS namelist group, obeying to FDS semantic.

The user builds the architectural model. Each element is split in parts. Each part should have homogeneous thermo-physical properties, as each Blender `object` can only have one set of FDS parameters assigned.




---


# FDS namelist group parameters #

The user describes every geometric FDS namelist group in the BlenderFDS `object properties panel`. The following paragraphs list one by one some of the parameters managed by the BlenderFDS interface.

## Syntax errors ##

BlenderFDS performs some simple checks on the syntax of the input parameters. The following example shows an unknown `namelist` and an `ID` parameter containing an unacceptable quote character:

![https://lh5.googleusercontent.com/_iTIkwVoSUm0/TXdX2LphPgI/AAAAAAAAAaM/wBNaxi33G4Q/blender%20error.png](https://lh5.googleusercontent.com/_iTIkwVoSUm0/TXdX2LphPgI/AAAAAAAAAaM/wBNaxi33G4Q/blender%20error.png)

BlenderFDS _does not enforce_ any automatic correction. It's up to the user to provide meaningful and syntactically correct parameters.

## `Namelist` parameter ##

The first and most important parameter of the `object properties panel` is the namelist group name `Namelist`. If BlenderFDS recognizes the namelist, the `panel` is udapted accordingly and shows relevant parameters only. The same `panel` label is updated to host a descriptive identification of the chosen namelist.

```
&OBST /
```

## `ID` parameter ##

The `ID` parameter is based on the Blender `object` name:

```
ID='Wall'
```

Some namelist groups still do not allow the insertion of the `ID` parameter. We reported the issue to FDS developers, as the presence of an `ID` parameter in all namelists could ease debugging of the FDS file. See [FDS Issue 887](http://code.google.com/p/fds-smv/issues/detail?id=887&can=1&q=reporter%3Aemanuele.gissi).

## `FYI` parameter ##

The `FYI` parameter contains user's comments and informations and is inserted as it is into namelist groups when not empty:

```
FYI='This is a comment.'
```

## `SURF_ID`, `SURF_ID3`, and `SURF_ID6` parameters ##

When the Blender `object` has a suitable namelist group name (`OBST, VENT`...) and the reference to a Blender material exists, BlenderFDS automatically configures and shows the relevant `SURF_ID` parameter referring to the appropriate Blender material:

```
SURF_ID='Brick wall'
```

The following is an example of a `VENT object` description:

![https://lh5.googleusercontent.com/-DJfmcPIkwu8/UDOtstsLLUI/AAAAAAAAApA/VpPimsr_FCA/s409/VENT.png](https://lh5.googleusercontent.com/-DJfmcPIkwu8/UDOtstsLLUI/AAAAAAAAApA/VpPimsr_FCA/s409/VENT.png)

| **New in 2.0**: why `SURF_ID3` and `SURF_ID6` are not supported |
|:----------------------------------------------------------------|

`SURF_ID3` and `SURF_ID6` parameters are not supported by BlenderFDS. These parameters parameters depend on the absolute orientation of the reference system. In Blender each object has its local ref system, that can be rotated, scaled, moved, thus not aligned any more with the global system.

I personally find `SURF_ID3` and `SURF_ID6` parameters rather _unclean_ and prefer to create separate `VENT` objects. I usually _duplicate_ the desired face and _separate_ it from the original object by creating a new Blender object. Then I move the new object slightly outside the original object, and finally set the new `VENT` namelist and its properties.

The new `VENT` object can be _parented_ to the original `OBST` to follow its translations, rotations and scalings.

See Blender manual on how to:
  * [duplicate elements](http://wiki.blender.org/index.php/Doc:2.6/Manual/Modeling/Objects/Duplication);
  * [separating, grouping and parenting objects](http://wiki.blender.org/index.php/Doc:2.6/Manual/Modeling/Objects/Groups_and_Parenting).

## `SAWTOOTH` and `THICKEN` parameters ##

| **New in 2.0**: `THICKEN` parameter |
|:------------------------------------|

In case of an `OBST object`, the user can insert the `SAWTOOTH=.FALSE.` and the `THICKEN=.TRUE.` parameters.

The following is an example of an `OBST object` description:

![https://lh4.googleusercontent.com/-Ft-Ybatvle4/UDOtrLHQTcI/AAAAAAAAAo0/TeMbBwsd33c/s427/OBST.png](https://lh4.googleusercontent.com/-Ft-Ybatvle4/UDOtrLHQTcI/AAAAAAAAAo0/TeMbBwsd33c/s427/OBST.png)

## `IJK` parameter ##

| **New in 2.0**: `IJK` setup  |
|:-----------------------------|

When the user enters a `MESH object`, the `panel` is updated to show the `IJK` parameter.

BlenderFDS checks if the number of cells requested by the user along the y and the z axis respects the requirements of the FDS Poisson solver. If this is not the case the user can push the button `Correct IJK` and set good values, as explained in paragraph § 6.3.1 of the FDS User's guide.

Meshes alignment can become a nightmare: I usually adapt mesh geometric dimensions to obtain good J and K values and correctly aligned meshes. This sometimes requires wizardry arts...

The parameter is then exported as follows:

```
IJK=12,50,50
```

The following is an example of an `MESH object` description:

![https://lh6.googleusercontent.com/-tX23Y_ZxXIo/UDdEJ7pHy5I/AAAAAAAAAqM/79Q4CPZxqgE/s800/MESH.png](https://lh6.googleusercontent.com/-tX23Y_ZxXIo/UDdEJ7pHy5I/AAAAAAAAAqM/79Q4CPZxqgE/s800/MESH.png)

## `Custom parameters` ##

`Custom parameters` field is used to include other FDS parameters to the namelist group. BlenderFDS inserts the `Custom parameters` value as it is, verbatim, and does not perform any check on its semantic. The user should use paired single quotes (eg: `PAR1='This is a string', PAR2='This is another'`) for strings in order to conserve uniformity with auto-generated FDS parameters.

# FDS namelist group geometry #

A Blender `object` is transformed into one or more FDS namelist groups depending on the complexity of its geometry and on the user requirements. The exported geometry is set using the `XB`, `XYZ`, `PBX`, `PBY`, or `PBZ` `object` parameters.

## `XB` parameter ##

| **Blender `object` `XB` set to** | **Exported as** | **Number of exported FDS namelists** |
|:---------------------------------|:----------------|:-------------------------------------|
| None                             | `XB` not set    | None                                 |
| Voxels                           | Voxelized solid | Many                                 |
| BBox                             | Bounding box    | Only one                             |
| Faces                            | Faces, one for each face of the Blender `object` | Number of `object mesh faces`        |
| Edges                            | Segments, one for each edge of the Blender `object` | Number of `object mesh edges`        |

### `XB` set to `None` ###

No `XB` parameter is added to the exported namelist group.

### `XB` set to `Voxels` ###

| **New in 2.0**: New voxelization algorithm |
|:-------------------------------------------|

The Blender `object` is treated by a voxelization algorithm that approximates its geometry as if it was made up of [Lego](http://www.lego.com) bricks. Objects are converted from their continuous geometric representation into a set of voxels that best approximates the continuous geometry of the object. The voxel size is specified by the user on a per-object basis, according to the desired accuracy.

The previous releases of BlenderFDS used a common _marching cube algorithm_ implemented in Python by Michael Schardt for Blender 2.48 and released under a GPL license. Due to its inherent slowness and other precision problems, this algorithm was replaced in BlenderFDS 2.0 by a direct employ of the Blender Remesh modifier contributed by Nicholas Bishop to Blender 2.62. This modifier uses a new method for contouring a signed grid developed by Tao Ju _[Ju, T., Losasso, F., Schaefer, S., Warren, J., Dual Contouring of Hermite Data, Proceedings of ACM SIGGRAPH, 21-26 July 2002]_. The new algorithm is much faster than the previous one.

![http://lh5.ggpht.com/_iTIkwVoSUm0/S9dLEyo67MI/AAAAAAAAASc/yvSFrr20JEI/lego_building.jpg](http://lh5.ggpht.com/_iTIkwVoSUm0/S9dLEyo67MI/AAAAAAAAASc/yvSFrr20JEI/lego_building.jpg)

When possible, BlenderFDS joins the voxels together in larger _boxes_ to minimize the number of lines of the FDS input file. The boxes sides are always aligned with the global reference system axis, as required by FDS:

![http://lh6.ggpht.com/_iTIkwVoSUm0/S9dRqlKwESI/AAAAAAAAASo/uu5-xDqgHe8/voxelization.png](http://lh6.ggpht.com/_iTIkwVoSUm0/S9dRqlKwESI/AAAAAAAAASo/uu5-xDqgHe8/voxelization.png)

Here is an example of a cylinder voxelization using different voxel sizes:

![https://lh3.googleusercontent.com/_iTIkwVoSUm0/TXY1dvieKZI/AAAAAAAAAYg/K4RfeEuwwjM/blender%20voxel%20boxel.png](https://lh3.googleusercontent.com/_iTIkwVoSUm0/TXY1dvieKZI/AAAAAAAAAYg/K4RfeEuwwjM/blender%20voxel%20boxel.png)

| **New in 2.0**: The new voxelization algorithm can treat both _manifold_ and _non manifold_ objects |
|:----------------------------------------------------------------------------------------------------|

The new voxelization algorithm can treat both _manifold_ and _non manifold_ objects, but exported geometries are more precise if the originating objects are _manifold_, that is water-tight and well-formed, so that BlenderFDS can decide which portion of space is solid and which is instead void. This is the reason why, if the object is non manifold, a warning message is displayed.

There is a specific page explaining how to deal with non manifold objects: [Dealing with non-manifold objects](NonManifoldObjects.md).

When setting `XB` to `Voxels`, the overall shape of the `object` is conserved as much as possible:

![http://lh6.ggpht.com/_iTIkwVoSUm0/S9dgyoPwZrI/AAAAAAAAAS0/Lp5CL2daR5c/voxels_shape.png](http://lh6.ggpht.com/_iTIkwVoSUm0/S9dgyoPwZrI/AAAAAAAAAS0/Lp5CL2daR5c/voxels_shape.png)

The Blender `object` is exported to many FDS namelist groups sharing the same parameters, and covering the same geometry. For example:

```
&OBST ID='Wall_0', XB=-1.575,-1.375,-1.375,0.475,0.025,1.975, SURF_ID='Gypsum wall',
      SAWTOOTH=.False., FYI='Voxelized walls' /
&OBST ID='Wall_1', XB=-1.575,-1.375,-1.375,1.375,1.975,3.025, SURF_ID='Gypsum wall',
      SAWTOOTH=.False., FYI='Voxelized walls' /
&OBST ID='Wall_2', XB=-1.575,-1.375,0.475,1.375,-0.025,1.975, SURF_ID='Gypsum wall',
      SAWTOOTH=.False., FYI='Voxelized walls' /
&OBST ID='Wall_3', XB=-1.575,-0.675,-1.575,-1.525,-0.025,3.025, SURF_ID='Gypsum wall',
      SAWTOOTH=.False., FYI='Voxelized walls' /
&OBST ID='Wall_4', XB=-1.575,0.625,-1.525,-1.475,-0.025,3.025, SURF_ID='Gypsum wall',
      SAWTOOTH=.False., FYI='Voxelized walls' /
...
```

### Voxel size ###

| **New in 2.0**: Voxel size on a per-object basis |
|:-------------------------------------------------|

The voxel is cubic and its size is specified by the user on a per-object basis, according to the desired accuracy. When exporting to FDS, geometric features that are smaller than voxel size are automatically filtered out by the voxelization algorithm.

When voxel size is too small compared to object size, the number of voxels grows too much. To prevent out of memory conditions, an error message appears and the required voxel size is not guaranteed:

![https://lh4.googleusercontent.com/-HXPS7rO4dnQ/UDdUl0xhLyI/AAAAAAAAAq0/OeXtD8Os6-8/s800/size%2520too%2520large%2520voxel%2520no.png](https://lh4.googleusercontent.com/-HXPS7rO4dnQ/UDdUl0xhLyI/AAAAAAAAAq0/OeXtD8Os6-8/s800/size%2520too%2520large%2520voxel%2520no.png)

Reduce the size of the voxelized object (eg by splitting it in two smaller objects) until the error message disappears.

### Visualizing voxels ###

| **New in 2.0**: Generated voxels visualization |
|:-----------------------------------------------|

Generated voxels can be easily visualized and interactively modified by the user before exporting by pushing the `Show Voxels` buttons. Once verified the quality of the voxelization, the user can hide all the voxels by pushing the `Hide All Voxels` button.

![https://lh5.googleusercontent.com/-7dwgGWD9WiE/UDdQWIdJdEI/AAAAAAAAAqc/XXA173wKCYw/s800/show-hide%2520voxels.png](https://lh5.googleusercontent.com/-7dwgGWD9WiE/UDdQWIdJdEI/AAAAAAAAAqc/XXA173wKCYw/s800/show-hide%2520voxels.png)

### `XB` set to `BBox` ###

BlenderFDS calculates the `object` bounding box in global coordinates. The resulting box coordinates are exported as `XB` parameter of one FDS namelist group.

In `BBox`, the overall shape of the `object` is not conserved, only its size is preserved:

![http://lh6.ggpht.com/_iTIkwVoSUm0/S9dgyfvZf5I/AAAAAAAAASw/mbMTAOg73MU/bbox_shape.png](http://lh6.ggpht.com/_iTIkwVoSUm0/S9dgyfvZf5I/AAAAAAAAASw/mbMTAOg73MU/bbox_shape.png)

and the Blender `object` is exported to one only FDS namelist group, for example:

```
&OBST ID='Wall', XB=0.123,2.233,0.123,2.233,0.123,2.233, SURF_ID='Gypsum wall',
      FYI='BBox wall' /
```

### `XB` set to `Faces` ###

BlenderFDS calculates the bounding box in global coordinates of the Blender `object` `faces`. Each `face` is flattened, and its edges straightened. The result is a group of right plane faces with edges parallel to the global axis, as required by FDS. The resulting coordinates are exported as `XB` parameters of many FDS namelist group, one for each `face`:

![http://lh4.ggpht.com/_iTIkwVoSUm0/S9d7GeTrJwI/AAAAAAAAAS8/gRl3cFbu1fk/face_shape.png](http://lh4.ggpht.com/_iTIkwVoSUm0/S9d7GeTrJwI/AAAAAAAAAS8/gRl3cFbu1fk/face_shape.png)

Of course. it is much more clean and less prone to errors to directly model "straight" `faces`, acceptable by FDS without transformation.

For example, `XB` set to `Faces` setting can be profitably employed to describe several `VENTs` that share the same parameters. The user creates an `object` made of separate `faces` distributed inside the building, and obtains a series of `VENTs`:

```
&VENT ID='Fan_0', XB=5.000,6.000,0.000,1.000,7.134,7.134, SURF_ID='Supply',
      DEVC_ID='Sd1' /
&VENT ID='Fan_1', XB=5.000,6.000,11.000,12.000,7.134,7.134, SURF_ID='Supply', 
      DEVC_ID='Sd1' /
&VENT ID='Fan_2', XB=5.000,6.000,32.000,33.000,7.134,7.134, SURF_ID='Supply',
      DEVC_ID='Sd1' /
...
```

### `XB` set to `Edges` ###

BlenderFDS calculates the end points global coordinates of the Blender `object` `edges`. The resulting coordinates are exported as `XB` parameters of many FDS namelist group, one for each `edge`.

For example, `XB` set to `Edges` setting can be used to describe a group of beam detectors, sharing the same parameters. The user creates an `object` made of independent `edges` distributed inside the building, and obtains a series of `DEVCs`:

```
&DEVC ID='Beam detectors_0', XB=0.029,-1.271,-1.235,1.307,2.500,2.500,
      QUANTITY='PATH OBSCURATION', SETPOINT=0.33 , FYI='Two detectors' /
&DEVC ID='Beam detectors_1', XB=1.217,-1.271,0.043,1.307,2.500,2.500,
      QUANTITY='PATH OBSCURATION', SETPOINT=0.33 , FYI='Two detectors' /
...
```

## `XYZ` parameter ##

| **Blender `object` `XYZ` set to** | **Exported as** | **Number of FDS namelist groups** |
|:----------------------------------|:----------------|:----------------------------------|
| None                              | `XYZ` not set   | None                              |
| Verts                             | Vertices        | Vertices, one for each vertex of the Blender `object` |
| Center                            | Center          | Only one                          |

### `XYZ` set to `None` ###

No `XYZ` parameter is added to the exported namelist group.

### `XYZ` set to `Verts` ###

BlenderFDS calculates the global coordinates of the Blender `object` `vertices`. The resulting coordinates are exported as `XYZ` parameters of many FDS namelist group, one for each `vertex`.

For example, `XYZ` set to `Verts` setting can be used to describe a group of thermocouples, sharing the same parameters. The user creates an `object` made of independent `vertices` distributed inside the building, and obtains a series of `DEVCs` like this:

```
&DEVC ID='Thermocouple serie_0', XYZ=-0.000,0.000,0.100, QUANTITY='THERMOCOUPLE' /
&DEVC ID='Thermocouple serie_1', XYZ=-0.000,0.000,0.400, QUANTITY='THERMOCOUPLE' /
&DEVC ID='Thermocouple serie_2', XYZ=-0.000,0.000,0.700, QUANTITY='THERMOCOUPLE' /
&DEVC ID='Thermocouple serie_3', XYZ=-0.000,0.000,1.000, QUANTITY='THERMOCOUPLE' /
&DEVC ID='Thermocouple serie_4', XYZ=-0.000,0.000,1.300, QUANTITY='THERMOCOUPLE' /
&DEVC ID='Thermocouple serie_5', XYZ=-0.000,0.000,1.600, QUANTITY='THERMOCOUPLE' /
...
```

### `XYZ` set to `Center` ###

BlenderFDS calculates the global coordinates of the Blender `object` `center`. The resulting coordinates are exported as `XYZ` parameter of one only FDS namelist group.

The `object` `center` is the small dot that appears when the Blender `object` is selected in `object mode`. It is the `object` local reference system origin.

## `PB*` parameter ##

| **Blender `object` `PB*` set to** | **Exported as** | **Number of FDS namelist groups** |
|:----------------------------------|:----------------|:----------------------------------|
| None                              | `PB*` not set   | None                              |
| Faces                             | Planes          | Planes, one for each `face` of the Blender `object` |

### `PB*` set to `None` ###

No `PBX, PBY, PBZ` parameter is added to the exported namelist group.

### `PB*` set to `Faces` ###

BlenderFDS calculates the bounding box in global coordinates of the Blender `object` `faces`. Each `face` is flattened, and its edges straightened. The result is a group of right plane faces with edges parallel to the global axis. Each `face` is replaced by a plane perpendicular to one global axis, as required by FDS. The resulting coordinates are exported as `PBX, PBY, PBZ` parameters of many FDS namelist group, one for each `face`.

Of course. it is much more clean and less prone to errors to directly model "straight" `faces`, acceptable by FDS as planes without transformation.

For example, this `PB*` setting can be used to input several `SLCFs` that share the same parameters.

The user creates an `object` made of separate `faces` distributed inside the building, and obtains a series of `SLCFs`:

```
&SLCF QUANTITY='TEMPERATURE', VECTOR=.TRUE., PBX=0.000 /
&SLCF QUANTITY='TEMPERATURE', VECTOR=.TRUE., PBY=0.600 /
...
```

Here is an example of a `SLCF object` using `PB*` set to faces:

![https://lh4.googleusercontent.com/-xtrib3VKxi4/UDOtKEowqdI/AAAAAAAAAoA/Eu1USS_LK_w/s411/SLCF.png](https://lh4.googleusercontent.com/-xtrib3VKxi4/UDOtKEowqdI/AAAAAAAAAoA/Eu1USS_LK_w/s411/SLCF.png)

## Setting `XB, XYZ, PB*` at the same time ##

The user can set both `XB, XYZ, PB*` at the same time: the affected namelist group receives both parameters.

However some combinations are not allowed. When a conflicting combination is entered, the user interface shows an error message. It is up to the user to set a safe value. The conflicting settings are those that require multiple namelist groups more than once. For example, `XB` set to `Voxels` and `XYZ` set to `Verts`. Conversely `XB` set to `Voxels` and `XYZ` set to `Center` are compatible settings.

# Copying FDS parameters and geometry from Blender active object to other objects #

After setting up FDS parameters and geometry for a single Blender object, the user can easily copy those settings to other Blender objects.

Select the destination objects in Blender [3D view editor](BlenderFDS_UI#The_3D_view_editor.md) or [outliner editor](BlenderFDS_UI#The_outliner_editor.md). The last selected object becomes the active object. The active object is outlined in yellow, the other selected objects are outlined in orange. The current active object is used as source for copying.

![http://wiki.blender.org/uploads/a/a9/25-Manual-Object-Selection-001.png](http://wiki.blender.org/uploads/a/a9/25-Manual-Object-Selection-001.png)

Push the `To Selected Objects` button at the bottom of the `object properties panel`. All the FDS parameters and geometry of the active object are copied to the selected objects.

![https://lh5.googleusercontent.com/-stwpQ1gY0yk/TwGFAPzfssI/AAAAAAAAAgw/-w1giZUZ5eU/s378/ToSelectedObjects.png](https://lh5.googleusercontent.com/-stwpQ1gY0yk/TwGFAPzfssI/AAAAAAAAAgw/-w1giZUZ5eU/s378/ToSelectedObjects.png)

The copied parameters are independent from the source object parameters: a modification of the copied parameters does not influence the source object's parameters and vice versa.

If you need a stronger link between objects (inherited properties and shared geometry), see [Blender object duplication](BlenderScenesToFDSCases#Blender_file_contains_several_FDS_cases.md).