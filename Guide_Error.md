# Error management #


---


Whenever BlenderFDS encounters a problem in user data, an error message appears nearby the offending input:

![http://blenderfds.googlecode.com/svn/wiki/images/panel/errors.png](http://blenderfds.googlecode.com/svn/wiki/images/panel/errors.png)

Any error prevents the parent namelist from being fully exported to the FDS case file.

Sometimes errors cannot be immediately detected, often because an heavy calculation process is required to discover the problem. These kind of calculations are performed only during exporting and importing operations.

If errors are discovered during such operations a popup message warns the user and:
  * on file _export_, error messages are collected into the exported FDS case file.
  * on file _import_, error messages are collected into the [free text file](Guide_Common#Free_text_file.md).
