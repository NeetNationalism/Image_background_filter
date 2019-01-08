#a filter that turns the white background
#into trans
from PIL import Image
import numpy as np
im=Image.open("image.jpg")
im_array=np.asarray(im)
arr_shape=im_array.shape
HEIGHT=arr_shape[0]
WIDTH=arr_shape[1]
arr_filtered=np.zeros((HEIGHT,WIDTH,4),np.uint8)

def is_not_color(x,c=[255,255,255]):
    #return True if x color is NOT he same as c 
    #else return False
    #default is white
    value=0
    for i in range(3):
        value+=c[i]-x[i]
    return value>150
 
for i in range(HEIGHT):
    for j in range(WIDTH):
        if is_not_color(im_array[i,j]):
            arr_filtered[i,j,:3]=im_array[i,j]
            arr_filtered[i,j,3]=255
Image.fromarray(arr_filtered).show()
