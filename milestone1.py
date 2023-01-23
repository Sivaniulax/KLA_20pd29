fp = open("Format_Source.txt","r+") 
outputFile = open('mile1.txt', 'w')

line = fp.readlines()
no_of_polygon = 2

for i in line:
    if "endel" in i:
        no_of_polygon -= 1
    print(i,end = '', file = outputFile)
    if no_of_polygon <=0:
        break


    
outputFile.close()
fp.close()

