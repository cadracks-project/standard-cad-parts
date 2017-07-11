r"""Flanged bearing generation"""

from ccad.model import cylinder

outer_diameter = {{ outer_diameter }}
inner_diameter = {{ inner_diameter }}
thickness = {{ thickness }}

flange_diameter = {{ flange_diameter}}
flange_thickness = {{ flange_thickness }}

# Bearing body generation by substracting an inner cylinder
part = cylinder(outer_diameter / 2, thickness) - cylinder(inner_diameter / 2, thickness)

# Flange creation and adding
flange = cylinder(flange_diameter / 2, flange_thickness) - \
         cylinder(outer_diameter / 2, flange_thickness)
part += flange

# anchors = [((0., 0., 0.), (0., 0., -10.)),
#            ((0., 0., flange_thickness), (0., 0., -10.)),
#            ((0., 0., thickness), (0., 0., 10.))]

anchors = {1: {"position": (0., 0., 0.),
               "direction": (0., 0., -1.),
               "dimension": inner_diameter,
               "iso_tolerance": "undefined",
               "description": "bearing axis on axle"},
           2: {"position": (0., 0., flange_thickness),
               "direction": (0., 0., -1.),
               "dimension": outer_diameter,
               "iso_tolerance": "undefined",
               "description": "flange bottom on surface, bearing in cage"}}