# copyfile()    =   copies contents of a file
# copy()        =   copyfile() + permission mode + destination can be a directory
# copy2()       = copy() + copies metadata (file's creation and modification times)

import shutil

shutil.copyfile('ReadAFile.txt','Copy.txt') #src,dst
shutil.copyfile('ReadAFile.txt','C:\\Users\\dang1\\OneDrive\\Desktop\\Copy2.txt') #src,dst
shutil.copy('ReadAFile.txt','C:\\Users\\dang1\\OneDrive\\Desktop\\Copy2.txt') #src,dst
shutil.copy2('ReadAFile.txt','C:\\Users\\dang1\\OneDrive\\Desktop\\Copy2.txt') #src,dst
