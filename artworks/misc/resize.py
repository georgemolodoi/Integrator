import os, sys
from os.path import isfile, isdir, join
from PIL import Image
from tqdm import tqdm

import random
import numpy as np

PATH  = 'Q:\\WebApps\\Integrator\\mysite\\artworks\media\\ArtistsOverview'

SAVE_PATH = 'Q:\\WebApps\\Integrator\\mysite\\artworks\media\\ArtistsOverview\\Resized'

SIZE = 256, 256

imgFiles = [f for f in os.listdir(PATH) if isfile(join(PATH, f)) and ".jpg" in f]


Image.MAX_IMAGE_PIXELS = None

for file in imgFiles:
    im = Image.open(join(PATH, file)) 
    im.thumbnail(SIZE)
    im.save(join(SAVE_PATH, file))
    print(f"Resized and saved {file}")

