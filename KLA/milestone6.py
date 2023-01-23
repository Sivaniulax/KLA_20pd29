import numpy as np
import math

outputFile = open('mile6.txt', 'w') 

def PolyArea(x,y):
    return 0.5*np.abs(np.dot(x,np.roll(y,1))-np.dot(y,np.roll(x,1)))

def computeangle(x,y):
    res = []
    for i in range(len(x)-2):
        a = np.array([x[i],y[i]])
        b = np.array([x[i+1],y[i+1]])
        c = np.array([x[i+2],y[i+2]])

        ba = a - b
        bc = c - b
        cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
        angle = np.arccos(cosine_angle)
        res.append(angle)
    res = sorted(res)
    return res


    

def Euclidean(a,b):
    temp = []
    for i in range(len(a)-1):
        Px = a[i]
        Py = b[i]
        Qx = a[i+1]
        Qy = b[i+1]
        dis = math.dist([Px, Py], [Qx, Qy])
        temp.append(dis)
    temp = sorted(temp)
    return temp   
 
def cal(x_y):
    arr = Convert(x_y)
    no_of_coordinates1 = int(arr[1])
    if no_of_coordinates != no_of_coordinates1:
        return 0 
    x = []
    y  = []
    for i in range(2,len(arr)):
        a,b = list(arr[i].split(" "))
        x.append(int(a))
        y.append(int(b))
    test1 = Euclidean(x,y)
    
    return x,y,test1
    


def Convert(string):
    li = list(string.split("  "))
    return li
fp1 = open("POI6.txt","r+") 
fp2 = open("Source6.txt","r+") 

poi = fp1.readlines()
source = fp2.readlines()

#write header info and store other details
for i in poi:
    if "xy" in i:
        x_y = i
    



arr = Convert(x_y)
no_of_coordinates = int(arr[1])
x,y,test = cal(x_y)
area = PolyArea(x,y)
angle = computeangle(x,y)
#print(area)
#print("Test:",test)

i = 0
while(i!= len(source)):
    
    if "boundary" in source[i] and "layer" in source[i+1] and "datatype" in source[i+2] and "xy" in source[i+3] and "endel" in source[i+4]:
        bound = source[i]
        lay = source[i+1]
        dtype = source[i+2]
        x_y = source[i+3]
        end_ = source[i+4]
        #print(x_y)
        x,y,test1 = cal(x_y)
        area1 = PolyArea(x,y)
        angle1 = computeangle(x,y)
        if test == test1 and area == area1 and angle == angle1:
            print(bound,end = '', file = outputFile)
            print(lay,end = '', file = outputFile)
            print(dtype,end = '', file = outputFile)
            print(x_y,end = '', file = outputFile)
            print(end_,end = '', file = outputFile)
        i+=5
    else:
        print(source[i],end = '', file = outputFile)
        i+=1
    
        

fp1.close()
outputFile.close()
fp2.close()
