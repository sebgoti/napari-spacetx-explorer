from typing import TYPE_CHECKING
from enum import Enum
import numpy as np
from napari_plugin_engine import napari_hook_implementation
if TYPE_CHECKING:
    import napari

@napari_hook_implementation
def napari_experimental_provide_function():
    return read_spots

def read_spots(
        points: "napari.layers.Points",
        genes: str = 'IGHG1',
        color_s: str = 'white',
        size_s: str = '10'
) -> "napari.types.LayerDataTuple":
    """Retrieve points' data from selected group of genes.

    Parameters
    ----------
    points: napari.types.PointsData
        The raw data from a decoded CSV file
    genes: list
        list with genes to visualize.

    Returns
    -------
    layer_data: napari.types.LayerDataTuple
        The layer data tuple containing the corresponding
        points and metadata for visualization.
    """
    genes_list = genes.split(',')
    genes_dict_cmap = {g: i for i, g in enumerate(genes_list)}

    color_cycle = color_s.split(',')
    size_cycle = [int(i) for i in size_s.split(',')]

    spots_idx = [genes_dict_cmap[g] for g in points.properties['gene'] if g in genes_list]

    # List with indices of selected genes by user.
    selected_points_idx = [i for i in range(len(points.data)) if points.properties['gene'][i] in genes_list]

    # Here we select the data coordinates and labels/index of requested genes:
    selected_data = [points.data[i] for i in selected_points_idx]
    spot_properties = {'label': spots_idx}

    face_color = {
        'colors': 'label',
        'color_mode': 'cycle',
        'categorical_colormap': color_cycle
    }

    layer_data = (
        selected_data,
        #{'face_color': 'magenta',
        # 'symbol': 'ring'},
        {'properties': spot_properties,
         'size': size_cycle,
         'face_color': face_color},
        'Points'
    )

    return [layer_data]