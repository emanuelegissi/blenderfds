# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 3
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

from . import bf_config, bf_geometry, bf_export
import bpy
from bpy.path import clean_name

# FIXME show bf_export in Blender outliner

### Various recurrent checks

def _detect_predefined_mas(context, layout):
    """Detect predefined entities and propose creation"""
    if not set(bf_config.mas_predefined) <= set(bpy.data.materials.keys()):
        row = layout.row()
        row.label(text="No FDS predefined SURFs", icon="ERROR")
        row.operator("material.bf_create_predefined", text="Create")

def _detect_old_bf_version_ijk(context, layout):
    """Detect old BlenderFDS file version and inform the user"""
    if tuple(context.scene.bf_version) < (2,0,0):
        row = layout.row()
        row.label(text="New: «IJK» replaces former «cell size» parameter", icon="HELP")

def _detect_old_bf_version_voxel_size(context, layout):
    """Detect old BlenderFDS file version and inform the user"""
    if tuple(context.scene.bf_version) < (2,0,0):
        row = layout.row()
        row.label(text="New: «voxel size» is now specific to each object", icon="HELP")

### UI: scene panel

class SceneButtonsPanel():
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "scene"

class SCENE_PT_bf(SceneButtonsPanel, bpy.types.Panel):
    bl_label = "FDS Case"
    
    def draw(self, context):
        layout = self.layout
        sc = context.scene
        
        # Case name
        row = layout.row()
        row.prop(sc, "name", text="CHID")
        if sc.name != clean_name(sc.name): 
            row.label(icon="ERROR")
        
        # Case title
        row = layout.row()
        row.prop(sc, "bf_title",)
        if bf_export.has_quotes(sc.bf_title): 
            row.label(icon="ERROR")
        
        # Case directory
        row = layout.row()
        row.prop(sc, "bf_directory")

        # Configuration
        row = layout.row()
        row.prop(sc, "bf_config_type", expand=True)
        if sc.bf_config_type == "FILE":
            row = layout.row()
            row.prop(sc, "bf_config_filepath")

        # Help message
        _detect_old_bf_version_voxel_size(context, layout)

### UI: object panel

class ObjectButtonsPanel():
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "object"
    
    @classmethod
    def poll(cls, context):
        ob = context.active_object
        return ob and ob.type == "MESH"

class OBJECT_PT_bf(ObjectButtonsPanel, bpy.types.Panel):
    bl_label = "FDS Object"

    def draw_header(self, context):
        layout = self.layout
        ob = context.active_object

        # Voxel temporary object
        if ob.bf_is_voxels:
            self.bl_label = "FDS (Temporary Object)"
            return

        # Export object to FDS
        layout.prop(ob, "bf_export", text="")

        # Object namelist description to panel title
        self.bl_label = "FDS {} ({})".format(ob.bf_nl, bf_config.nls.get(ob.bf_nl, "Unknown")) 

    def draw(self, context):
        layout = self.layout
        ob = context.active_object
        layout.active = ob.bf_export

        # Voxel temporary object
        if ob.bf_is_voxels:
            row = layout.row()
            row.operator("object.bf_hide_voxels")
            return

        # Init parameter choice from config and name
        bf_nl = ob.bf_nl
        nl_params = bf_config.nl_params.get(bf_nl,"")

        # Namelist
        row = layout.row()
        row.prop(ob, "bf_nl")
        if not bf_nl in bf_config.nls:
            row.label(icon="ERROR")

        # ID
        row = layout.row()
        row.active = "ID" in nl_params
        row.prop(ob, "name", text="ID")
        if bf_export.has_quotes(ob.name): 
            row.label(icon="ERROR")

        # FYI
        if "FYI" in nl_params:
            row = layout.row()
            row.prop(ob, "bf_fyi")
            if bf_export.has_quotes(ob.bf_fyi): 
                row.label(icon="ERROR")

        # Display as
        row = layout.row()
        row.prop(ob, "draw_type", text="Display as")
        row.prop(ob, "show_transparent", text="Show transparency")
                   
        # SURF_ID
        if "SURF_ID" in nl_params and ob.active_material and ob.active_material.bf_export:
            row = layout.row()
            row.label(text="SURF_ID='{0}'".format(ob.active_material.name))

        # IJK
        if "IJK" in nl_params:
            split = layout.row().split(percentage=.80)
            row1 = split.row()
            row1.prop(ob, "bf_ijk_n")
            row2 = split.row()
            row2.operator("object.bf_correct_ijk")
            row2.active = ob.bf_ijk_n[:] != bf_geometry.get_good_ijk(ob)
            layout.label(text="{0} cells, cell size is {1[0]:.3f} x {1[1]:.3f} x {1[2]:.3f}".format(bf_geometry.get_cell_number(ob), bf_geometry.get_cell_size(ob)))
            _detect_old_bf_version_ijk(context, layout)

        
        # Geometry
        row = layout.row()
        col1, col2, col3 = row.column(), row.column(), row.column()
        
        # XB
        col1.active = "XB" in nl_params
        col1.label(text="XB:")
        col1.prop(ob, "bf_xb", text="")
        
        # XYZ
        col2.active = "XYZ" in nl_params
        col2.label(text="XYZ:")
        col2.prop(ob, "bf_xyz", text="")
        
        # PB
        col3.active = "PB" in nl_params
        col3.label(text="PB*:")
        col3.prop(ob, "bf_pb", text="")

        # If XB, set voxel_size, show/hide voxels, check manifold, check size
        if ob.bf_xb == "VOXELS":
            row = layout.row()
            row.prop(ob, "bf_voxel_size")
            _detect_old_bf_version_voxel_size(context, layout)
            if ob.bf_has_voxels_shown:
                row.operator("object.bf_hide_voxels")
            else:
                row.operator("object.bf_show_voxels")
            if not bf_geometry.is_manifold(context, ob.data):
                row = layout.row()
                row.label(text="Object is non manifold", icon="ERROR")
                row.operator("object.bf_select_non_manifold")
            if bf_geometry.calc_remesh(context, max(ob.dimensions), ob.bf_voxel_size)[3]:
                row = layout.row()
                row.label(text="Object size too large, voxel size not guaranteed", icon="ERROR")
        
        # Check one only one multiple at a time
        if ob.bf_xb in ["VOXELS","FACES","EDGES"]:
            if ob.bf_xyz == "VERTS":
                row = layout.row()
                row.label(text="XB and XYZ conflicting", icon="ERROR")

            if ob.bf_pb  == "FACES":
                row = layout.row()
                row.label(text="XB and PB* conflicting", icon="ERROR")

        if ob.bf_xyz == "VERTS":
            if ob.bf_pb  == "FACES":
                row = layout.row()
                row.label(text="XYZ and PB* conflicting", icon="ERROR")

        # SAWTOOTH and THICKEN
        if "SAWTOOTH" in nl_params or "THICKEN" in nl_params:
            row = layout.row()
            if "SAWTOOTH" in nl_params:
                row.prop(ob, "bf_sawtooth", text='SAWTOOTH=.FALSE.')
            else:
                row.label(text=' ')
            if "THICKEN" in nl_params:
                row.prop(ob, "bf_thicken", text='THICKEN=.TRUE.')

        # Custom param
        col = layout.column()
        col.label(text="Custom {0} Parameters:".format(bf_nl))
        col.prop(ob, "bf_custom_param", text="")
        if bf_export.has_unmatched_quotes(ob.bf_custom_param): 
            col.label(text="Use matched single straight quotes", icon="ERROR")

        # Copy active object FDS properties to other selected objects  
        row = layout.row()
        row.label()
        row.operator("object.bf_fds_props_to_sel_obs")

### UI: material panel

class MaterialButtonsPanel():
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "material"

    @classmethod    
    def poll(cls, context):
        ma = context.material
        ob = context.active_object
        return ma and ob and ob.type == "MESH" and "SURF_ID" in bf_config.nl_params.get(ob.bf_nl,"") and not ob.bf_is_voxels

class MATERIAL_PT_bf(MaterialButtonsPanel, bpy.types.Panel):
    bl_label = "FDS Material"

    def draw_header(self, context):
        layout = self.layout
        ma = context.material
        
        # Export material to FDS
        layout.prop(ma, "bf_export", text="")
        
        # Object namelist description to panel title
        bf_nl = ma.bf_nl
        self.bl_label = "FDS {} ({})".format(bf_nl, bf_config.nls.get(bf_nl, "Unknown")) 

    def draw(self, context):
        layout = self.layout
        ma = context.material
        ob = context.active_object
        layout.active = ma.bf_export

        # Detect
        _detect_predefined_mas(context, layout)

        # Init parameter choice from config and name
        bf_nl = ma.bf_nl
        nl_params = bf_config.nl_params.get(bf_nl,"")

        # ID
        if "ID" in nl_params:
            row = layout.row()
            row.active = "ID" in nl_params
            row.prop(ma, "name", text="ID")
            if bf_export.has_quotes(ma.name): 
                row.label(icon="ERROR")

        # FYI
        if "FYI" in nl_params:
            row = layout.row()
            row.prop(ma, "bf_fyi")
            if bf_export.has_quotes(ma.bf_fyi):
                row.label(icon="ERROR")

        # RGB
        if "RGB" in nl_params:
            row = layout.row()
            row.active = "RGB" in nl_params
            row.prop(ma, "diffuse_color", text="RGB")

        # TRANSPARENCY
        if "TRANSPARENCY" in nl_params:
            row = layout.row()
            row.active = "TRANSPARENCY" in nl_params
            row.prop(ma, "use_transparency", text="TRANSPARENCY")
            row.prop(ma, "alpha")

        # Custom param
        col = layout.column()
        col.label(text="Custom {0} Parameters:".format(bf_nl))
        col.prop(ma, "bf_custom_param", text="")
        if bf_export.has_unmatched_quotes(ma.bf_custom_param): 
            col.label(text="Use matched single straight quotes", icon="ERROR")

