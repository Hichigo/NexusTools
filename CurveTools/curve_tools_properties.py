import bpy
from bpy.types import PropertyGroup
from bpy.props import BoolProperty, IntProperty, EnumProperty, PointerProperty

from .curve_tools_utils import filter_on_curve_type

class CurveTools_SCENE_Properties(PropertyGroup):

	num_copy: IntProperty(
		name="Copy number",
		description="Number copy active object",
		min=2,
		default=5
	)

	target_curve: PointerProperty(
		name="Target curve",
		description="Chose curve object",
		type=bpy.types.Object,
		poll=filter_on_curve_type
	)

	follow_curve: BoolProperty(
		name="Follow curve",
		description="Object follow by curve",
		default=False
	)

	curve_radius: BoolProperty(
		name="Curve radius",
		description="Apply radius curve to object",
		default=False
	)

	forward_axis: EnumProperty(
		name="Forward axis",
		items=[
			("FORWARD_X", "X", "", 0),
			("FORWARD_Y", "Y", "", 1),
			("FORWARD_Z", "Z", "", 2),
			("TRACK_NEGATIVE_X", "-X", "", 3),
			("TRACK_NEGATIVE_Y", "-Y", "", 4),
			("TRACK_NEGATIVE_Z", "-Z", "", 5)
		],
		default = "FORWARD_X"
	)

	up_axis: EnumProperty(
		name="Up axis",
		items=[
			("UP_X", "X", "", 0),
			("UP_Y", "Y", "", 1),
			("UP_Z", "Z", "", 2)
		],
		default = "UP_Z"
	)