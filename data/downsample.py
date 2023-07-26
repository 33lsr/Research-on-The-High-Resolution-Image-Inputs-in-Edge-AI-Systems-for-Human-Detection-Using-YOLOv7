

import cv2
import os

file_path = 'E:/waseda/learning/project/dataset/coco/val'
image_list = []
for filename in os.listdir(file_path):
    image_list.append(filename)
    
    input_path = 'E:/waseda/learning/project/dataset/coco/val/'+filename
    #print(input_path)
    original_image = cv2.imread(input_path)
    img_1 = cv2.pyrDown(original_image)
    output_path = 'E:/waseda/learning/project/dataset/coco/val_rate2/'+filename
    cv2.imwrite(output_path,img_1)
