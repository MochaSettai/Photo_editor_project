# Pillow Library link
# https://pillow.readthedocs.io/en/stable/
from PIL import Image, ImageEnhance, ImageFilter
import os

# defines the path of image folders
path = './imgs'
pathOut = '/editedImgs'

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    # converts the images to greyscale and sharpens the images
    edit = img.convert('L').filter(ImageFilter.SHARPEN)

    # adds contrast to the images by a factor of provided value
    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)

    clean_name = os.path.splitext(filename)[0]

    edit.save(f'.{pathOut}/{clean_name}_edited.jpg')
