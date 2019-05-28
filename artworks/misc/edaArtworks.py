from sys import argv
from os import listdir, chdir, getcwd
from os.path import isfile, isdir, join
from tqdm import tqdm
from PIL import Image

import random 
import os, sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

path = 'Q:\DeepLearning\ImageClassification\Artwork_data\images'

def folderIter(path, action, randomSelect=False,):
    """
    Loops through all the folders and files and applies an action to each file.
    
    path = string oto the the path of folders 

    **changes working directory to each folder
    """

    folders = [f for f in listdir(path)]

    # Loop through folders
    for id, folder in enumerate(folders):
        tqdm.write('\n')
        tqdm.write(f'Currently in {folder} folder. {len(folders)-id-1} remaining...')

        # Join path with directories name
        fpath = join(path, folder)
        chdir(fpath)

        # Loop through files in directoy
        files = [f for f in listdir(fpath)]
        
        if (randomSelect):
            sampleLenght = 30
            try:
                randomFiles = random.sample(files, sampleLenght)
            
            except ValueError:
                sampleLenght = sampleLenght//2
                randomFiles = random.sample(files, sampleLenght)
                print('Try reducing the sampleLenght of random sample!')

            action(randomFiles)
        else: 
            action(files)
    
def plotImages(images):
    size = (128, 128)
    n_images = len(images)
    cols = 5

    fig = plt.figure()

    for n, image in enumerate(images):
        try:
            im = Image.open(image)
        except:
            print(f'Could not open {image} ')
            continue

        thmb = im.resize(size, Image.ANTIALIAS)
        
        fig.add_subplot(cols, np.ceil(n_images/float(cols)), n+1)
        plt.subplots_adjust(wspace=0.1, hspace=0.1)
        plt.axis('off')
        plt.imshow(np.array(thmb))
    
    fig.set_size_inches(np.array(fig.get_size_inches()) * n_images)
    
    saveName = join(sys.path[0], os.path.basename(getcwd()) + '.jpg')
    
    print(f"Creating {saveName}")
    plt.savefig(saveName)

def getFolderLenght(path):
    folders = [f for f in listdir(path)]
    lenghts = []
    for folder in folders:
        filePath = join(path, folder)
        files = [f for f in listdir(filePath)]
        lenghts.append((folder, len(files)))
        # print(f'The {folder} folder has {len(files)} images.')
        
    df = pd.DataFrame(lenghts, columns=['Artist', 'No_of_Paintings'])
    print(df)
    return df


if __name__ == '__main__':
    folderIter(path, plotImages, randomSelect=True)

