import os, sys, shutil
from os.path import isfile, join


def arrangeFiles(dirName): 
    path = sys.path[0]
    files = [f for f in os.listdir(path) if isfile(join(path, f)) and ('jpg' in f)]

    try:
        os.mkdir(dirName)

    except FileExistsError:
        print('The folder already exists')

    for f in files:
        print(f'Moving file {f}')
        shutil.move(join(path, f), join(path, dirName, f))


if __name__ == "__main__":
    arrangeFiles(sys.argv[1])