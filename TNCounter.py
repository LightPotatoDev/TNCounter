import os
import sys
abspath = os.path.abspath(os.path.dirname(__file__))
sys.path.append(abspath)

from functions import imgProcess
from PIL import Image, ImageEnhance
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\light\AppData\Local\tesseract.exe'

INPUT_FOLDER_NAME = 'inputItem'
CROP_FOLDER_NAME = 'itemCut'

#1. read images
imgs = imgProcess.loadImages(os.path.join(abspath, INPUT_FOLDER_NAME))

#2. read floor/position data from each image and convert to dict [TODO]
#imgDict = dict()

#3. cut to item pieces
cuts = imgProcess.cutImages(imgs[0])
for idx,img in enumerate(cuts):
    thepath = ''.join((os.path.join(abspath, CROP_FOLDER_NAME), '\\', str(idx), '.png'))
    img.save(thepath)

#4. modify images to increase text reading accuracy
cutEnhance = []
for img in cuts:
    img = img.convert('L')
    img = img.resize((img.width * 10, img.height * 10), Image.Resampling.LANCZOS)
    img = img.point(lambda x: 0 if x < 150 else 255)
    #enhancer = ImageEnhance.Contrast(img)
    #imgEnhanced = enhancer.enhance(2)
    cutEnhance.append(img)
cutEnhance[1].show()

#5. read item type and the number from each img piece
texts = []
for img in cuts:
    txt = pytesseract.image_to_string(img)
    texts.append(txt)
for i,t in enumerate(texts):
    print(i)
    print(t)

#6. store the info in a spreadsheet