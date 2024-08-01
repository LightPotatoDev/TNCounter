import os
from PIL import Image
import numpy as np

ABSPATH = os.path.abspath(os.path.dirname(__file__))

def load_images(path,asDict=False) -> list|dict:
    images = []
    imgDict = dict()

    for filename in os.listdir(path):
        filepath = os.path.join(path, filename)
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            try:
                with Image.open(filepath) as img:
                    if not asDict:
                        images.append(img.copy())
                    else:
                        name = filename.split('.')[0]
                        imgDict[name] = img.copy()
            except Exception as e:
                print(f'Error loading image {filename}:{e}')

    if not asDict:
        return images
    else:
        return imgDict

START_POINT = (3,40)
SPACING = (1,22)
INTERFACE_SIZE = (149,38)
TIMES = (3,7)

def cut_images(img) -> list:
    cuts = []
    for i in range(TIMES[0]):
        for j in range(TIMES[1]):
            x1 = START_POINT[0] + SPACING[0]*i + INTERFACE_SIZE[0]*i
            x2 = x1 + INTERFACE_SIZE[0]
            y1 = START_POINT[1] + SPACING[1]*j + INTERFACE_SIZE[1]*j
            y2 = y1 + INTERFACE_SIZE[1]
            cuts.append(img.crop((x1,y1,x2,y2)))

    return cuts

NUM_POINT = ((40,14),(40,27))
NUM_SIZE = (6,8)
NUM_SPACING = 6
NUM_RES_PATH = ''.join((os.path.join(ABSPATH, '..'), '\\resources\\numbers'))
NUM_IMAGES = load_images(NUM_RES_PATH)
NUM_TEST_PATH = ''.join((os.path.join(ABSPATH, '..'), '\\numberCompareTest'))
NUM_DIFF_TRESHOLD = 96
#WHITE_TRESHOLD = 128

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
    #diff[array2 < WHITE_TRESHOLD] = 0
    maxdiff = np.max(diff)
    #error = np.sum(np.square(diff))
    #print(error)
    return maxdiff

def get_number(img) -> list:
    res = [0,0]
    for i in range(2):
        for j in range(3):
            prevRes = res[i]
            x1 = NUM_POINT[i][0] + NUM_SPACING*j
            x2 = x1 + NUM_SIZE[0]
            y1 = NUM_POINT[i][1]
            y2 = y1 + NUM_SIZE[1]

            cropNum = img.crop((x1,y1,x2,y2))
            for idx,num in enumerate(NUM_IMAGES):
                diff = compare_num(cropNum,num)
                if diff < NUM_DIFF_TRESHOLD:
                    res[i] = 10*res[i]+idx
                    break
            
            if prevRes == res[i]:
                break
            
    return res

ITEM_POINT = (8,13)
ITEM_SIZE = (24,24)
ITEM_RES_PATH = ''.join((os.path.join(ABSPATH, '..'), '\\resources\\items'))
ITEM_IMAGES = load_images(ITEM_RES_PATH,asDict=True)
ITEM_DIFF_TRESHOLD = 12

def compare_item(img1,img2) -> int:
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
    for i in range(ITEM_SIZE[0]):
        for j in range(ITEM_SIZE[1]):
            if array2[i][j][3] == 0:
                diff[i][j] = 0
                
    maxdiff = np.max(diff)
    return maxdiff

def get_item(img) -> str:
    res = 'null'
    x1 = ITEM_POINT[0]
    x2 = x1 + ITEM_SIZE[0]
    y1 = ITEM_POINT[1]
    y2 = y1 + ITEM_SIZE[1]

    cropItem = img.crop((x1,y1,x2,y2))
    
    for name,itemImg in ITEM_IMAGES.items():
        diff = compare_item(cropItem,itemImg)
        if diff < ITEM_DIFF_TRESHOLD:
            res = name
            break
    
    return res