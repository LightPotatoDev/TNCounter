import os
import sys
abspath = os.path.abspath(os.path.dirname(__file__))
sys.path.append(abspath)

from functions import imgProcess
from functions import itemDictionary
from functions.roomClass import Room
from functions.makeDataframe import make_tactical_df

INPUT_FOLDER_NAME = 'inputItem'
CROP_FOLDER_NAME = 'itemCut'

#1. read images
imgs = imgProcess.load_images(os.path.join(abspath, INPUT_FOLDER_NAME), True)

#2. convert to Room object
rooms = dict()
for name,img in imgs.items():
    realname = name.split(' ')[0]
    if not realname in rooms:
        rooms[realname] = Room(realname)
    rooms[realname].add_image(img)

#3. cut to item pieces
for name,obj in rooms.items():
    obj.crop()
    obj.save_crops(os.path.join(abspath, CROP_FOLDER_NAME))

#4. read numbers & item
for name,obj in rooms.items():
    obj.get_items()
    
#5. plug to spreadsheet
dict_list = [rooms[i].item_dict for i in rooms.keys()]
df = make_tactical_df(dict_list,list(rooms.keys()))
print(df)
