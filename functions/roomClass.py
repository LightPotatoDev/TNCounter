from . import itemDictionary
from . import imgProcess
import copy

class Room:
    def __init__(self,name):
        self.name = name
        self.images = []
        self.crops = []
        self.item_dict = copy.deepcopy(itemDictionary.item_dict)
        
    def add_image(self,img):
        self.images.append(img)
        
    def crop(self):
        for img in self.images:
            self.crops.extend(imgProcess.cut_images(img))
            
    def save_crops(self,path):
        for i,x in enumerate(self.crops):
            filename = ''.join((path, '\\', self.name, '_', str(i), '.png'))
            x.save(filename)
            
    def get_items(self):
        for idx,img in enumerate(self.crops):
            item = imgProcess.get_item(img)
            num = imgProcess.get_number(img)
            if item != 'null':
                self.item_dict[item] += sum(num)