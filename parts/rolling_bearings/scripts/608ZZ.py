#!/usr/bin/python
# coding: utf-8

r"""Plain bearing generation"""

from ccad.model import cylinder

outer_diameter = 22.0  # The outer diameter of the bearing
inner_diameter = 8.0
thickness = 7.0

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

if __name__ == '__main__':
    import ccad.display as cd
    v = cd.view()
    v.display(part, color=(0.1, 0.1, 1.0), transparency=0.3)
    for k, anchor in anchors.items():
        v.display_vector(origin=anchor['position'], direction=anchor['direction'])
    cd.start()
