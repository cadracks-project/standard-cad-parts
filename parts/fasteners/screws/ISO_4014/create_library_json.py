#!/usr/bin/python
# coding: utf-8

r"""Script that creates the library.json file for the ISO 4014 standard"""


import logging
from party.library_creation import autocreate_library
from party.library_checking import check_all

logger = logging.getLogger(__name__)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s :: %(levelname)6s :: '
                               '%(module)20s :: %(lineno)3d :: %(message)s')

    logger.info("Creating the library JSON from its template ...")
    autocreate_library("library_template.json")
    logger.info("...done")

    logger.info("Checking the library JSON  ...")
    library_ok_list, _ = check_all("library.json")
    ok = all(list_element is True for list_element in library_ok_list)
    if ok is True:
        logger.info("...done - All OK")
    else:
        logger.error("ERROR(S) in the library JSON")
        logger.info("rules ok : %s" % str(library_ok_list[0]))
        logger.info("units ok : %s" % str(library_ok_list[1]))
        logger.info("fields ok : %s" % str(library_ok_list[2]))
