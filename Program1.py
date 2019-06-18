from PIL import Image

img = Image.open('pic_python.jpeg')
print(img)

width,height = img.size
print(width,height)
print(img.format)
print(img.info)
print(img.width)
print(img.height)
print(img.mode)

img.save("original_img.jpeg")

rotated_img = img.rotate(90)
rotated_img.save("rotated_img.jpeg")

area = (0,0,img.width/2,img.height/2)
cropped_img = img.crop(area)
cropped_img.save("cropped_img.jpeg")

width,height = img.size
resized_img = img.resize((int(width/2),int(height/2)))
resized_img.save("resized_img.jpeg")


img2 = Image.open("pic_python2.jpeg")
print(img2.size)
resized_img2 = img2.resize(((img.width),(img.height)))
resized_img2.save("resized2ndImg.jpeg")
img.paste(resized_img2,(100,100))
img.save("pasted_img.jpeg")

img = Image.open("pic_python.jpeg")
print(img.histogram())

transposed_img = img.transpose(Image.FLIP_TOP_BOTTOM)
transposed_img.save("transposed_img.jpeg")

print(img.split())

