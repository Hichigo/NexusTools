import bpy

from bpy.types import Operator


class VIEW3D_OT_SelectedToCurve(Operator):
	"""Set selected objects to curve"""
	bl_idname = "view3d.selected_to_curve"
	bl_label = "Selected To Curve"


	def invoke(self, context, event):
		selected_objects = context.selected_objects
		num_objects = len(selected_objects)

		if num_objects == 0:
			self.report({"ERROR"}, "No selected objects!")
			return {"FINISHED"}
		
		return self.execute(context)


	def execute(self, context):
		curve_tools = context.scene.curve_tools
		target_curve = curve_tools.target_curve
		follow_curve = curve_tools.follow_curve
		curve_radius = curve_tools.curve_radius
		forward_axis = curve_tools.forward_axis
		up_axis = curve_tools.up_axis

		selected_objects = context.selected_objects
		num_objects = len(selected_objects)
		
		delta_offset = 1 / (num_objects - 1)
		i = 0
		for ob in selected_objects:
			ob.location = (0, 0, 0)
			fp = ob.constraints.new(type="FOLLOW_PATH")
			fp.target = target_curve
			fp.use_fixed_location = True
			fp.use_curve_follow = follow_curve
			fp.use_curve_radius = curve_radius
			fp.forward_axis = forward_axis
			fp.up_axis = up_axis

			constrain = ob.constraints[0]
			if i == 0:
				constrain.offset_factor = 0
			else:
				constrain.offset_factor = delta_offset * i
			i += 1

		return {"FINISHED"}

class VIEW3D_OT_CopyToCurve(Operator):
	"""Set copy active object to curve"""
	bl_idname = "view3d.copy_to_curve"
	bl_label = "Copy Active To Curve"

	def execute(self, context):
		return {"FINISHED"}



# for s in spheres:
#     sc = s.constraints[0]
#     s.matrix_world = s.matrix_world
#     print(s.location)
#     s.constraints.remove(sc)