"""
This module is an example of a barebones function plugin for napari

It implements the ``napari_experimental_provide_function`` hook specification.
see: https://napari.org/docs/dev/plugins/hook_specifications.html

Replace code below according to your needs.
"""
from typing import TYPE_CHECKING

import numpy as np
import string
from csv import reader
from napari_plugin_engine import napari_hook_implementation

if TYPE_CHECKING:
    import napari


# This is the actual plugin function, where we export our function
# (The functions themselves are defined below)
@napari_hook_implementation
def napari_experimental_provide_function():
    # we can return a single function
    # or a tuple of (function, magicgui_options)
    # or a list of multiple functions with or without options, as shown here:
    return read_spots


def read_spots(file_path: str,
               gene: str = "BATF"):

    with open(file_path, 'r') as fh:
        csv_reader = reader(fh)
        header = next(csv_reader)
        xc, yc = header.index('xc'), header.index('yc')
        spot_coordinates = []
        i = 0
        for row in csv_reader:
            if row[header.index('target')] == gene:
                i += 1
                spot_coordinates.append([float(row[xc]), float(row[yc])])

    layer_data = (
        np.array(spot_coordinates),
        {
            "size": 10
            },
        "Points"
            )
    return layer_data
