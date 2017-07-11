r"""Plain bearing generation"""

from ccad.model import cylinder

outer_diameter = {{ outer_diameter }}  # The outer diameter of the bearing
inner_diameter = {{ inner_diameter }}
thickness = {{ thickness }}

# The bearing is modelled as a cylinder with a hole in the middle
part = cylinder(outer_diameter / 2, thickness) - cylinder(inner_diameter / 2, thickness)

anchors = [((0., 0., 0.), (0., 0., -10.)),
           ((0., 0., thickness), (0., 0., 10.))]

anchors = {1: {"position": (0., 0., thickness / 2.),
               "direction": (0., 0., -1.),
               "dimension": inner_diameter,
               "iso_tolerance": "undefined",
               "description": "bearing axis on axle"},
           2: {"position": (0., 0., thickness / 2.),
               "direction": (0., 0., -1.),
               "dimension": outer_diameter,
               "iso_tolerance": "undefined",
               "description": "bearing axis in cage"}}