'''
John Griffin Harrington
Searching for Digital Images
September 18, 2020
'''
import os
from PIL import Image
from prettytable import PrettyTable


directory = input("Please enter a directory:\n")
table = PrettyTable(['Image?', 'File', 'FileSize', 'Ext', 'Format', 'Width', 'Height', 'Type'])

if not (os.path.isdir(directory)):
    directory = input("Seriously a directory only please:\n")

fileList = os.path.abspath(directory)
with os.scandir(fileList) as dirs:
    for eachFile in dirs: 
        try: 
            absPath = os.path.abspath(eachFile)
            ext = os.path.splitext(absPath)[1]
            fileSize = '{:,}'.format(os.path.getsize(absPath))
        except:
            continue
        
        try:
            with Image.open(absPath) as im:
                imStatus = 'Yes'
                imFormat = im.format
                imType = im.mode
                imWidth = im.size[0]
                imHeight = im.size[1]
                
                table.add_row([imStatus, absPath, fileSize, ext, imFormat, imWidth, imHeight, imType])
        except:
            imStatus = 'NO'
            table.add_row([imStatus, absPath, fileSize, ext, 'NA', 'NA','NA','NA'])
    
table.align = 'l'
print(table.get_string())
