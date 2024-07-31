import os
import sys
abspath = os.path.abspath(os.path.dirname(__file__))
sys.path.append(abspath)

from functions import imgProcess
from PIL import Image, ImageEnhance

INPUT_FOLDER_NAME = 'inputItem'
CROP_FOLDER_NAME = 'itemCut'

#1. read images
imgs = imgProcess.loadImages(os.path.join(abspath, INPUT_FOLDER_NAME))

#2. read floor/position data from each image and convert to dict [TODO]
#imgDict = dict()

#3. cut to item pieces
cuts = imgProcess.cutImages(imgs[1])
for idx,img in enumerate(cuts):
    thepath = ''.join((os.path.join(abspath, CROP_FOLDER_NAME), '\\', str(idx), '.png'))
    img.save(thepath)

#4. read numbers & item
for idx,img in enumerate(cuts):
    item = imgProcess.getItem(img)
    print(item)
    num = imgProcess.getNumber(img)
    print(num)
    print('')