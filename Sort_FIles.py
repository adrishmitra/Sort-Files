import os
import shutil

import easygui
import eel

eel.init('UI')

#region True/False 
# def bool_check(x):
#     if(x == "True" or x == "true" or x == "1"):
#         return(True)
#     elif(x == "False" or x == "false" or x == '0'):
#         return(0)
#     else:
#         print("Wrong Input! ")
#         main()
#endregion

@eel.expose
def main():
    dir = easygui.diropenbox()
    os.chdir(dir)
    return dir

@eel.expose
def mkdir(dictionary_obj, x):
    directories = ['','','','','','']
    dir = x
    os.chdir(dir)

    for j in range(6):
        file_type = dictionary_obj[j]
        if(file_type[1] == True):
            command = 'mkdir ' + file_type[0]
            directories[j] = dir + '\\' + file_type[0]
            print(directories[j])
            try:
                os.system(command)
            except:
                print("Initializing...")
    return directories

@eel.expose
def move(path, direc):
    files_list = os.listdir(path) # Array of files

    zip_dir = direc[0]
    img_dir = direc[1]
    app_dir = direc[2]
    vid_dir = direc[3]
    mp3_dir = direc[4]
    doc_dir = direc[5]
    

    # Looping through file 
    for i in files_list:
        ext = os.path.splitext(i)[1]
        ### APPLiCATIONS ####
        if(ext == '.exe' and app_dir != ''):
            print(ext, app_dir)
            shutil.move(i, app_dir)
            otpt = "Moved " + i + " to Applications folder"
            print(otpt)

        #### IMAGES ####
        if(ext == '.png' or ext == '.jpg' or ext == '.jpeg' or ext == '.webp' and img_dir != ''):
            shutil.move(i, img_dir)
            otpt = "Moved" + i + "to Images folder"
            print(otpt)

        #### VIDEOS ####
        if(ext == '.mp4' or ext == '.mkv' or ext == '.avi' and vid_dir != ''):
            shutil.move(i, vid_dir)
            otpt = "Moved" + i + "to Videos folder"
            print(otpt)

        #### ZIP FILES ####
        if(ext == '.zip' or ext == '.rar' and zip_dir != ''):
            shutil.move(i, zip_dir)
            otpt = "Moved" + i + "to Zip folder"
            print(otpt)

        #### MUSIC ####
        if(ext == '.mp3' and mp3_dir != ''):
            shutil.move(i, mp3_dir)
            otpt = "Moved" + i + "to Music folder"
            print(otpt)

        #### PDF FILES ####
        if(ext == '.pdf' or ext == '.docx' or ext == '.xlsx' or ext == '.txt' and doc_dir != ''):
            shutil.move(i, doc_dir)
            otpt = "Moved" + i + "to Docs folder"
            print(otpt)
        
eel.start('index.html', size= (1000, 850))
