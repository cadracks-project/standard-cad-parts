r"""Generation script for ISO 4014 screw"""

from ccad.model import prism, filling, ngon, cylinder, translated

k_max = {{ k_max }}
s_max = {{ s_max }}
l_g_max = {{ l_g_max }}
d_s_max = {{ d_s_max }}
d_s_min = {{ d_s_min }}
l_max = {{ l_max }}

head = translated(prism(filling(ngon(2 / 3**.5 * s_max / 2., 6)), (0, 0, k_max)), (0., 0., -k_max))

threaded = cylinder(d_s_min / 2., l_max)
unthreaded = cylinder(d_s_max / 2., l_g_max)

part = head + threaded + unthreaded
anchors = {1: {"position": (0., 0., 0.),
               "direction": (0., 0., -1.),
               "dimension": d_s_max,
               "description": "screw head on plane"}}