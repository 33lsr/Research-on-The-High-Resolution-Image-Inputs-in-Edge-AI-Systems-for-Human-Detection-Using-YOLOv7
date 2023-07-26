#get height  range
import os
import json

json_input = 'E:/waseda/learning/project/person-10/predictions.json'  

list = []

#get data in input
#only read
with open(json_input,'r') as f:
        

    #load data
    data = json.load(f)
    for instance in data:
            h = instance['bbox'][3]
            list.append(h)

#list.sort()
print(max(list),min(list))
f.close()   

