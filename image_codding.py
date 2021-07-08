import cv2
import random
import numpy as np
import argparse
from PIL import Image as im

parser = argparse.ArgumentParser()
parser.add_argument('--image')
args = parser.parse_args()

image = cv2.imread(args.image)
image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
image=cv2.resize(image,(600,600))
#image=image.astype(float)

key=np.zeros((image.shape),dtype='float')
for i in range(key.shape[0]):
    for j in range(key.shape[1]):
        r=random.randint(0,256)
        key[i,j]=r

np.save('keys.npy', key)
# key=np.random.random((image.shape))*255
# key=255 * np.random.random_sample((image.shape))
# key=key/255
# image=image/255
result=np.zeros((image.shape),dtype='uint8')
# with open('keys.npy', 'wb') as f:
#     np.save(f, key)
global temp
temp=0
for  i in range(image.shape[0]):
    for j in range(image.shape[1]):
        temp=image[i, j] + key[i,j]
        if temp > 255:
            temp = image[i, j] + key[i,j] - 255
        result[i,j]=temp



# image=cv2.multiply(image,key)
# image=image*255
# print(image)
# cv2.imwrite('coded.jpg',result)
# cv2.waitKey()
encrypted_img = im.fromarray(result)
encrypted_img.save('codded.bmp')

