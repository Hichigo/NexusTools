bl_info = {
	"name" : "Nexus Tools",
	"author" : "Nexus Studio",
	"version" : (0, 0, 1),
	"blender" : (2, 80, 0),
	"location" : "N menu",
	"description" : "",
	"warning" : "",
	"category" : "User"
}

import bpy

from bpy.types import Panel
# from bpy.props import StringProperty, BoolProperty, EnumProperty

class VIEW3D_PT_NexusToolsMainPanel(Panel):
	"""Main panel nexus tools"""
	bl_label = "Nexus Tools"
	bl_idname = "VIEW3D_PT_NexusToolsMainPanel"
	bl_space_type = 'VIEW_3D'
	bl_region_type = 'UI'
	bl_category = "Nexus"
	bl_options = {"DEFAULT_CLOSED"}

	def draw(self, context):
		layout = self.layout

		col = layout.column()
		col.label(text="Test text")



classes = (
	VIEW3D_PT_NexusToolsMainPanel,
)

def register():
	from bpy.utils import register_class
	for cls in classes:
		register_class(cls)

def unregister():
	from bpy.utils import unregister_class
	for cls in reversed(classes):
		unregister_class(cls)

if __name__ == "__main__":
	register()