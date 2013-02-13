# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 3
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####
"""BlenderFDS, an open tool for the NIST Fire Dynamics Simulator"""

bl_info = {
    "name": "BlenderFDS",
    "author": "Emanuele Gissi",
    "version": (2, 0, 1),
    "blender": (2, 6, 4),
    "api": 35622,
    "category": "Export",
    "location": "File > Export > FDS Case (.fds)",
    "description": "BlenderFDS, an open graphical editor for the NIST Fire Dynamics Simulator",
    "warning": "",
    "wiki_url": "http://www.blenderfds.org/",
    "tracker_url": "http://code.google.com/p/blenderfds/issues/list",
    "support": "COMMUNITY",
    "category": "Import-Export",
}

### To support reload properly, try to access a package var, if it's there, reload everything

if "bpy" in locals():
    import imp
    imp.reload(bf_config)
    imp.reload(bf_ui)
    imp.reload(bf_operators)
    imp.reload(bf_export)
    imp.reload(bf_geometry)
else:
    from . import bf_config
    from . import bf_ui
    from . import bf_operators
    from . import bf_export
    from . import bf_geometry

import bpy
from bpy.props import *
from bpy_extras.io_utils import ExportHelper
from os import path

### UI: Menu

class ExportFDS(bpy.types.Operator, ExportHelper):
    bl_label = "Export scene as FDS case"
    bl_idname = "export_scene.nist_fds"
    bl_description = "Export current Blender Scene as an FDS file"

    filename_ext = ".fds"
    filter_glob = StringProperty(default="*.fds", options={'HIDDEN'})
    
    def execute(self, context):
        # FIXME asincronous saving non blocking
        return bf_export.save(self, context, **self.as_keywords(ignore=("check_existing", "filter_glob")))

def menu_func_export(self, context):
    # Prepare default filepath
    filepath ="{0}.fds".format(path.splitext(bpy.data.filepath)[0])
    directory = path.dirname(filepath)
    basename = path.basename(filepath)
    # If the context scene contains path and basename, use them
    sc = context.scene
    if sc.bf_directory: directory = sc.bf_directory
    if sc.name: basename = "{0}.fds".format(bpy.path.clean_name(sc.name))
    # Call the exporter script
    filepath = "{0}/{1}".format(directory, basename)
    self.layout.operator(ExportFDS.bl_idname, text="Fire Dynamics Simulator Case (.fds)").filepath = filepath

### Registration/Unregistration

def register():
    bpy.utils.register_module(__name__)

    # scene properties
    bpy.types.Scene.bf_title = StringProperty(
        name="TITLE",
        description="Insert case description into TITLE parameter",
        maxlen=60)
    bpy.types.Scene.bf_directory = StringProperty(
        name="Directory",
        description="Case main directory",
        subtype="DIR_PATH")

    items_list = [("AUTO", "Auto Config", "Automatic basic configuration for non-geometric parameters"),
                  ("FILE", "Config File", "Use external configuration file to describe non-geometric parameters",)]
    bpy.types.Scene.bf_config_type = EnumProperty(
        name="Config Type",
        description="Configuration type of non-geometric parameters",
        items=items_list,
        default="AUTO")
    bpy.types.Scene.bf_config_filepath = StringProperty(
        name="Config File",
        description="Path to external configuration file describing non-geometric parameters",
        subtype="FILE_PATH",
        default="config.fds")
    bpy.types.Scene.bf_version = IntVectorProperty(
        name="Version",
        description="BlenderFDS version used for file creation and exporting",
        default=(0,0,0), size=3)
        # FIXME future versions are going to have: default=bl_info["version"])

    # object properties
    bpy.types.Object.bf_export = BoolProperty(
        name="Export",
        description="Export this Blender object to an FDS namelist",
        default=False)

    bpy.types.Object.bf_nl = StringProperty(
        name="Namelist",
        description="Namelist group name",
        default="OBST")

    items_list = [("NONE",   "None",   "None"),
                  ("VOXELS", "Voxels", "Voxelized solid"),
                  ("BBOX",   "BBox",   "Bounding box"),
                  ("FACES",  "Faces",  "Faces, one for each face of this object"),
                  ("EDGES",  "Edges",  "Segments, one for each edge of this object")]
    bpy.types.Object.bf_xb = EnumProperty(
        name="XB",
        description="Set XB parameter",
        items=items_list,
        default="BBOX")

    items_list = [("NONE",   "None",   "None"),
                  ("CENTER", "Center", "Point, corresponding to center point of this object"),
                  ("VERTS",  "Vertices",  "Points, one for each vertex of this object"),]
    bpy.types.Object.bf_xyz = EnumProperty(
        name="XYZ",
        description="Set XYZ parameter",
        items=items_list,
        default="NONE")
    
    items_list = [("NONE",   "None",   "None"),
                  ("FACES",  "Faces",  "Planes, one for each face of this object"),]
    bpy.types.Object.bf_pb = EnumProperty(
        name="PB*",
        description="Set PBX, PBY, PBZ parameters",
        items=items_list,
        default="NONE")
    
    bpy.types.Object.bf_voxel_size = FloatProperty(
        name="Voxel Size",
        description="Minimum resolution for object voxelization",
        step=1,precision=3,min=.01,max=2.,
        default=.10,
        update=bf_operators.update_voxels)

    bpy.types.Object.bf_sawtooth = BoolProperty(
        name="SAWTOOTH=.FALSE.",
        description="Set SAWTOOTH=.FALSE. parameter",
        default=False)
        
    bpy.types.Object.bf_thicken = BoolProperty(
        name="THICKEN=.TRUE.",
        description="Set THICKEN=.TRUE. parameter",
        default=False)
        
    bpy.types.Object.bf_ijk_n = IntVectorProperty(
        name="IJK",
        description="Number of cells in I, J, and K directions",
        default=(10,10,10), min=1, max=99999, size=3)

    bpy.types.Object.bf_fyi = StringProperty(
        name="FYI",
        description="Insert namelist description into FYI parameter",
        maxlen=60)

    bpy.types.Object.bf_custom_param = StringProperty(
        name="Custom Namelist Parameters",
        description="Custom parameters are appended verbatim to the namelist, use single quotes")

    bpy.types.Object.bf_is_voxels = BoolProperty(
        name="Voxel Object",
        description="This is a voxel temporary object",
        default=False)

    bpy.types.Object.bf_has_voxels_shown = BoolProperty(
        name="Voxels shown",
        description="This object voxels are currently being shown",
        default=False)

    # material properties
    bpy.types.Material.bf_export = BoolProperty(
        name="Export",
        description="Export this Blender material to an FDS SURF namelist",
        default=True)
        
    bpy.types.Material.bf_nl = StringProperty(
        name="Namelist",
        description="Namelist group name",
        default="SURF")
        
    bpy.types.Material.bf_fyi = StringProperty(
        name="FYI",
        description="Insert SURF description into FYI parameter",
        maxlen=60)
        
    bpy.types.Material.bf_custom_param = StringProperty(
        name="Custom SURF parameters",
        description="Custom parameters are appended verbatim to the namelist, use single quotes")

    # export menu
    bpy.types.INFO_MT_file_export.append(menu_func_export)

def unregister():
    bpy.utils.unregister_module(__name__)

    # scene properties
    del bpy.types.Scene.bf_title
    del bpy.types.Scene.bf_directory
    del bpy.types.Scene.bf_config_type
    del bpy.types.Scene.bf_config_filepath
    del bpy.types.Scene.bf_version

    # object properties
    del bpy.types.Object.bf_export
    del bpy.types.Object.bf_nl
    del bpy.types.Object.bf_xb
    del bpy.types.Object.bf_xyz
    del bpy.types.Object.bf_pb
    del bpy.types.Object.bf_voxel_size
    del bpy.types.Object.bf_sawtooth
    del bpy.types.Object.bf_ijk_n
    del bpy.types.Object.bf_fyi
    del bpy.types.Object.bf_custom_param
    del bpy.types.Object.bf_is_voxels
    del bpy.types.Object.bf_has_voxels_shown

    # material properties
    del bpy.types.Material.bf_export
    del bpy.types.Material.bf_nl
    del bpy.types.Material.bf_fyi
    del bpy.types.Material.bf_custom_param

    # export menu
    bpy.types.INFO_MT_file_export.remove(menu_func_export)

if __name__ == "__main__":
    register()
