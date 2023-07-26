import os
import json


json_dir = 'E:/waseda/learning/project/dataset/02_annotation_modified_rate2.json'  # json
out_dir = 'E:/waseda/learning/project/dataset/txtoutput/'  #txt

def main():
    # json 
    with open(json_dir, 'r') as load_f:
        data = json.load(load_f)

    for imginfo in data['images']:
        tmp = imginfo['file_name'].split('.')
        filename = out_dir + tmp[0] + '.txt'
        imgid = imginfo['id']
        if os.path.exists(filename):
            fp = open(filename, mode="a+")
            # 相对坐标
            for instance in data['annotations']:
                if instance['image_id'] == imgid :
                    x = (instance['bbox'][0] + (instance['bbox'][2] *0.5)) / imginfo['width']
                    y = (instance['bbox'][1] + (instance['bbox'][3] *0.5))  / imginfo['height']
                    if x>1:  x = 1
                    if y>1:  y = 1
                    if x<0:  x = 0
                    if x<0:  x = 0
                    w = instance['bbox'][2] / imginfo['width']
                    h = instance['bbox'][3] / imginfo['height']
                    
                    instance_str = str(instance['category_id']) + ' ' + str('%.6f' % x) + ' ' + str('%.6f' % y) + ' ' + str('%.6f' % w) + \
                            ' ' + str('%.6f' % h)
                    line_data = fp.readlines()
                    #if len(line_data) != 0: #有内容
                        #fp.write('\n' + instance_str)
                    #else:
                    fp.write(instance_str+ '\n' )
                    
            #fp.close()
                

        else:
            fp = open(filename, mode="w")
            fp.close()


if __name__ == '__main__':
    main()