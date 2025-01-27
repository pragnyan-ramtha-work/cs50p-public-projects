import sys
from PIL import Image

images = []

for arg in sys.argv:
    image = image.open(arg)
    image.append(image)

image[0].save(
    "cat.gif"

)   
