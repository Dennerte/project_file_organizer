import os
import shutil
import sys

file_extensions = {
    ".pdf": "Document",
    ".jpg": "Photo",
    ".txt": "Textfile",
    ".zip": "Compressed"
}

def check_folder(folder):
    if os.path.exists(folder):
        print("Your folder is: " + folder)
        return 0
    else:
        print("Folder location not found")
        return 1

def make_folders(folder):
    folder_list = list()
    for x in os.listdir(folder):
        extension = os.path.splitext(x)
        if extension[1] not in file_extensions.keys():
            continue
        folder_name = file_extensions.get(extension[1])
        if extension[1] not in folder_list:
            folder_list.append(extension[1])
            try:
                os.mkdir(os.path.join(folder, folder_name))
            except OSError as e:
                print ("Error: ", e)

def organize_files(folder):
    for x in os.listdir(folder):
        extension = os.path.splitext(x)
        if extension[1] not in file_extensions.keys():
            continue
        folder_name = file_extensions.get(extension[1])
        src = os.path.join(folder, x)
        dst = os.path.join(folder, folder_name, x)
        shutil.move(src, dst)

def main(argv):
    if len(argv) > 1 and argv[1] != "--dry-run":
        print("Invalid action: " + argv[1])
        print("Only valid action: --dry-run\nExiting Now!")
        exit()
    print("Hello, choose the correct path to organize:")
    folder = input()
    if check_folder(folder) == 1:
       exit()
    make_folders(folder)
    organize_files(folder)

main(sys.argv)
