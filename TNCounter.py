import os
import sys
abspath = os.path.abspath(os.path.dirname(__file__))
sys.path.append(abspath)

from functions import imgProcess
from functions import itemDictionary

INPUT_FOLDER_NAME = 'inputItem'
CROP_FOLDER_NAME = 'itemCut'

#1. read images
imgs = imgProcess.loadImages(os.path.join(abspath, INPUT_FOLDER_NAME))

#2. read floor/position data from each image and convert to dict [TODO]
#imgDict = dict()

#3. cut to item pieces
cuts = []
for img in imgs:
    cuts.extend(imgProcess.cutImages(img))
    
for idx,img in enumerate(cuts):
    thepath = ''.join((os.path.join(abspath, CROP_FOLDER_NAME), '\\', str(idx), '.png'))
    img.save(thepath)
    
itemDict = itemDictionary.itemDict

#4. read numbers & item
for idx,img in enumerate(cuts):
    item = imgProcess.getItem(img)
    num = imgProcess.getNumber(img)
    if item != 'null':
        itemDict[item] += sum(num)
    
print('')
print('Total Static Atk, Def, Hp Gain in Tut1')
print(itemDictionary.calculate_stats(itemDict))
print('')
for item in itemDict:
    print(f"{item.ljust(30)} {itemDict[item]}")