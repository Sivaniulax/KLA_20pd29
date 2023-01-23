import numpy as np
'''
class polygon:
    def PolyArea(x,y):
        return 0.5*np.abs(np.dot(x,np.roll(y,1))-np.dot(y,np.roll(x,1)))
'''
fp1 = open("POI_2.txt","r+") 
fp2 = open("Source_2.txt","r+") 
outputFile = open('mile2.txt', 'w')
poi = fp1.readlines()
source = fp2.readlines()

#write header info and store other details
for i in poi:
    if "boundary" in i:
        bound = i
    elif "layer" in i:
        lay = i
    elif "datatype" in i:
        dtype = i
    elif "xy" in i:
        x_y = i
    elif "endel" in i:
        end_ = i
    elif "endstr" not in i and "endlib" not in i:
        print(i,end = '', file = outputFile)

fp1.close()

   


outputFile.close()

fp2.close()
