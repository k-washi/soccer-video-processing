import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import utils.config
import logging

def add_ID_to_path(file_name, id):
    name, ext = os.path.splitext(file_name)
    if type(id) == int:
        return name + "_" + str(id) + ext

    logging.info("Bad id type {0}, {1}".format(id, type(id)))
    return file_name

