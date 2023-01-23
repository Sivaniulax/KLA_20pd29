import numpy as np
import math

outputFile = open('mile2.txt', 'w') 

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
    
    return test1
    


def Convert(string):
    li = list(string.split("  "))
    return li
fp1 = open("POI_2.txt","r+") 
fp2 = open("Source_2.txt","r+") 

poi = fp1.readlines()
source = fp2.readlines()

#write header info and store other details
for i in poi:
    if "xy" in i:
        x_y = i
    



arr = Convert(x_y)
no_of_coordinates = int(arr[1])
test = cal(x_y)
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
        test1 = cal(x_y)
        if test == test1:
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
