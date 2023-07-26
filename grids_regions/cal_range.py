import json

with open('E:\waseda\learning\project\grids\points.json','r+') as g:
    data = json.load(g)
    for item in data:
        list = item['size']
        if list == []:
            item['range'] = [0,0]
        else:
            minsize = round(min(list))
            maxsize = round(max(list))
            item['range'] = [minsize,maxsize]
            print(item['range'])

with open('E:\waseda\learning\project\grids\points.json','w') as r:
    json.dump(data,r,indent=4)