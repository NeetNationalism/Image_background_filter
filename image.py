#Given any image with white background 
#program returns an RGBA .png image
#with transparent background (A=1.0)
from PIL import Image
im=Image.open("image.jpg")
im_filtered=Image.new("RGBA",im.size)
for i in range(im.width):
    for j in range(im.height):
        c=im.getpixel((i,j))
        if c!=(255,255,255):
            im_filtered.putpixel((i,j),(c[0],c[1],c[2]))
im_filtered.save("image","png")