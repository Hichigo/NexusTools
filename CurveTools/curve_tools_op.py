import bpy

from bpy.types import Operator


class VIEW3D_OT_SelectedToCurve(Operator):
	"""Set selected objects to curve"""
	bl_idname = "view3d.selected_to_curve"
	bl_label = "Selected To Curve"

	def invoke(self, context, event):
		curve_tools = context.scene.curve_tools
		target_curve = curve_tools.target_curve
		selected_objects = context.selected_objects
		num_objects = len(selected_objects)

		if target_curve == None:
			self.report({"ERROR"}, "Please set Target curve!")
			return {"FINISHED"}

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
			# function?
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

	def invoke(self, context, event):
		curve_tools = context.scene.curve_tools
		target_curve = curve_tools.target_curve
		active_object = context.active_object

		if target_curve == None:
			self.report({"ERROR"}, "Please set Target curve!")
			return {"FINISHED"}

		if active_object == None:
			self.report({"ERROR"}, "No active object!")
			return {"FINISHED"}
		
		return self.execute(context)

	def execute(self, context):
		curve_tools = context.scene.curve_tools
		target_curve = curve_tools.target_curve
		follow_curve = curve_tools.follow_curve
		curve_radius = curve_tools.curve_radius
		forward_axis = curve_tools.forward_axis
		up_axis = curve_tools.up_axis
		num_copy = curve_tools.num_copy
		
		active_object = bpy.context.active_object
		active_object.location = (0, 0, 0)

		# function?
		fp = active_object.constraints.new(type="FOLLOW_PATH")
		fp.target = target_curve
		fp.use_fixed_location = True
		fp.use_curve_follow = follow_curve
		fp.use_curve_radius = curve_radius
		fp.forward_axis = forward_axis
		fp.up_axis = up_axis

		constrain = active_object.constraints[0]
		constrain.offset_factor = 0
		
		col = active_object.users_collection[0]

		delta_offset = 1 / (num_copy - 1)
		for i in range (1, num_copy):
			new_obj = active_object.copy()
			new_obj.data = active_object.data
			new_obj.animation_data_clear()
			col.objects.link(new_obj)

			constrain = new_obj.constraints[0]
			constrain.offset_factor = delta_offset * i

		return {"FINISHED"}



# for s in spheres:
#     sc = s.constraints[0]
#     s.matrix_world = s.matrix_world
#     print(s.location)
#     s.constraints.remove(sc)