# Blender materials to FDS SURFs #


---


## Default `SURF` panel ##

Blender materials are exported to FDS `SURFs` namelist groups. Generic `SURF` panel is reached by clicking on the following highlighted button of Blender property editor:

![http://blenderfds.googlecode.com/svn/wiki/images/panel/ma/get_ma.png](http://blenderfds.googlecode.com/svn/wiki/images/panel/ma/get_ma.png)

Here is the default `SURF` properties panel:

![http://blenderfds.googlecode.com/svn/wiki/images/panel/ma/SURF.png](http://blenderfds.googlecode.com/svn/wiki/images/panel/ma/SURF.png)

This displayed Blender material is going to be exported as:

```
&SURF ID='Hot wall' FYI='A fixed temperature boundary condition' RGB=255,140,0 TMP_FRONT=200. /
```

The dark orange color is translated to its RGB representation.

Some parameters are not going to be exported:
  * `TRANSPARENCY`, that is set to fully opaque, thus omitted;
  * `MATL_ID`, that has the exporting flag unchecked.

The `free text` parameter 'TMP\_FRONT=200.' is appended untouched to the namelist. The `free text` input box can be used to freely input the details of any kind of FDS `SURF` parameter, for more information on this type of data field see [`free text`](Guide_Common#Free_text_data_field.md).

## `<Assign to Selected Objects>` button ##

By clicking this button, the displayed material is assigned to all currently selected objects. This can be very useful when having to assign the same `SURF_ID` boundary condition to many objects.

## An example of a specialized `SURF` panel ##

Here is an example of a specialized `SURF` panel:

![http://blenderfds.googlecode.com/svn/wiki/images/panel/ma/SURF_burner.png](http://blenderfds.googlecode.com/svn/wiki/images/panel/ma/SURF_burner.png)

The displayed Blender material is going to be exported as:

```
&SURF ID='Burner' FYI='Est.d area...' HRRPUA=300.0 TAU_Q=-178.9 RGB=255,0,0 /
```

## `<Set t^2 Ramp>` button ##

By clicking this button, the user can calculate the appropriate `HRRPUA` and `TAU_Q` values for setting up the desired ramping up burner. The input values required for this calculation are:
  * the maximum total heat release rate (HRR) value,
  * the fire growth rate,
  * the reference HRR, be it for Eurocode or US ramp.

![http://blenderfds.googlecode.com/svn/wiki/images/panel/ma/SURF_burner_set_ramp.png](http://blenderfds.googlecode.com/svn/wiki/images/panel/ma/SURF_burner_set_ramp.png)

The burner area is estimated by summing the area of all the surfaces currently linked to this boundary condition; the resulting value is used to calculate the `HRRPUA` as the ratio of the maximum heat release rate and the estimated burner area.

| That burner area value shall be **double checked** by the savy user! |
|:---------------------------------------------------------------------|

In fact BlenderFDS cannot be exactly sure of where the fuel gas is going to be injected into the domain during the FDS simulation: if a surface is obstructed by another solid object, FDS is not going to inject fuel gas from there...

| If geometries are further modified and burner area changes, the calculated `HRRPUA` and `TAU_Q` values **are not automatically updated**. |
|:------------------------------------------------------------------------------------------------------------------------------------------|

## Predefined `SURFs` ##

When starting a new project, BlenderFDS automatically creates the following FDS predefined `SURF` namelists: `OPEN, INERT, MIRROR`. Obviously these namelists are not exported to the FDS case file.
