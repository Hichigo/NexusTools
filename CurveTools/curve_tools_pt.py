import bpy
from bpy.types import Panel


class VIEW3D_PT_CurveTools(Panel):
	"""Curve tools panel"""
	bl_label = "Curve Tools"
	bl_idname = "VIEW3D_PT_CurveTools"
	bl_space_type = 'VIEW_3D'
	bl_region_type = 'UI'
	bl_category = "Nexus"
	bl_parent_id = "VIEW3D_PT_NexusToolsMainPanel"
	bl_options = {"DEFAULT_CLOSED"}

	def draw(self, context):
		layout = self.layout

		col = layout.column()
		col.label(text="Curve tools panel")