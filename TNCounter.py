import os
import sys
abspath = os.path.abspath(os.path.dirname(__file__))
sys.path.append(abspath)

from functions import imgProcess
from functions import itemDictionary
from functions.floorClass import Floor

INPUT_FOLDER_NAME = 'inputItem'
CROP_FOLDER_NAME = 'itemCut'

#1. read images
imgs = imgProcess.load_images(os.path.join(abspath, INPUT_FOLDER_NAME), True)

#2. convert to Floor object
floors = dict()
for name,img in imgs.items():
    realname = name.split(' ')[0]
    if not realname in floors:
        floors[realname] = Floor(realname)
    floors[realname].add_image(img)

#3. cut to item pieces
for name,obj in floors.items():
    obj.crop()
    obj.save_crops(os.path.join(abspath, CROP_FOLDER_NAME))

#4. read numbers & item
for name,obj in floors.items():
    obj.get_items()
    print(obj.item_dict)
    
#5. get the total
