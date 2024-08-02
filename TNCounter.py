import os
import sys
abspath = os.path.abspath(os.path.dirname(__file__))
sys.path.append(abspath)

from functions import img_process
from functions import item_dictionary
from functions.room_class import Room
from functions.make_dataframe import make_tactical_df
from functions.edit_sheet import edit_tactical_sheet

INPUT_FOLDER_NAME = 'inputItem'
CROP_FOLDER_NAME = 'itemCut'

#1. read images
imgs = img_process.load_images(os.path.join(abspath, INPUT_FOLDER_NAME))

#2. convert to Room object
rooms = dict()
for name,img in imgs.items():
    realname = name.split(' ')[0]
    if not realname in rooms:
        rooms[realname] = Room(realname)
    rooms[realname].add_image(img)

#3. cut to item pieces & read numbers and items
for name,obj in rooms.items():
    obj.crop()
    obj.save_crops(os.path.join(abspath, CROP_FOLDER_NAME))
    obj.get_items()
    
#4. make some dataframe
dict_list = [rooms[i].item_dict for i in rooms.keys()]
df = make_tactical_df(dict_list,list(rooms.keys()))
excel_file = 'TNCount.xlsx'
df.to_excel(excel_file, index=True)

#5. modify spreadsheet
edit_tactical_sheet(excel_file)