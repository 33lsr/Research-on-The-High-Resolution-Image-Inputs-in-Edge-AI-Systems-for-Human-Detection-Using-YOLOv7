from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

img = Image.new(mode="RGB", color=(255, 255, 255), size=(13377,7526))

img.save('grids/img.jpg')