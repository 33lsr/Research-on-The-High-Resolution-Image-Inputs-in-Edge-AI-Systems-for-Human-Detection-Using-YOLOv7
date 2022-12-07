'''
delete object other than person
calculate human size
write in a new json file
'''

import json

#set path
json_input = '01_annotation.json'
json_output = '01_annotation_modified.json'

dict={}

#get data in input
def get_json_data(json_input):
    #only read
    with open(json_input,'rb') as f:
  
        #load data
        data = json.load(f)
        
        
        for frame in data:

            del_list = []
            for object in data[frame]['objects list']:
                
                #Delete objects other than person
                if object['category'] != 'person': 
                    del_list.append(object)

                #Calculate human size
                if object['category'] == 'person':
                    image_height = data[frame]['image size']['height']
                    human_size = image_height *(object['rects']['full body']['br']['y'] - object['rects']['full body']['tl']['y'])
                    object['human size'] = human_size    

            for  del_object in del_list:
                data[frame]['objects list'].remove(del_object)
        

    dict = data         
 
    f.close()   
    return dict

#write json    
def write_json_data(dict):
    with open(json_output,'w') as r:
        json.dump(dict,r,indent=4)
    r.close()

#main
the_revised_dict = get_json_data(json_input)
write_json_data(the_revised_dict)

