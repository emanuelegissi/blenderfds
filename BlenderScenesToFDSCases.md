| **Updated to 2.0** |
|:-------------------|

When exported, each Blender `scene` becomes an FDS case, that is an `.fds` text input file.




---


# Blender file contains several FDS cases #

In general, the user needs to simulate several scenarios with similar geometries and thermo-physical parameters. Only a small number of parameters are to be modified.
The user builds the geometry into a Blender `scene`. Then duplicates the `objects` in several new `scenes`:
  * the `objects` that do not change should be linked between the `scenes` to share exactly the same geometrical `mesh` and FDS parameters. If the user decides to modify the common geometry or the common thermo-physical parameters, all the linked `objects` from all `scenes` are modified accordingly. See http://wiki.blender.org/index.php/Doc:2.6/Manual/Modeling/Objects/Duplication for precisions.
  * depending on the scenarios, some `objects` from specific `scenes` must have their own geometry and thermo-physical parameters. The user unlinks them from the common properties and they become independent. Then the user can modify their parameters and geometry.

Each `scene` requires the user to enter several parameters in its `scene panel`:

![https://lh4.googleusercontent.com/-40Zud8q3xgw/UDOtLaVPZRI/AAAAAAAAAoU/LqzBns9vGTE/s800/case.png](https://lh4.googleusercontent.com/-40Zud8q3xgw/UDOtLaVPZRI/AAAAAAAAAoU/LqzBns9vGTE/s800/case.png)

## `CHID` and `TITLE` parameters ##

The `CHID` value is used as the default file name for the exported FDS input file. For this reason the requirements for the `CHID` string are more stringent: it shall be a valid filename. So no spaces are allowed.

The `CHID` and `TITLE` values are also used to insert an appropriate `HEAD` namelist group in that file. For example:

```
&HEAD CHID='uni-build-s1', TITLE='University building, scenario 1' /
```

## Case `Directory` ##

The case `Directory` is the default directory where the single FDS input file is exported. Each `scene` can be exported to a different FDS input file stored in its particular directory. Each FDS simulation store its output files in its directory and they do not get mixed with other simulation results.

## `Config File` ##

If `Auto Config` is chosen, an empty default configuration is automatically included in the FDS input file. This is often used to check the geometry.

If `Config File` is chosen, BlenderFDS includes the specified `Config File` verbatim at the beginning the exported FDS input file. The configuration file is a text file used to specify the non-geometrical FDS namelist groups, commonly edited with the user-preferred text editor. Beware that BlenderFDS performs no sanity check to the configuration file syntax and semantic.

A typical configuration file may contain the following parameters:

```
&TIME T_END=900.0 /

&REAC ID='polyurethane', SOOT_YIELD=0.1875, CO_YIELD=0.02775,
      C=1.0, H=1.75, O=0.25, N=0.065,
      HEAT_OF_COMBUSTION=25300., IDEAL=.TRUE. /
      Gas phase reaction: polyurethane flexible foam (means) from
      Tewarson SFPE Handbook 3rd ed,
      SFPE handbook table 3-4.14, p. 3-112.

&MATL ID='Gypsum plaster', CONDUCTIVITY=0.48,
      SPECIFIC_HEAT=0.84, DENSITY=1440. /
      Thermo-physical properties of gypsum plaster.

&PROP ID='acme smoke detector', QUANTITY='CHAMBER OBSCURATION',
      LENGTH=1.8, ACTIVATION_OBSCURATION=3.28 /
      
&ISOF QUANTITY='TEMPERATURE', VALUE(1)=60. /
&ISOF QUANTITY='VISIBILITY', VALUE(1)=10. /
&BNDF QUANTITY='ADIABATIC SURFACE TEMPERATURE' /
```

## `Voxel Size` ##

| **New in 2.0**: voxel size is set on a per-object basis |
|:--------------------------------------------------------|

The `Voxel Size` is not any more set in the `scene` panel.
See [BlenderObjectsToFDSNamelistGroups#XB\_parameter](BlenderObjectsToFDSNamelistGroups#XB_parameter.md) for a detailed description.

# Exporting current Blender `scene` to an FDS input file #

Eventually the Blender `scene` is ready, the building geometry is modeled, the boundary conditions are assigned, the configuration file is prepared.

The user selects the `File > Export > FDS Case (.fds)` menu and exports the current Blender `scene` to an FDS input file. The input file receives the default name entered in the `CHID` field of the `scene panel`, and is saved in the default case `Directory`.

![https://lh5.googleusercontent.com/_iTIkwVoSUm0/TXeImWooLdI/AAAAAAAAAb8/TsWMxOZUrS8/s720/blender%20export%20menu.png](https://lh5.googleusercontent.com/_iTIkwVoSUm0/TXeImWooLdI/AAAAAAAAAb8/TsWMxOZUrS8/s720/blender%20export%20menu.png)

To specify a different location to save the export file, click on the desired path in the file browser pane, then specify a file name.

In the file browser window, the user can also prefer to 'Export Visible Objects' only. This can be useful while debugging the exported geometry in Smokeview.

When exporting large files, the Blender user interface can _freeze_ for several minutes while the process advances. This is an issue with current Blender version that hopefully will be resolved in the near future. Note: for a relatively complex building such as the example case, the export process may take up to 3 minutes.

Here's the export result of the example case building as viewed in Smokeview:

![http://lh3.ggpht.com/_iTIkwVoSUm0/TA1Q8isrsyI/AAAAAAAAAUw/Dp16RUJY8sQ/fds_case1.jpg](http://lh3.ggpht.com/_iTIkwVoSUm0/TA1Q8isrsyI/AAAAAAAAAUw/Dp16RUJY8sQ/fds_case1.jpg)

Monitoring the terminal window the user can follow the advancement of the exporting procedure:

![https://lh3.googleusercontent.com/_iTIkwVoSUm0/TXeJfZi6V9I/AAAAAAAAAcE/VP_Q1mU3PBE/terminal%20exporting%20fds%20case.png](https://lh3.googleusercontent.com/_iTIkwVoSUm0/TXeJfZi6V9I/AAAAAAAAAcE/VP_Q1mU3PBE/terminal%20exporting%20fds%20case.png)