import numpy as np
from PIL import Image

def compare_item(img1,img2) -> int:
    IMAGE_SIZE = (24,24)
    
    if img1.size != img2.size:
        print(img1.size,img2.size)
        raise ValueError("Images must have the same dimensions")
        
    array1 = np.array(img1,dtype=np.int32)
    array2 = np.array(img2,dtype=np.int32)
    
    diff = np.abs(array1 - array2)
    for i in range(IMAGE_SIZE[0]):
        for j in range(IMAGE_SIZE[1]):
            if array2[i][j][3] == 0:
                diff[i][j] = 0
                
    print(diff)
                
    sumdiff = np.sum(diff)
    return sumdiff

img1 = Image.open('Golden feather 30%.png')
img2 = Image.open('Golden feather 50%.png')
print(compare_item(img1, img2))

img1.close()
img2.close()