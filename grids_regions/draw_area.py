from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os
import json

input_img = r'E:/waseda/learning/project/grids/grid_geocoding_img.jpg'

(filepath,filename) = os.path.split(input_img)
img = Image.open(input_img)
img_d = ImageDraw.Draw(img)
x_len, y_len = img.size


with open('E:/waseda/learning/project/grids/points.json','rb') as f:
  
    #load data
    data = json.load(f)
    for item in data:
        #x,y=item['id']
        content = str(item['range'])
        #img_d.text(((x-1)*640+100,(y-1)*640+100),content,fill=(255,0,0),font=font)
        if item['range'] == [0,0]:
            for x in range(item['area'][0],item['area'][1]):
                for y in range(item['area'][2],item['area'][3]):
                    if x > 13376: x=13376
                    if y > 7525: y= 7525
                    img.putpixel((x,y),(128,128,128))

        if item['range'][0] < 128:        #if item['range'][0] < 128:
            for x in range(item['area'][0],item['area'][1]):
                for y in range(item['area'][2],item['area'][3]):
                    if x > 13376: x=13376
                    if y > 7525: y= 7525
                    img.putpixel((x,y),(255,0,0))

        if 128 <= item['range'][0] < 256:
            for x in range(item['area'][0],item['area'][1]):
                for y in range(item['area'][2],item['area'][3]):
                    if x > 13376: x=13376
                    if y > 7525: y= 7525
                    img.putpixel((x,y),(255,125,0))

        if 256 <= item['range'][0] < 512:
            for x in range(item['area'][0],item['area'][1]):
                for y in range(item['area'][2],item['area'][3]):
                    if x > 13376: x=13376
                    if y > 7525: y= 7525
                    img.putpixel((x,y),(255,255,0))       

        if 512 <= item['range'][0] < 1024:
            for x in range(item['area'][0],item['area'][1]):
                for y in range(item['area'][2],item['area'][3]):
                    if x > 13376: x=13376
                    if y > 7525: y= 7525
                    img.putpixel((x,y),(0,255,0))

        if item['range'][0] >= 1024:
            for x in range(item['area'][0],item['area'][1]):
                for y in range(item['area'][2],item['area'][3]):
                    if x > 13376: x=13376
                    if y > 7525: y= 7525
                    img.putpixel((x,y),(0,0,255))

img.save(os.path.join(filepath, "area_"+filename))