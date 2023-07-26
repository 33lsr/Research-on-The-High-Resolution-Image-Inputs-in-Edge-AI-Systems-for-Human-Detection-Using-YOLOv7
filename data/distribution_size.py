'''
evaluate
'''

import json
import numpy as np
import matplotlib.pyplot as plt

#start
json_input = 'E:/waseda/learning/project/dataset/02_annotation_modified.json'

def get_data(json_input):
    with open(json_input,'rb') as f:
        
        #load data
        data = json.load(f)
        size = []
        location_xlist = []
        location_ylist = []
         
        for object in data['annotations']:

            #location_width
            location_x = object['bbox'][0]
            location_xlist.append(location_x)

            #location_height
            location_y = 15052 - object['bbox'][1]
            location_ylist.append(location_y)

            #size
            size.append(object['human_size'])

    f.close
    return(location_xlist,location_ylist,size)

def draw(x,y,size):
    plt.scatter(x, y, alpha=0.4, s=size)
    plt.xlabel('Location(x) in image')
    plt.ylabel('Location(y) in image')
    plt.xlim((0, 26753))
    plt.ylim((0, 15052))
    plt.show()

x,y,size = get_data(json_input) 
#draw(x,y,size)
#size.sort()
result = []
for idx,val in enumerate(size):
    if val <   750:
        result.append(int(y[idx]))
result.sort()
result.reverse()
print(result)
print(max(result),min(result))
#print(size)

