"""
This module is an example of a barebones QWidget plugin for napari

It implements the ``napari_experimental_provide_dock_widget`` hook specification.
see: https://napari.org/docs/dev/plugins/hook_specifications.html

Replace code below according to your needs.
"""
from napari_plugin_engine import napari_hook_implementation
from qtpy.QtWidgets import QWidget, QHBoxLayout, QPushButton
from magicgui import magic_factory
from ._reader import reader_function
import magicgui


class ExampleQWidget(QWidget):
    # your QWidget.__init__ can optionally request the napari viewer instance
    # in one of two ways:
    # 1. use a parameter called `napari_viewer`, as done here
    # 2. use a type annotation of 'napari.viewer.Viewer' for any parameter
    def __init__(self, parent=None):
        super().__init__(parent)
        #self.resize(1200, 800)
        #self.viewer = napari_viewer

        btn = QPushButton("Click me!")
        btn.clicked.connect(self._on_click)

        self.setLayout(QHBoxLayout())
        self.layout().addWidget(btn)
        self.show()

    def _on_click(self):
        print("napari has")#, len(self.viewer.layers), "layers")


#genes_file = reader_function('~/Documents/Data/napari-spacetx-explorer/spots_reduced.csv')
#genes_list = (genes_file[0][1]['properties']['gene']).unique()#genes_file.properties['gene'].unique()

@magic_factory#(
#    call_button='Make Points',
#    genes = dict(widget_type='ComboBox', label='gene selection', choices=genes_list, value=genes_list[0], tooltip='there is a')
#)
def example_magic_widget(
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
    # genes_dict_cmap = {g: i for i, g in e}

    # color_cycle = [
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
    # ]
    color_cycle = color_s.split(',')
    size_cycle = [int(i) for i in size_s.split(',')]

    spots_idx = [genes_dict_cmap[g] for g in points.properties['gene'] if g in genes_list]
    # spots_idx = [genes_dict_cmap[gene] for gene in points.properties['gene']]
    # selected_points = [points.data[i] for i in range(len(points.data)) if points.properties['gene'][i] in genes_list]

    # List with indices of selected genes by user.
    selected_points_idx = [i for i in range(len(points.data)) if points.properties['gene'][i] in genes_list]

    # Here we select the data coordinates and labels/index of requested genes:
    selected_data = [points.data[i] for i in selected_points_idx]
    selected_idx = spots_idx  # [spots_idx[i] for i in selected_points_idx]

    spot_properties = {'label': selected_idx}

    face_color = {
        'colors': 'label',
        'color_mode': 'cycle',
        'categorical_colormap': color_cycle
    }

    # selected_points = [points.data[i] for i in range(len(points.data))
    #                   if points.properties['gene'][i] in genes]

    layer_data = (
        selected_data,
        # {'face_color': 'magenta',
        # 'symbol': 'ring'},
        {'properties': spot_properties,
         'size': size_cycle,
         'face_color': face_color},
        'Points'
    )

    return layer_data


@napari_hook_implementation
def napari_experimental_provide_dock_widget():
    # you can return either a single widget, or a sequence of widgets
    return example_magic_widget#, {'name': 'spacetx-visualizer'}#[ExampleQWidget, example_magic_widget]
"""

from qtpy.QtWidgets import QWidget
from napari_plugin_engine import napari_hook_implementation
#from magicgui import magic_factory

class MyWidget(QWidget):
    def __init__(selfself, napari_viewer):
        self.viewer = napari_viewer
        super().__init__()

        # initialize layout
        layout = QGridLayout()

        # add a button
        btn = QPushButton('Click me!', self)
        def trigger():
            print("napari has", len(napari_viewer.layers), "layers")
        btn.clicked.connect(trigger)
        layout.addWidget(btn)

        # activate layout
        self.setLayout()

@napari_hook_implementation
def napari_experimental_provide_dock_widget:
    return MyWidget
"""