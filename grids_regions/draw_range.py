path='grids/IMG_02_01'

# -*- coding: utf-8 -*-

from tkinter.font import Font
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os
import json

input_img = r'grids\img.jpg'

# 生成
(filepath,filename) = os.path.split(input_img)
img = Image.open(input_img)
img_d = ImageDraw.Draw(img)
x_len, y_len = img.size
x_step = 640
y_step = 640
#print x_len
#print y_len
for x in range(0, x_len, x_step):
    img_d.line(((x, 0), (x, y_len)), (0,100,255),width=10)
for y in range(0, y_len, y_step):
    img_d.line(((0, y), (x_len, y)), (0,100,255),width=10)
#img.save(os.path.join(filepath,"grid_"+filename) )

# 编码 
cnt = 1
font = ImageFont.truetype('E:/waseda/learning/project/grids/arial.ttf', size = 100)
for i in range(0,x_len,x_step):
    img_d.text((i+300,200), str(cnt),fill=(0,100,255),font=font)
    cnt+=1
cnt = 2
for j in range(y_step,y_len,y_step):
    img_d.text((300,j+200), str(cnt),fill=(0,100,255),font=font)
    cnt+=1
#img.save(os.path.join(filepath, "grid_geocoding_"+filename))

with open('E:/waseda/learning/project/grids/points.json','rb') as f:
  
    #load data
    data = json.load(f)
    for item in data:
        x,y=item['id']
        content = str(item['range'])
        #img_d.text(((x-1)*640+100,(y-1)*640+100),content,fill=(255,0,0),font=font)


#img.save(os.path.join(filepath, "grid_geocoding_"+filename))