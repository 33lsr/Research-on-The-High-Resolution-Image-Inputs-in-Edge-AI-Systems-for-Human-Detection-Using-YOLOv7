import os
import json
from tkinter.tix import ButtonBox

json_output = 'E:/waseda/learning/project/person-2/64prediction.json'
output=[]

f = open("E:/waseda/learning/project/person-2/person_2_64.txt")
for line in f:
    list = line.split()
    a=float(list[1])
    b=float(list[2])
    c=float(list[3])
    d=float(list[4])
    imgw=1920
    imgh=1080
    
    x=(a-0.5*c)*imgw
    y = (b-0.5*d)*imgh
    w= imgw*c
    h=imgh*d

    instance = {}
    instance["image_id"] = "person_2_64"
    instance["category_id"] = 0
    instance["bbox"] = [x,y,w,h]
    instance["score"] = 1
    output.append(instance)


with open(json_output,'w') as r:
    json.dump(output,r,indent=4)
r.close()