from http.client import OK
import json

#input = 'grids/02_annotation_modified_rate2.json'
#file_path ='E:\waseda\learning\project\grids\points.json'
input_path = 'grids/02_annotation_modified_rate2.json'
file_path = 'E:\waseda\learning\project\grids\points.json'
m=640

with open(input_path,'rb') as f:
    data1 = json.load(f)

    with open(file_path,'r+') as g:
        data2 = json.load(g)

        for instance in data1['annotations']:
            x_center = instance['bbox'][0]+0.5*instance['bbox'][2]
            y_center = instance['bbox'][1]+0.5*instance['bbox'][3]
            center=[x_center,y_center]
            x_id = (x_center//m) + 1
            y_id = (y_center//m) + 1
            human_size = instance['human_size']
            #print('yes')
            for point in data2:
                if [x_id,y_id] == point["id"] :
                    point['size'].append(human_size)
                    
                    #print(isinstance(list_size,list))
                    #print('yes')
                    with open(file_path,'w') as r:
                        json.dump(data2,r,indent=4)
                    
                
