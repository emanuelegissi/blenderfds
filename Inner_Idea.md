# The idea behind BlenderFDS #


---


## Blender data files have a hierarchical structure ##

Each Blender file contains a database of geometric features. This database contains all the `scenes`, `objects`, `meshes`, `materials`, `textures` etc. that are described in the Blender file and shown in Blender UI. A file can contain multiple `scenes`, and each `scene` can contain multiple `objects`. `Objects` are composed by `meshes` and can contain multiple `materials`, which in turn can contain many `textures`.

The following example outliner panel shows this kind of data organization:

![http://blenderfds.googlecode.com/svn/wiki/images/outliner/generic_window.png](http://blenderfds.googlecode.com/svn/wiki/images/outliner/generic_window.png)

## Blender entities: `scenes`, `objects`, `meshes`, `materials` ##

A Blender `scene` is a collection of `objects`. `Object` properties are manipulated in `Blender Object mode`.

Each Blender `object` groups:
  * its `mesh`, the shape of the `object`,
  * its `material`, the aspect of its surface (color, transparency...),
  * the `texture` applied to its `material`,
  * other `objects` by the parenting feature.

A Blender `mesh` is a collection of faces, edges, and vertices which can be modeled and manipulated in `Blender Edit Mode`. The Blender `mesh` is not to be confused with an FDS `MESH`. In fact, a Blender `mesh` is only a volume or a surface defined by vertices, edges and faces: it is the geometric description of the parent `object`.

A `vertex` is a 3-dimensional coordinate, representing a point in space. An `edge` is a straight, wire-like line representing the boundary of 2 adjacent vertices. A `face` is a planar connection of edges representing a boundary, field, or solid surface. Faces are always flat. Edges are always straight. An edge is formed by the intersection of 2 faces. Vertices are formed by the intersection of 3 or more faces. For example, a cube has 6 faces, 12 edges and 8 vertices.

## Every Blender entity can be duplicated and linked to several parents ##

It is also possible to create links between different Blender entities, so that they share some information. For example, if you have a car `mesh`, you can use that car `mesh` for six cars in a parking lot scene. If you modify the original car `mesh`, then all the six cars of the parking lot inherit that modification.

![http://blenderfds.googlecode.com/svn/wiki/images/geometry/faces_edges_vertices.png](http://blenderfds.googlecode.com/svn/wiki/images/geometry/faces_edges_vertices.png)

## FDS input file ##

FDS input is a single text file. Input data is specified by namelist groups:

![http://blenderfds.googlecode.com/svn/wiki/images/syntax/commented_command.png](http://blenderfds.googlecode.com/svn/wiki/images/syntax/commented_command.png)

Namelist groups are used to describe every aspect of the fire simulation: simulation name, duration, computational domain, geometry, boundary conditions, materials, output quantities, control logic...

## Geometric entities ##

Many namelist groups extend their action in the computational space to volumes, faces, segments, points, or planes:

![http://blenderfds.googlecode.com/svn/wiki/images/geometry/geometric_entities.png](http://blenderfds.googlecode.com/svn/wiki/images/geometry/geometric_entities.png)

The simulated-ambient geometric description is entered line by line; the geometric entities are defined in each namelist group by the `XB, XYZ, PBX, PBY, PBZ` parameters.

FDS uses an absolute global reference coordinate system, that conforms to the right hand rule. By default, the z axis is considered the vertical. FDS employs the units of measurement from the International System (SI). Lengths are expressed in _m_.



### Faces ###

A **face** is represented by a right plane face with edges parallel to the axis. Its position and dimensions are described by the coordinates of two opposite vertices, that must lie on the same plane. For example:

```
&VENT XB=0.5,1.1,2.0,3.1,-2.0,-2.0, SURF_ID='fire' /`
```

uses the parameter `XB` to define a flat face perpendicular to the z axis imposing a particular boundary condition over a solid. Two of the six coordinates are the same, denoting a flat face as opposed to a solid.

### Segments ###

A **segment** is bounded by two end points. If point A=(xA, yA, zA) and point B=(xB, yB, zB) are the end points, its coordinates are entered following the same convention valid for volumes. For example,

```
&DEVC XB=0.5,1.5,2.0,3.5,-2.0,0., QUANTITY='PATH OBSCURATION', ID='beam1', SETPOINT=0.33 /
```

is a beam smoke detector between (0.5,2.0,-2.0) and (1.5,3.5,0.) end points.

### Points ###

A **point** is simply identified by its 3 coordinates. For example, the line:

```
&DEVC XYZ=2.,3.,4., QUANTITY='THERMOCOUPLE', ID='termo1' /
```

uses the parameter `XYZ` to insert a thermocouple at the point of coordinates (2.,3.,4.).

### Planes ###

A **plane** is represented by a right plane perpendicular to one of the reference axis. For example, these lines:

```
&SLCF PBX=0.5, QUANTITY='TEMPERATURE' /
```

is a plane perpendicular to the x axis and intersecting its point (.5,0.,0.).

```
&SLCF PBY=1.5, QUANTITY='TEMPERATURE' /
```

is a plane perpendicular to the y axis and intersecting its point (0.,1.5,0.).

```
&SLCF PBZ=-.5, QUANTITY='TEMPERATURE' /
```

is a plane perpendicular to the z axis and intersecting its point (0.,0.,-.5).

All use the parameters `PBX, PBY, PBZ` to specify the coordinate in the direction of the perpendicular axis.

## BlenderFDS links Blender entities to FDS namelist groups ##

| **Blender** | **FDS** |
|:------------|:--------|
| Each file   | One or more FDS input files |
| Each `scene`  | A case (one FDS input file, with header namelists as `HEAD, TIME, MISC, DUMP, REAC,`...) |
| Each `object` | One or more namelist groups (`OBST, DEVC, VENT, HOLE, SLCF, `...) |
| Each `material` | One `SURF` namelist group |

## Each Blender `scene` is an FDS case ##

Each Blender `scene` can be exported to an `.fds` text input file. A single Blender file can contain several `scenes`, thus several FDS cases, one for each simulated scenario.

For example, the same parking lot can be duplicated in several `scenes`. The geometrical `meshes` and the thermo-physical parameters of the cars can be shared between all the cars in all the `scenes`; the position of the cars in the single `scenes` can be varied according to the simulated scenario.

## Each Blender `object` and its `material` are exported as one or more FDS namelist group ##

Each Blender `object` is linked to one or more FDS namelist groups. The exported namelist groups extend their action to the geometry covered by the Blender `object mesh`.

For example:

![http://blenderfds.googlecode.com/svn/wiki/images/screen/idea_1.png](http://blenderfds.googlecode.com/svn/wiki/images/screen/idea_1.png)

That yellow Blender _Wall_ `object` is exported as many `OBST` namelist groups that describe the round and carved geometry of the wall.

The Blender material linked to the _Wall_ `object` is named _Gypsum wall_ and rendered in yellow color. The _Gypsum wall_ Blender material is exported as an FDS `SURF` namelist containing all the user entered parameters:

![http://blenderfds.googlecode.com/svn/wiki/images/screen/idea_2.png](http://blenderfds.googlecode.com/svn/wiki/images/screen/idea_2.png)

In particular, the Blender _Wall_ `object`, and its _Gypsum wall_ `material` are exported to the FDS input file as an obstacle, and its boundary condition:

```
&SURF ID='Gypsum wall', RGB=204,199,56, MATL_ID='Gypsum plaster', THICKNESS=0.03 /

&OBST ID='Wall_0', XB=-1.575,-1.375,-1.375,-0.475,-0.025,1.975, SURF_ID='Gypsum wall',
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

These entities are visualized in Smokeview as a yellow round obstacle:

![http://blenderfds.googlecode.com/svn/wiki/images/screen/idea_3.png](http://blenderfds.googlecode.com/svn/wiki/images/screen/idea_3.png)