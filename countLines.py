import os
import sys
path = os.getcwd()
files = os.listdir(path)
thisFileNameSplit = sys.argv[0].split("\\")
thisFileName = thisFileNameSplit[len(thisFileNameSplit)-1]
thisFolderName = thisFileNameSplit[len(thisFileNameSplit)-2]
lineCount=0

print('---------------------------------------------------------')
print("python count lines of all files in this folder.")
print("Project : "+thisFolderName)
print('{:<40}|{:40}'.format("File name","Lines"))
print('---------------------------------------------------------')
for f in files:
    fileN = f
    x = fileN.split(".")
    if fileN != thisFileName:
        try : 
            num_lines = sum(1 for line in open(fileN))
            print('{:<40}|{:0}'.format(fileN,num_lines))
            lineCount = lineCount + num_lines
        except:
            print('{:<40}|{:40}'.format(fileN,"Can't read file"))
    else :
        pass
print('---------------------------------------------------------')
print("Total = "+str(lineCount))
print('---------------------------------------------------------')
