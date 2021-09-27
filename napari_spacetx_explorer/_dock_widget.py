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


genes_file = reader_function('~/Documents/Data/napari-spacetx-explorer/spots_reduced.csv')
genes_list = (genes_file[0][1]['properties']['gene']).unique()#genes_file.properties['gene'].unique()

@magic_factory#(
#    call_button='Make Points',
#    genes = dict(widget_type='ComboBox', label='gene selection', choices=genes_list, value=genes_list[0], tooltip='there is a')
#)
def example_magic_widget(
        img_layer: "napari.layers.Points"#,
 #       genes
) -> "napari.types.LayerDataTuple":

    print(f"you have selected {img_layer}")


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