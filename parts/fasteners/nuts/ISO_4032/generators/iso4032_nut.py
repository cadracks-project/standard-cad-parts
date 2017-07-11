r"""Generation script for ISO 4032 nut"""

from ccad.model import prism, filling, ngon, cylinder

m_max = {{ m_max }}
s_max = {{ s_max }}
d_a_min = {{ d_a_min }}

body = prism(filling(ngon(2 / 3**.5 * s_max / 2., 6)), (0, 0, m_max))

hole = cylinder(d_a_min / 2., m_max)
part = body - hole
anchors = {1: {"position": (0., 0., 0.),
               "direction": (0., 0., -1.),
               "dimension": d_a_min,
               "description": "tightened bolt"}}