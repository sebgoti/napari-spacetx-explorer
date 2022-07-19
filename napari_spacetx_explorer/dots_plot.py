from starfish import Experiment
import os
import matplotlib
#import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from starfish import Experiment
from starfish.image import ApplyTransform, LearnTransform, Filter
from starfish.types import Axes
from starfish import data, FieldOfView
from starfish.spots import FindSpots
from starfish.util.plot import imshow_plane
from starfish.core.spots.DecodeSpots.trace_builders import build_spot_traces_exact_match

import napari

ROOT = '/Volumes/exchange/SebastianGonzalez/Sanjana'
SAMPLE = 'Sample2_20220530'
SPOTS = 'spots.csv'

size = 2100
fov = 'fov_105'
gene = 'ACTA2'
e = Experiment.from_json(os.path.join(ROOT, SAMPLE, 'SpaceTx/primary/experiment.json'))


def gene_points(SAMPLE, gene, fov, exp, size):
    size = 2100
    # Take x & y positions for translated FOV:
    fov_coord = pd.read_csv(os.path.join(ROOT, SAMPLE, 'Tiled/primary/coordinates.csv'))

    x_coord = fov_coord['xc_min'].iloc[int(fov.split('_')[1])]
    y_coord = fov_coord['yc_min'].iloc[int(fov.split('_')[1])]

    # Plot points layer in napari of seleceted gene and with the new frame of reference:
    spots = pd.read_csv(os.path.join(ROOT, SAMPLE, SPOTS))
    gene_transcripts = spots[spots.target == gene]

    spot_map = []
    for i in range(len(gene_transcripts)):
        x, y = gene_transcripts[['xc', 'yc']].iloc[i].to_list()
        if (x_coord <= x <= x_coord + size) and (y_coord <= y <= y_coord + size):
            x, y = x - x_coord, y - y_coord
            spot_map.append([y, x])


    #x_trans = [x for x in gene_transcripts['xc'] if x_coord <= x < x_coord + size]
    #y_trans = [y for y in gene_transcripts['yc'] if y_coord <= y < y_coord + size]
    return spot_map #list(map(list, zip(*spot_map)))

#spot_map = np.zeros((len(x_trans), 2))
#spot_map[:, 0] = x_trans
#spot_map[:, 1] = y_trans
#viewer = napari.Viewer()
#viewer.add_points(gene_points(SAMPLE, gene, fov, e, size), symbol = 'ring', size = 10)
#napari.run()