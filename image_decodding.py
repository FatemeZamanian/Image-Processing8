import cv2
import numpy as np
import argparse
from PIL import Image as im

parser = argparse.ArgumentParser()
parser.add_argument('--image',type=str)
parser.add_argument('--key',type=str)
args = parser.parse_args()
image = im.open(args.image)
image= np.array(image)

# image=image/255
# image=image.astype(float)

key = np.load(args.key)
# key=key*255
# result=cv2.divide(image,key)
# result=result*255
result=np.zeros_like(image)

for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        temp = image[i, j]-key[i,j]
        if temp < 0:
            temp = 255 + temp
        result[i, j] = temp

cv2.imshow('',result)
cv2.waitKey()