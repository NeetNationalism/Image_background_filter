#a program that removes white background
#from images

from PIL import Image
import numpy as np
im=Image.open("image.jpg")
im_RGB=np.asarray(im)
#shape==(height,width,3)
#0,0 in top left
im_png=Image.new("RGBA",im.size,(0,0,0,0))

def is_white(rgb):
#return true if rgb list/tuple is a white pixel
    v=0
    for value in rgb:
        v+=255-value        
    return v<20
    
for i in range(im.height):
    for j in range(im.width):
        if  not is_white(im_RGB[i,j]):
         im_png.putpixel((j,i),(255,0,0,255))
        #dummy pixel to be replaces with 
        #actual pixel