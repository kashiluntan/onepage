from PIL import Image
import os
import PIL
import glob

size = 100

images = [file for file in os.listdir() if file.endswith(('jpeg', 'png', 'jpg'))]
for image_name in images:
    img = Image.open(image_name)
    image = img.resize((100, 100), PIL.Image.NEAREST)
    image.save(image_name)
	
