from typing import TYPE_CHECKING
#from enum import Enum
import numpy as np
from napari_plugin_engine import napari_hook_implementation
if TYPE_CHECKING:
    import napari


# This is the actual plugin function, where we export our function
# (The functions themselves are defined below)
@napari_hook_implementation
def napari_experimental_provide_function():
    # we can return a single function
    # or a tuple of (function, magicgui_options)<-------
    # or a list of multiple functions with or without options, as shown here:
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
    #genes_dict_cmap = {g: i for i, g in e}

    #color_cycle = [
    #    [0.12156863, 0.46666667, 0.70588235, 1.],
    #    [1., 0.49803922, 0.05490196, 1.],
    #    [0.17254902, 0.62745098, 0.17254902, 1.],
    #    [0.83921569, 0.15294118, 0.15686275, 1.],
    #    [0.58039216, 0.40392157, 0.74117647, 1.],
    #    [0.54901961, 0.3372549, 0.29411765, 1.],
    #    [0.89019608, 0.46666667, 0.76078431, 1.],
    #    [0.49803922, 0.49803922, 0.49803922, 1.],
    #    [0.7372549, 0.74117647, 0.13333333, 1.],
    #    [0.09019608, 0.74509804, 0.81176471, 1.]
    #]
    color_cycle = color_s.split(',')
    size_cycle = [int(i) for i in size_s.split(',')]

    spots_idx = [genes_dict_cmap[g] for g in points.properties['gene'] if g in genes_list]
    # spots_idx = [genes_dict_cmap[gene] for gene in points.properties['gene']]
    # selected_points = [points.data[i] for i in range(len(points.data)) if points.properties['gene'][i] in genes_list]

    # List with indices of selected genes by user.
    selected_points_idx = [i for i in range(len(points.data)) if points.properties['gene'][i] in genes_list]

    # Here we select the data coordinates and labels/index of requested genes:
    selected_data = [points.data[i] for i in selected_points_idx]
    selected_idx = spots_idx#[spots_idx[i] for i in selected_points_idx]

    spot_properties = {'label': selected_idx}

    face_color = {
        'colors': 'label',
        'color_mode': 'cycle',
        'categorical_colormap': color_cycle
    }

    #selected_points = [points.data[i] for i in range(len(points.data))
    #                   if points.properties['gene'][i] in genes]

    layer_data = (
        selected_data,
        #{'face_color': 'magenta',
        # 'symbol': 'ring'},
        {'properties': spot_properties,
         'size': size_cycle,
         'face_color': face_color},
        'Points'
    )

    return layer_data




