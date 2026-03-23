"""
Custom primitive objects for the libero_simple task suite.

These are simple geometric shapes (no scanned meshes) that are easier for
policies to manipulate and generalise from.
"""

import os
import pathlib
import numpy as np

from robosuite.models.objects import MujocoXMLObject

from libero.libero.envs.base_object import register_object

_ASSETS_DIR = pathlib.Path(__file__).parent.parent.parent / "assets" / "custom_objects"


class CustomPrimitiveObject(MujocoXMLObject):
    """Base class for custom primitive objects loaded from local XML assets."""

    def __init__(self, name, obj_name):
        super().__init__(
            str(_ASSETS_DIR / obj_name / f"{obj_name}.xml"),
            name=name,
            joints=[dict(type="free", damping="0.0005")],
            obj_type="all",
            duplicate_collision_geoms=True,
        )
        self.category_name = obj_name
        self.object_properties = {"vis_site_names": {}}
        # Keep objects upright; allow free spin around the vertical z-axis.
        self.rotation = (-np.pi, np.pi)
        self.rotation_axis = "z"


# ── Cubes ────────────────────────────────────────────────────────────────────

@register_object
class RedCube(CustomPrimitiveObject):
    """A solid red 5 cm cube."""

    def __init__(self, name="red_cube"):
        super().__init__(name, "red_cube")
        self.rotation = (-np.pi, np.pi)
        self.rotation_axis = "z"


@register_object
class GreenCube(CustomPrimitiveObject):
    """A solid green 5 cm cube."""

    def __init__(self, name="green_cube"):
        super().__init__(name, "green_cube")
        self.rotation = (-np.pi, np.pi)
        self.rotation_axis = "z"


@register_object
class BlueCube(CustomPrimitiveObject):
    """A solid blue 5 cm cube."""

    def __init__(self, name="blue_cube"):
        super().__init__(name, "blue_cube")
        self.rotation = (-np.pi, np.pi)
        self.rotation_axis = "z"


@register_object
class YellowCube(CustomPrimitiveObject):
    """A solid yellow 5 cm cube."""

    def __init__(self, name="yellow_cube"):
        super().__init__(name, "yellow_cube")
        self.rotation = (-np.pi, np.pi)
        self.rotation_axis = "z"


# ── Boxes ─────────────────────────────────────────────────────────────────────

class SimpleBox(CustomPrimitiveObject):
    """Base class for simple rectangular boxes with a contain_region site.

    The box is 12 cm × 12 cm × 7 cm with 1 cm walls.  Its interior is
    10 cm × 10 cm × 6 cm — large enough to hold the 5 cm cubes.
    The contain_region site drives the BDDL ``In`` predicate check.
    """

    def __init__(self, name, obj_name):
        super().__init__(name, obj_name)
        # Box must stay upright; randomise spin around z only.
        self.rotation = (0, 0)
        self.rotation_axis = "z"


@register_object
class BrownBox(SimpleBox):
    """A brown rectangular box."""

    def __init__(self, name="brown_box"):
        super().__init__(name, "brown_box")


@register_object
class BlueBox(SimpleBox):
    """A blue rectangular box."""

    def __init__(self, name="blue_box"):
        super().__init__(name, "blue_box")


@register_object
class GreenBox(SimpleBox):
    """A green rectangular box."""

    def __init__(self, name="green_box"):
        super().__init__(name, "green_box")


@register_object
class OrangeBox(SimpleBox):
    """An orange rectangular box."""

    def __init__(self, name="orange_box"):
        super().__init__(name, "orange_box")
