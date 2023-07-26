import pickle
path='E:/waseda/learning/project/result/result.pkl'  
	   
f=open(path,'rb')
data=pickle.load(f)
 
print(data)
print(len(data))

