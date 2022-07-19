from starfish import Experiment
import os
import matplotlib
#import matplotlib.pyplot as plt
import numpy as np

from starfish import Experiment
from starfish.image import ApplyTransform, LearnTransform, Filter
from starfish.types import Axes
from starfish import data, FieldOfView
from starfish.spots import FindSpots
from starfish.util.plot import imshow_plane
from starfish.core.spots.DecodeSpots.trace_builders import build_spot_traces_exact_match

import napari

from dots_plot import *

ROOT = '/Volumes/exchange/SebastianGonzalez/Sanjana'
SAMPLE = 'Sample2_20220530'
SPOTS = 'spots.csv'
SPOTS_PATH = os.path.join(ROOT, SAMPLE, SPOTS)
e = Experiment.from_json(os.path.join(ROOT, SAMPLE, 'SpaceTx/primary/experiment.json'))


# The idea is for the user to select a field of view and then to
# show this sequence of files with the codebook information from
# the selected gene and plot the spots file on top of this

def get_cropped_coords(table, x_min, x_max, y_min, y_max):
    df = table.to_features_dataframe()
    df = df.loc[df['x'].between(x_min, x_max) & df['y'].between(y_min, y_max)]
    return df['x'].values-x_min, df['y'].values-y_min, df['radius'].values.astype(int)


def read_round(gene):
    round_ch_array = [] #list((len(gene), 2)).astype(int)

    for i in range(len(gene)):
        l = list(gene[i])
        idx = l.index(1)
        #print('Round {} & channel {}'.format(i, idx))
        round_ch_array.append(idx)
    return round_ch_array

def read_gene(cbk,
              gene: str = 'ACTA2',
    ) -> list:
    """

    Parameters
    ----------
    gene

    Returns
    -------
    tuple: (round, chanel)
    """
    return cbk.sel(target = gene).data

def view_gene_exp(
    gene: str = 'None',
    fov: str = 'fov_000',
    exp: Experiment = e,
    xslice: int = 500,
    yslice: int = 500,
    thr: float = 0.025,
    size: int = 2100
):
    """
    Read and display data according to a StarFISH-formatted
    experiment.
    Parameters
    ----------
    gene
    fov
    exp

    Returns
    -------

    """
    FOV = exp[fov]
    imgs = FOV.get_image(FieldOfView.PRIMARY_IMAGES)
    dots = FOV.get_image("anchor_dots")

    # register primary images to reference round
    learn_translation = LearnTransform.Translation(reference_stack=dots, axes=Axes.ROUND, upsampling=1000)
    transforms_list = learn_translation.run(imgs.reduce({Axes.CH, Axes.ZPLANE}, func="max"))
    warp = ApplyTransform.Warp()
    warp.run(imgs, transforms_list=transforms_list, in_place=True)

    # run blob detector with dots as reference image
    # following guideline of sigma = radius/sqrt(2) for 2D images
    # threshold is set conservatively low
    #bd = FindSpots.BlobDetector(
    #    min_sigma=1,
    #    max_sigma=3,
    #    num_sigma=30,
    #    threshold=thr,
    #    is_volume=False,
    #    measurement_type='mean',
    #)
    #spots = bd.run(image_stack=imgs, reference_image=dots)

    # build spot traces into intensity table
    #bd_table = build_spot_traces_exact_match(spots)

    #bd_x, bd_y, bd_s = get_cropped_coords(bd_table, xmin, xmax, ymin, ymax)
    round_ch_array = read_round(read_gene(e.codebook, gene))

    spot_map = gene_points(SAMPLE, gene, fov, e, size)

    viewer = napari.Viewer()
    viewer.grid.stride = 2
    for i in range(len(round_ch_array)):
        # Plot anchor image and selected channel:
        cropped_image: starfish.ImageStack = imgs.sel({Axes.ROUND: i,  # , ch),
                                                       Axes.CH: round_ch_array[i],
                                                       Axes.X: (0, xslice),
                                                       Axes.Y: (0, yslice)})

        round_ch: np.array = cropped_image.xarray.squeeze().data

        viewer.add_image(round_ch, name=f'Round_{i}')
        viewer.add_points(spot_map, symbol='ring', size=20)

    dots = dots.sel({Axes.X: (0, xslice), Axes.Y: (0, yslice)}).xarray.squeeze().data
    viewer.add_image(dots, name="Anchor dots")
    viewer.add_points(spot_map, symbol='ring', size=20)
    napari.run()

#dots.reduce({Axes.ZPLANE}, func="max"), sel = {Axes.X: (xmin, xmax),
    #
    #Axes.Y: (ymin, ymax)}, vmax = 0.15, ax = ax1, title = 'AnchorSpots')
    #viewer = napari.Viewer()

    # Plot anchor image and selected channel:
    #viewer.add_image(imgs.reduce())
#if __name__ == "__main__":
view_gene_exp('ACTA2', 'fov_105', e, 2100, 2100)

