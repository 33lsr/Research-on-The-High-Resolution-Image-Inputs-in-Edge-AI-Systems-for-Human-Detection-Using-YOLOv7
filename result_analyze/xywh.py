from numpy import *
#bbox gt
#gt = [x,y,w,h]
#bbox = [xb,yb,wb,hb]
#label(中心点xy+相对wh)-->annotation(左上xy+像素值wh)
'''
a=0.2265625
b=0.4476309226932668
c=0.03125
d=0.12219451371571072
imgw=640
imgh=401

x=(a-0.5*c)*imgw
y = (b-0.5*d)*imgh
w= imgw*c
h=imgh*d
print(x)
print(y)
print(w)
print(h)
'''
list_size = []
#read txt method two
f = open("E:/waseda/learning/project/person-dataset-11000(1)/person-dataset-11000/labels/test/person_2_64.txt")
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
    bbox_list =[x,y,w,h]
    #list1=[a,b,c,d]
    list_size.append(d*640)
    print(bbox_list)

#print(mean(list_size))