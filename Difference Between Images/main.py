from PIL import Image, ImageChops

# The ImageChops module contains a number of arithmetical image operations, called channel operations (“chops”)
# These can be used for various purposes, including special effects, image compositions, algorithmic painting, and more.

# Creating image objects with Image

img1 = Image.open("1.jpg")
img2 = Image.open("2.jpg")


# Getting the difference between images

diff = ImageChops.difference(img1, img2)

# Now showing the differences

if diff.getbbox():
    diff.show()