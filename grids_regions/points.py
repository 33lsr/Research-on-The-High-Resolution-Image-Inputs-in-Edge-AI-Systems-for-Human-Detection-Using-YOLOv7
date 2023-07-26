import json
#setpoints

output="E:/waseda/learning/project/grids/points.json"

m=640
imgh = 7680
imgw = 13377

grid_num_x = imgw//m+1
grid_num_y = imgh//m+1

points = []

for i in range(1,22): #xy
    for j in range(1,13): #y
        point={}
        point['id'] = [i,j]
        point['location'] = [(i-0.5)*m,(j-0.5)*m]
        point['area'] = [(i-1)*m,(j-1)*m,i*m,j*m]#left top，right bottom
        point['size'] = []
        points.append(point)

#print(grid_num_x,grid_num_y)
with open(output,'w') as r:
    json.dump(points,r,indent=4)