#a filter that turns the white background
#into trans
from PIL import Image
import numpy as np
im=Image.open("image.jpg")
im_array=np.asarray(im)
arr_shape=im_array.shape
HEIGHT=arr_shape[0]
WIDTH=arr_shape[1]
print(im_array.dtype)
arr_filtered=np.zeros((HEIGHT,WIDTH,4),np.uint8)
for i in range(HEIGHT):
    for j in range(WIDTH):
        if np.array_equal(im_array[i,j],[255,255,255]):
            arr_filtered[i,j]=[255,0,0,255]
Image.fromarray(arr_filtered).show()
