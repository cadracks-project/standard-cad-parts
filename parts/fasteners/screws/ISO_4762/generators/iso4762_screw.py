r"""Generation script for ISO 4762 screw"""

from ccad.model import prism, filling, ngon, cylinder, translated

length = {{ length }}
threaded_length = {{ thread_length_minimal }}
unthreaded_diameter = {{ diameter_major }}
threaded_diameter = {{ diameter_pitch }}
head_diameter = {{ head_diameter }}
head_height = {{ head_height }}
key_size = {{ key_size }}
socket_depth = {{ socket_depth }}

if length - threaded_length > 0.:
    body = cylinder(threaded_diameter / 2, length) + \
           cylinder(unthreaded_diameter / 2, length - threaded_length)
else:
    body = cylinder(threaded_diameter / 2, length)

socket = translated(prism(filling
                          # ngon is written in a circle of a given radius,
                          # the socket definition is the diameter of the
                          # circle written in the hexagon
                          # -> multiply by 2 / sqrt(3)
                          (ngon(2 / 3**.5 * key_size / 2., 6)),
                          (0, 0, socket_depth)),
                    (0, 0, -head_height))

head = translated(cylinder(head_diameter / 2., head_height),
                  (0, 0, -head_height)) - socket
part = head + body
anchors = {1: {"position": (0., 0., 0.),
               "direction": (0., 0., -1.),
               "dimension": unthreaded_diameter,
               "description": "screw head on plane"}}