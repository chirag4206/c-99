import os
import shutil
#os.system("date")
#os.getcwd()
source="C:/Users/chira/OneDrive/Documents/python/class-99/text1.txt"
destination="C:/Users/chira/OneDrive/Documents/python/class-99/backup"

#listOfFiles=os.listdir(source)
#for file in listOfFiles:
shutil.move(source,destination)
shutil.copy(source,destination)
os.listdir()