# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 20:45:54 2021

@author: SNB
"""

#Read an image

#Method 1 :
    
from PIL import Image as pl
from PIL import ImageDraw
from PIL import ImageEnhance 
import numpy as nm
from skimage import filters
from matplotlib import pyplot as plt
#from matplotlib import Image as im

#Read image using PIL

img = pl.open(r"E:\Shruti\Study\MBA\Sem-2\Analytics\Python\Data\Assignment -2 (NumPy)\fruits.png")
print(img.format)
print(img.size)
print(type(img))

print(img.mode)

#Store image data in array

img_arr = nm.asarray(img)
img_copy = nm.copy(img_arr)
print(img_arr)
print(img_arr.shape)
print(img_arr.dtype)

#Display Image
plt.imshow(img_arr[100:200, 100:512, :])

#Convert image into grey scale
img_gray = 255 - img_arr
#img_gray = nm.array(img.convert('L'))
#print(img_gray.shape)
#plt.imshow(img_gray)

#Image impact
img_double = img_arr * 2
img_half = img_arr / 3
#plt.imshow(img_double)
#plt.imshow(img_half)

#Create image from array
array_to_image = pl.fromarray(img_gray)
#array_to_image.show()
#array_to_image.save('E:\Shruti\Study\MBA\Sem-2\Analytics\Python\Data\Assignment -2 (NumPy)\GreyFruits.jpg')

#Change the value of Pixels 

#Red 
img_copy_R = nm.copy(img_arr)
img_copy_R[:,:,(1,2)] = 0

#Green
img_copy_G = nm.copy(img_arr)
img_copy_G[:,:,(0,2)] = 0

#Blue
img_copy_B = nm.copy(img_arr)
img_copy_B[:,:,(0,1)] = 0

#Concatenate all the R , G, B images
concatenate_image = nm.concatenate((img_copy_R,img_copy_G,img_copy_B), axis = 1)

plt.imshow(concatenate_image)

in_1,in_2,in_3,in_4 = nm.hsplit(img_arr, 4)
#concatenate_image = nm.concatenate((in_1,in_2,in_3,in_4), axis = 1)

#Split image into 3 components RGB
red, green, blue = img.split()
merge_image = pl.merge('RGB', (green,red,blue))
print(red.mode)
print(blue.mode)
print(green.mode)
print(merge_image.mode)
plt.imshow(merge_image)

#Image MAnipulations
#Image Filtering
edges = filters.sobel(img)
#plt.imshow(edges, cmap = 'gray')

#Get pixel value at certain position
print(img.getpixel((324,456)))

#Resize an image
resize_image = img.resize(1200,1200)
plt.imshow(resize_image)

#Thumbnail 
print(img.size)
img.thumbnail((400,400))
print(img.size)
plt.imshow(img)

#Image Enhance
img.Enhance = img.Contrast(img)
img.Enhance(1.8).show()

#Rotate image
img = img.rotate(180)
img.show()

img = img.rotate(90)
#plt.imshow(img)

#Brightening an image
bright_img = ImageEnhance.Brightness(img)
brightness = 1.5
bright_img = bright_img.enhance(brightness)
#plt.imshow(bright_img)

#Apply colors effect on image
Color_img = ImageEnhance.Color(img)
Color = 5
Color_img = Color_img.enhance(Color)
#plt.imshow(Color_img)

#Apply Contrast on image
Contrast_img = ImageEnhance.Contrast(img)
Contrast = 10
Contrast_img = Contrast_img.enhance(Contrast)
#plt.imshow(Contrast_img)

#Apply Sharpness on image
Sharpened_img = ImageEnhance.Sharpness(img)
Sharpness = 20
Sharpened_img = Sharpened_img.enhance(Sharpness)
#plt.imshow(Sharpened_img)

#Flip an image
#Method 1 :
flip_img = img.transpose(pl.FLIP_TOP_BOTTOM)
plt.imshow(flip_img)

#Method 2 :
img_arr_flip = nm.copy(img_arr)
for i in range(511):
    for j in range(511):
        img_arr_flip[i,j] = img_arr[i, 511-j]

plt.imshow(img_arr_flip)
    
#Drawing on an image
draw_img = ImageDraw.Draw(img)
draw_img.rectangle((70,50,160,240), outline = 'Black', fill = 'Yellow')
draw_img.text((75,65), 'Hello World', fill = 'green')
plt.imshow(img)

#Crop an image
width, height = img.size

#Setting points
left = 6
top = height/4
right = 200
bottom = 2 * height/4
cropped_img = img.crop((left,top,right,bottom))
plt.imshow(cropped_img)

#Make a black strip in an image
img_copy[0:512,50:90] = (0,0,0)
plt.imshow(img_copy)

#Negative transformation

#Read image pixel values and apply transformation
for i in range(0, img.size[0] - 1):
    for j in range(0, img.size[1] - 1):
        img_pixel = img.getpixel((i,j));
        
        negate_red_pixel = 255 - img_pixel[0]
        negate_green_pixel = 255 - img_pixel[1]
        negate_blue_pixel = 255 - img_pixel[2]
        
        img.putpixel((i,j), (negate_red_pixel, negate_green_pixel, negate_blue_pixel));
        
img.show()
    