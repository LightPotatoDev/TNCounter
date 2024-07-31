import os
from PIL import Image

def loadImages(path):
    images = []

    for filename in os.listdir(path):
        filepath = os.path.join(path, filename)
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            try:
                with Image.open(filepath) as img:
                    images.append(img.copy())
            except Exception as e:
                print(f'Error loading image {filename}:{e}')

    return images

START_POINT = (3,40)
SPACING = (1,22)
INTERFACE_SIZE = (149,38)
TIMES = (3,7)

def cutImages(img):
    cuts = []
    for i in range(TIMES[0]):
        for j in range(TIMES[1]):
            x1 = START_POINT[0] + SPACING[0]*i + INTERFACE_SIZE[0]*i
            x2 = x1 + INTERFACE_SIZE[0]
            y1 = START_POINT[1] + SPACING[1]*j + INTERFACE_SIZE[1]*j
            y2 = y1 + INTERFACE_SIZE[1]
            cuts.append(img.crop((x1,y1,x2,y2)))

    return cuts