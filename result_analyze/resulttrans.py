import os
import json

json_input = 'E:/waseda/learning/project/person-1/person-1_perdictions.json'  # json
json_output = 'E:/waseda/learning/project/person-1/predictions.json'  # 输出的 txt 

list = []


#get data in input
def get_json_data(json_input):
    #only read
    with open(json_input,'rb') as f:
        

        #load data
        data = json.load(f)
        for instance in data:
            #instance['image_id'] = int(instance['image_id'][-2:])
            if instance['category_id'] ==1: #only person
                #instance['category_id'] = 0
                
                list.append(instance)

    f.close()   
    return list

    #write json    
def write_json_data(dict):
    with open(json_output,'w') as r:
        json.dump(list,r,indent=4)
    r.close()

#main
the_revised_dict = get_json_data(json_input)
write_json_data(the_revised_dict)