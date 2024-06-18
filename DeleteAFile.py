import os
import shutil

path = "Delete.txt"
path2 = "DeleteFolder"
try:
    #os.remove(path)
    #os.rmdir(path2) #Delete empty folder only
    shutil.rmtree(path2) #Careful!!! Dangerous function!!! Delete all file and dir
except FileNotFoundError:
    print("That file was not found!")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("You cannot delete that using that function!")
else:
    print(path2+" was deleted")