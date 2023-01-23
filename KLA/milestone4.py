import numpy as np
import math

outputFile = open('mile4.txt', 'w') 

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
 
def cal(x_y,no_of_coordinates):
    arr = Convert(x_y)
    no_of_coordinates1 = int(arr[1])
    if no_of_coordinates1 not in  no_of_coordinates:
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
fp1 = open("POI4.txt","r+") 
fp2 = open("Source4.txt","r+") 

poi = fp1.readlines()
source = fp2.readlines()

#write header info and store other details
test = []
no_of_coordinates = []
for i in poi:
    if "xy" in i:
        x_y = i
        arr = Convert(x_y)
        no_of_coordinates.append(int(arr[1]))
        #print(no_of_coordinates)
        x = []
        y  = []
        for i in range(2,len(arr)):
            a,b = list(arr[i].split(" "))
            x.append(int(a))
            y.append(int(b))
        temp = Euclidean(x,y)
        test.append(temp)
print(test[0])
print(test[1])

i = 0
while(i!= len(source)):
    val = 0
    if "boundary" in source[i] and "layer" in source[i+1] and "datatype" in source[i+2] and "xy" in source[i+3] and "endel" in source[i+4]:
        bound = source[i]
        lay = source[i+1]
        dtype = source[i+2]
        x_y = source[i+3]
        end_ = source[i+4]
        test1 = cal(x_y,no_of_coordinates)
        print(i)
        if test1 != 0 and test1 in test:
            j = i+5
            if "boundary" in source[j] and "layer" in source[j+1] and "datatype" in source[j+2] and "xy" in source[j+3] and "endel" in source[j+4]:
                bound1 = source[j]
                lay1 = source[j+1]
                dtype1 = source[j+2]
                x_y1 = source[j+3]
                end_1 = source[j+4]
                test2 = cal(x_y1,no_of_coordinates)
                if test1 == test[0] and test2 == test[1] or test1 == test[1] and test2 == test[0]:
                    val = 1
                    print(bound,end = '', file = outputFile)
                    print(lay,end = '', file = outputFile)
                    print(dtype,end = '', file = outputFile)
                    print(x_y,end = '', file = outputFile)
                    print(end_,end = '', file = outputFile)
                    print(bound1,end = '', file = outputFile)
                    print(lay1,end = '', file = outputFile)
                    print(dtype1,end = '', file = outputFile)
                    print(x_y1,end = '', file = outputFile)
                    print(end_1,end = '', file = outputFile)
                    i+=10
                
        if val == 0:
            i+=5
    else:
        print(source[i],end = '', file = outputFile)
        i+=1    


    
    
    

fp1.close()
outputFile.close()
fp2.close()
