#!/usr/bin/python
# coding: utf-8

r"""Example use of the library.json file to create geometry_scripts and
cad files

"""

import logging
from os.path import join, dirname

from party.library_use import generate
from party.scripts_checking import check_all_scripts_from_library_jsons


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s :: %(levelname)6s :: '
                           '%(module)20s :: %(lineno)3d :: %(message)s')

generate(json_library_filepath=join(dirname(__file__), "library.json"),
         generate_steps=True, generate_stls=True, generate_htmls=True)
ok, errors = check_all_scripts_from_library_jsons(dirname(__file__))
if ok is True:
    logging.info("Scripts are ok")
else:
    logging.error("ERROR(S) in scripts")
    logging.error(str(errors))
