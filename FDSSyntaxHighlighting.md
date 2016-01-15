Syntax highlighting is a feature of some text editors that display text in different colors and fonts according to the category of terms. This page lists various sources for FDS syntax highlighting applied to text editors.

![https://lh5.googleusercontent.com/_iTIkwVoSUm0/TXeUFa-EkjI/AAAAAAAAAcQ/CBnI6aioMaI/s512/gedit%20syntax%20high.png](https://lh5.googleusercontent.com/_iTIkwVoSUm0/TXeUFa-EkjI/AAAAAAAAAcQ/CBnI6aioMaI/s512/gedit%20syntax%20high.png)




---


# Gedit text editor #

Gedit is the official text editor of the Gnome desktop environment, that comes preinstalled in many Linux distributions.

Download Gedit for Linux, Mac OSX, and MS Windows from: http://projects.gnome.org/gedit/index.html

Download the plugin from [link](http://code.google.com/p/blenderfds/downloads/detail?name=gedit_fds_20120326.zip&can=2&q=)

This plugin is released under the GNU General Public License (GPL).

Extract the zipped file and copy its contents to the following directory: `~/.local/share/`. Now you can run the `gedit` editor.

# Notepad++ text editor #

Download Notepad++ for MS Windows from: http://notepad-plus-plus.org/

Download the plugin from: http://code.google.com/p/blenderfds/downloads/list

This plugin is released under the GNU General Public License (GPL) by Dipl.-Ing. M.Kitzlinger, Technische Universitaet Darmstadt, Institut fuer Numerische Methoden und Informatik im Bauwesen,

To install it:

  1. Open Notepad++
  1. Open the User-Defined Dialog e.g. via View-menu.
  1. Press import-button and select the downloaded file.
  1. Restart Notepad++

# Vim text editor #

Vim is a highly configurable text editor built to enable efficient text editing. It is an improved version of the vi editor distributed with most UNIX systems.

Download Vim from: http://www.vim.org

Here is a syntax highlighting building script provided by Andrew Louie: https://sites.google.com/site/louiea/vimsyntaxfileforfds

If you use Vim, you do not need too many explanations... ;-)

# Fraise (former Smultron) text editor #

This plugin updates the list of Fraise syntax definitions. Do not hesitate to contact its developer in case of problems: [parsipal@gmail.com](mailto:parsipal@gmail.com).

Download Fraise for Mac OSX from: http://www.fraiseapp.com/

Download the plugin from:
  * FDS 5.5.0 keywords: [Smultron\_SHxFDS5.5.x.zip](http://www.tidestudio.com/DOWNLOAD/Smultron_SHxFDS5.5.x.zip)
  * FDS 5.4.x keywords: [Smultron\_SHxFDS5.4.x.zip](http://www.tidestudio.com/DOWNLOAD/Smultron_SHxFDS5.4.x.zip)

This plugin is released under the GNU General Public License (GPL).

To install it:
  1. Download and install Fraise text editor.
  1. Quit Fraise before start installation process.
  1. `Finder > Go > Application > Fraise.app`, then right click on it and choose `explore contained`.
  1. Open the `Resource` directory;
  1. Overwrite the `SyntaxDefinitions.plist`;
  1. Open `Syntax Definitions` directory;
  1. Copy `fds.plist` into it;
  1. Now start Fraise and load any FDS input file.