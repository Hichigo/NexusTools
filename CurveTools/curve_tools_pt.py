import bpy
from bpy.types import Panel


class VIEW3D_PT_CurveTools(Panel):
	"""Curve tools panel"""
	bl_label = "Curve Tools"
	bl_idname = "VIEW3D_PT_CurveTools"
	bl_space_type = "VIEW_3D"
	bl_region_type = "UI"
	bl_category = "Nexus"
	bl_parent_id = "VIEW3D_PT_NexusToolsMainPanel"
	bl_options = {"DEFAULT_CLOSED"}

	def draw(self, context):
		layout = self.layout
		scene = context.scene
		curve_tools = scene.curve_tools

		col = layout.column()
		col.operator("view3d.selected_to_curve", text="Selected to curve", icon="CON_FOLLOWPATH")

		col = layout.column()
		col.operator("view3d.copy_to_curve", text="Copy to curve", icon="MOD_ARRAY")

		col = layout.column()
		col.prop_search(curve_tools, "target_curve", scene, "objects")
		box = col.box()
		box.label(text="Settings:")

		box.prop(curve_tools, "num_copy")

		box.prop(curve_tools, "follow_curve")
		box.prop(curve_tools, "curve_radius")
		
		row = box.row()
		row.label(text="Forward:")
		row.prop(curve_tools, "forward_axis", expand=True)
		
		row = box.row()
		row.label(text="Up:")
		row.prop(curve_tools, "up_axis", expand=True)