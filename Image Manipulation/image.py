from PIL import Image, ImageFilter
import os

# Displaying images

image1 = Image.open("h1.jpeg")
image1.show()

# For saving images in different format
image1.save("h1.png")


# Convert all images into png

for f in os.listdir('.'):
    if f.endswith('.jpeg') or f.endswith('.jpg'):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)
        i.save('PNG/{}.png'.format(fn))

# Resize all images

size_300 = (300,300)
for f in os.listdir('.'):
    if f.endswith('.jpeg') or f.endswith('.jpg'):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)
        i.thumbnail(size_300)
        i.save('Image_300x300/{}.jpg'.format(fn,fext))

# Rotate image

img2 = Image.open('h2.jpg')
img2.rotate(90).save('rotate_image.jpg')

# Make image black & white

img3 = Image.open('h3.jpeg')
img3.convert(mode='L').save('bnw_image.jpg')

# Make image black & white

img4 = Image.open('h4.jpeg')
img4.filter(ImageFilter.GaussianBlur(15)).save('blurred_image.jpg')
