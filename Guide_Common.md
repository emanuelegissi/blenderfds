# Common aspects of the user interface #


---


## Export checkbox ##

The user decides which namelists and parameters are exported to the FDS case file by thicking the relevant export checkboxes:

![http://blenderfds.googlecode.com/svn/wiki/images/panel/export_namelist.png](http://blenderfds.googlecode.com/svn/wiki/images/panel/export_namelist.png)

When the namelist or the parameter is not to be exported, its user interface is greyed out.

## `FYI` data field ##

The `FYI` data field is used to comment the namelist group and can be recognized by the `info` icon.

![http://blenderfds.googlecode.com/svn/wiki/images/panel/FYI.png](http://blenderfds.googlecode.com/svn/wiki/images/panel/FYI.png)

The contents of the `FYI` data field are included in the parent namelist as this:

```
FYI='This is an example'
```

BlenderFDS enforces the following rules to prevent the creation of a malformed FDS case file:
  * `&` and `/` characters are not allowed,
  * no quote character is allowed.

## `Free text` data field ##

The free text data field is used to freely add any kind of FDS parameter to the parent namelist group. It can be recognized by the `notebook` icon.

![http://blenderfds.googlecode.com/svn/wiki/images/panel/Free_Parameters.png](http://blenderfds.googlecode.com/svn/wiki/images/panel/Free_Parameters.png)

In this case the `DEVC_ID='glass door breaker'` parameter is appended verbatim to the parent namelist, but no check is performed on the existance of the referred `DEVC`.

To add more parameters just separate them with spaces, eg.:

```
P1=3.14,2.11,2.34 P2='This is a string!' P3=.TRUE.
```

BlenderFDS knows nothing about what the user adds to free text data fields and does not check the validity of the input.

However BlenderFDS enforces the following rules to prevent the creation of a malformed FDS case file:
  * `&` and `/` characters are not allowed,
  * only single quote characters are allowed as string delimiters (eg. `P1='Right'`, `P2="Wrong"`),
  * single quote characters shall be properly matched (eg. `P1='Right'`, `P2='Not'right'`).

## `Free text` file ##

A free text file allows the user to freely enter multiline namelists. This is tipically used for namelist groups that have no geometric expression, eg. `ISOF, BNDF, PROP, MATL, ...`.

The free text file data field refers to a text that is included in the Blender file:

![http://blenderfds.googlecode.com/svn/wiki/images/panel/free_text_file.png](http://blenderfds.googlecode.com/svn/wiki/images/panel/free_text_file.png)

and that can be directly edited in the Blender text editor:

![http://blenderfds.googlecode.com/svn/wiki/images/panel/free_text_file_editor.png](http://blenderfds.googlecode.com/svn/wiki/images/panel/free_text_file_editor.png)

The entered text is appended as it is to the parent namelist. BlenderFDS knows nothing about what the user adds to the free text file and does not check at all the validity of the input.

| Handle this feature with care: it is possible to create **malformed** FDS case files! |
|:--------------------------------------------------------------------------------------|