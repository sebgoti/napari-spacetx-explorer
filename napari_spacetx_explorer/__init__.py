try:
    from ._version import version as __version__
except ImportError:
    __version__ = "0.1.5"


from ._reader import napari_get_reader
from ._function2 import napari_experimental_provide_function
#from ._dock_widget import napari_experimental_provide_dock_widget
#from ._summary import napari_experimental_provide_function
#from ._function import napari_experimental_provide_function

