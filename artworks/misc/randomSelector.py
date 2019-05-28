import os, sys
from os.path import isfile, isdir, join
from PIL import Image
from tqdm import tqdm

import random
import numpy as np
import matplotlib.pyplot as plt


PATH  = 'Q:\DeepLearning\ImageClassification\Artwork_data\images'
SAMPLE  = 30


class RandomSelector:
    def __init__(self, path, sampleSize):
        self.path = path
        self.sampleSize = sampleSize
        self.pathList = []

    def getRandomFolder(self):
        folders = [f for f in os.listdir(self.path) if isdir(join(self.path, f))]
        indx = random.randint(0, len(folders)-1)
        folderPath = join(self.path, folders[indx])
        return folderPath
    
    def getRandomFile(self):
        folderPath = self.getRandomFolder()
                
        files = [f for f in os.listdir(folderPath) if isfile(join(folderPath, f))]
        indx = random.randint(0, len(files)-1)
        filePath = join(folderPath, files[indx])

        return filePath

    def __call__(self):
        for _ in range(self.sampleSize):
            self.pathList .append(self.getRandomFile()) 
        return self.pathList

    def __len__(self):
        return len(self.pathList)
    
    def __getitem__(self, positon):
        return self.pathList[positon]

    def __repr__(self):
        return f"{self.pathList}"        

class ImagePlot:

    size = (128, 128)
    extension = '.jpg'
    colsToPlot = 5
    fnameDiff = str(random.randint(0,1000))

    def __init__(self, images):
        self.images = images
        self.imageContainer = []

        for image in images:
            try: 
                im = Image.open(image)
            except:
                print(f"Could not open {im}")
                continue
            self.imageContainer.append(im)


  
    def Resize(self, size):
        self.size = size
        self.resizedImageContainer = []

        for image in self.imageContainer:
            imageResized = image.resize(size, Image.ANTIALIAS)
            self.resizedImageContainer.append(imageResized)
        
        return self.resizedImageContainer
    
    
    def ImgShape(self):
        for image in self.imageContainer:
            print(np.asarray(image).shape)

    def stackImagesH(self):
        images = self.Resize(self.size)
        imageMerge = np.hstack( (np.asarray(i)) for i in images)
        imageMerge = Image.fromarray(imageMerge)

        filename = self.stackImagesH.__name__ + self.fnameDiff
        imageMerge.save(filename + self.extension)
    
    def stackImagesV(self):
        images = self.Resize(self.size)
        imageMerge = np.hstack( (np.asarray(i)) for i in images)
        imageMerge = Image.fromarray(imageMerge)

        filename = self.stackImagesV.__name__ + self.fnameDiff
        imageMerge.save(filename + self.extension)
    
    def stackPlots(self):
        images = self.Resize(self.size)
        n_images = len(images)
        
        fig = plt.figure()
        for n, image in enumerate(images):
            
            fig.add_subplot(self.colsToPlot, np.ceil(n_images/float(self.colsToPlot)), n+1)
            plt.subplots_adjust(wspace=0.1, hspace=0.1)
            plt.axis('off')
            plt.imshow(np.array(image))
        
        fig.set_size_inches(np.array(fig.get_size_inches()) * n_images)
        filename = self.stackPlots.__name__ + self.fnameDiff
        plt.savefig(filename + self.extension)
    
    
if __name__ == "__main__":

    

    if len(sys.argv) == 2:
        for i in range(int(sys.argv[1])):

            random.seed(random.randint(0, 1000))

            f = RandomSelector(PATH, SAMPLE)
            imagesPath = f() 

            im = ImagePlot(imagesPath)
            im.stackPlots()

            print(f"Created {i+1} image!")
    
    else:
            random.seed(random.randint(0, 1000))

            f = RandomSelector(PATH, SAMPLE)
            imagesPath = f() 

            im = ImagePlot(imagesPath)
            im.stackPlots()

            print(f"Created one image!")

    

