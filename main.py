
from rembg import remove

from PIL import Image

image_path = 'coolest-car/coolest-car.jpg'
image_path_removebg = 'coolest-car/coolest-car.png'

taking_image = Image.open(image_path)
giving_image = remove(taking_image)
giving_image.save(image_path_removebg)