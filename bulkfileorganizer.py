import os, shutil

path = r"C:/bulkorgtest/"
file_name = os.listdir(path)
print(file_name)

folder_name = ['image files','pdf files']

for loop in range (0,2):
    if not os.path.exists(path + folder_name[loop]):
        print(path + folder_name[loop])
        os.makedirs(path + folder_name[loop])
    
for file in file_name:
    if ".png" in file and not os.path.exists(path + "image files/" + file):
        shutil.move(path + file,path + "image files/" + file)
    elif ".pdf" in file and not os.path.exists(path + "pdf files/" + file):
        shutil.move(path +  file,path +"pdf files/" + file)
