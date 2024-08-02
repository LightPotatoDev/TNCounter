import os
from PIL import Image
import numpy as np
import pickle

ABSPATH = os.path.abspath(os.path.dirname(__file__))
RES_PATH = ''.join((os.path.join(ABSPATH, '..'), '\\resources'))

def load_images(path,as_dict=False) -> list|dict:
    images = []
    imgDict = dict()

    for filename in os.listdir(path):
        filepath = os.path.join(path, filename)
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            try:
                with Image.open(filepath) as img:
                    if not as_dict:
                        images.append(img.copy())
                    else:
                        name = filename.split('.')[0]
                        imgDict[name] = img.copy()
            except Exception as e:
                print(f'Error loading image {filename}:{e}')

    if not as_dict:
        return images
    else:
        return imgDict
    
def load_number_images() -> list:
    NUMBER_IMG_PATH = ''.join((RES_PATH, '\\numbers'))
    NUMBER_PKL_PATH = ''.join((RES_PATH, '\\numbers_img.pkl'))
    images:dict = dict()
    if os.path.exists(NUMBER_PKL_PATH):
        with open(NUMBER_PKL_PATH, 'rb') as f:
            images = pickle.load(f)
        return images
    else:
        images = load_images(NUMBER_IMG_PATH, as_dict = True)
        with open(NUMBER_PKL_PATH, 'wb') as f:
            pickle.dump(images, f)
        return images
        
def load_item_images() -> dict:
    ITEM_IMG_PATH = ''.join((RES_PATH, '\\items'))
    ITEM_PKL_PATH = ''.join((RES_PATH, '\\items_img.pkl'))
    images:dict = dict()
    if os.path.exists(ITEM_PKL_PATH):
        with open(ITEM_PKL_PATH, 'rb') as f:
            images = pickle.load(f)
        return images
    else:
        images = load_images(ITEM_IMG_PATH, as_dict = True)
        with open(ITEM_PKL_PATH, 'wb') as f:
            pickle.dump(images, f)
        return images

def cut_images(img) -> list:
    START_POINT = (3,40)
    SPACING = (1,22)
    IMAGE_SIZE = (149,38)
    TIMES = (3,7)
    
    cuts = []
    for i in range(TIMES[0]):
        for j in range(TIMES[1]):
            x1 = START_POINT[0] + SPACING[0]*i + IMAGE_SIZE[0]*i
            x2 = x1 + IMAGE_SIZE[0]
            y1 = START_POINT[1] + SPACING[1]*j + IMAGE_SIZE[1]*j
            y2 = y1 + IMAGE_SIZE[1]
            cuts.append(img.crop((x1,y1,x2,y2)))

    return cuts

def add_alpha(img) -> Image:
    alpha = Image.new('L', img.size, 255)
    img = img.convert('RGBA')
    img.putalpha(alpha)
    return img

def compare_num(img1, img2) -> int:
    if img1.size != img2.size:
        print(img1.size,img2.size)
        raise ValueError("Images must have the same dimensions")
    
    if img1.mode != 'RGBA':
        img1 = add_alpha(img1)
    if img2.mode != 'RGBA':
        img2 = add_alpha(img2)
        
    img1 = img1.convert('L')
    img2 = img2.convert('L')
    
    array1 = np.array(img1,dtype=np.int32)
    array2 = np.array(img2,dtype=np.int32)

    diff = np.abs(array1 - array2)
    maxdiff = np.max(diff)
    return maxdiff

def get_number(img) -> list:
    START_POINT = ((40,14),(40,27))
    IMAGE_SIZE = (6,8)
    SPACING = 6
    DIFF_TRESHOLD = 96
    NUM_IMAGES:dict = load_number_images()
    
    res = [0,0]
    for i in range(2):
        for j in range(3):
            prevRes = res[i]
            x1 = START_POINT[i][0] + SPACING*j
            x2 = x1 + IMAGE_SIZE[0]
            y1 = START_POINT[i][1]
            y2 = y1 + IMAGE_SIZE[1]

            cropNum = img.crop((x1,y1,x2,y2))
            for idx,num in NUM_IMAGES.items():
                diff = compare_num(cropNum,num)
                if diff < DIFF_TRESHOLD:
                    res[i] = 10*res[i]+int(idx)
                    break
            
            if prevRes == res[i]:
                break
            
    return res

def compare_item(img1,img2) -> int:
    IMAGE_SIZE = (24,24)
    
    if img1.size != img2.size:
        print(img1.size,img2.size)
        raise ValueError("Images must have the same dimensions")
    
    if img1.mode != 'RGBA':
        img1 = add_alpha(img1)
    if img2.mode != 'RGBA':
        img2 = add_alpha(img2)
        
    array1 = np.array(img1,dtype=np.int32)
    array2 = np.array(img2,dtype=np.int32)
    
    diff = np.abs(array1 - array2)
    for i in range(IMAGE_SIZE[0]):
        for j in range(IMAGE_SIZE[1]):
            if array2[i][j][3] == 0:
                diff[i][j] = 0
                
    maxdiff = np.max(diff)
    return maxdiff

def get_item(img) -> str:
    START_POINT = (8,13)
    IMAGE_SIZE = (24,24)
    ITEM_DIFF_TRESHOLD = 12
    ITEM_IMAGES = load_item_images()
    
    res = 'null'
    x1 = START_POINT[0]
    x2 = x1 + IMAGE_SIZE[0]
    y1 = START_POINT[1]
    y2 = y1 + IMAGE_SIZE[1]

    cropItem = img.crop((x1,y1,x2,y2))
    
    for name,itemImg in ITEM_IMAGES.items():
        diff = compare_item(cropItem,itemImg)
        if diff < ITEM_DIFF_TRESHOLD:
            res = name
            break
    
    return res