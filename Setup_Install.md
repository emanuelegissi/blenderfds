# Install BlenderFDS #


---


## First, get Blender ##

[Download](http://www.blender.org/) the appropriate Blender package for your platform and install it on your computer:

  * The _Microsoft Windows_ Blender package comes with an optional self-extracting installer.

  * For other operating systems (_Linux, Mac OS X..._) you can unpack the downloaded compressed file to the location of your choice. Provided the Blender binary is in the original extracted directory, Blender will run straight out of the box. No system libraries or system preferences are altered.

Launch Blender executable and check that it works correctly.

| BlenderFDS shall be installed on the right Blender version, as specified in the release notes of the downloaded package. It does not work with older versions and it is not guaranteed to work with newer ones. |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Then, install BlenderFDS add-on into Blender ##

[Download](Setup_Download.md) the latest BlenderFDS distribution package and unzip it in a comfortable location.

After launching the Blender executable, open the the Blender `Add-Ons` panel using the `File > User Preferences` menu and clicking on the `Add-Ons` tab (1). The following window tab opens up:

![http://blenderfds.googlecode.com/svn/wiki/images/install/1.png](http://blenderfds.googlecode.com/svn/wiki/images/install/1.png)

For a script to show up in the `Add-ons` panel it first has to be installed. Click the `Install Add-On` button (2).

A file browser window opens up.

![http://blenderfds.googlecode.com/svn/wiki/images/install/3.png](http://blenderfds.googlecode.com/svn/wiki/images/install/3.png)

Locate and select the `blenderfds.zip` (3) file inside the BlenderFDS distribution package that you just downloaded and unzipped. Click the file browser `Install Add-On` button (4). Blender automatically unzips the BlenderFDS add-on and copies its content to its local `addons/blenderfds` directory.

Once installed, the add-on shows up in the `Add-ons` panel. By checking the `Enable Add-on` checkbox (5), you can activate its functionalities:

![http://blenderfds.googlecode.com/svn/wiki/images/install/5.png](http://blenderfds.googlecode.com/svn/wiki/images/install/5.png)

Finally, click on the `Save As Default` button (6) to complete the installing procedure and make the installation permanent.

BlenderFDS is ready to use.