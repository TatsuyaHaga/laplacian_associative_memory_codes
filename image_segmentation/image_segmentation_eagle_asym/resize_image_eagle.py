#!/usr/bin/env python3

import sys
import numpy
import itertools
import PIL.Image

def trim_img(img,size,offset):
    img_np=numpy.array(img)
    orig_y=img_np.shape[0]
    orig_x=img_np.shape[1]
    size_x=size[0]
    size_y=size[1]
    offset_x=offset[0]
    offset_y=offset[1]
    x1=int((orig_x-size_x+offset_x)/2)
    x2=int((orig_x+size_x+offset_x)/2)
    y1=int((orig_y-size_y+offset_y)/2)
    y2=int((orig_y+size_y+offset_y)/2)
    return PIL.Image.fromarray(img_np[y1:y2, x1:x2])

#resize image
img=PIL.Image.open(sys.argv[1])
#img=0.298912*img[:,:,0]+0.586611*img[:,:,1]+0.114478*img[:,:,2] #mono
img=trim_img(img, (150,150), (-130,-20))
img.save("trimmed.jpg")
img=img.resize((35,35),resample=PIL.Image.BILINEAR)
img.save("resized.jpg")
