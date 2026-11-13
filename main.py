import os

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
    folder_list = []
    for x in os.listdir(folder):
        extension = x[-4:]
        folder_name = file_extensions.get(extension)
        if extension not in folder_list:
            folder_list.append(extension)
            try:
                os.mkdir(f"{folder}\\{folder_name}")
            except OSError as e:
                print ("Error: ", e)

def organize_files(folder):
    for x in os.listdir(folder):
        if x.endswith(".pdf"):
            shutil.move(folder, f"{folder}{folder_name}")
        elif x.endswith(".jpg"):

        elif x.endswith(".txt"):

        else x.endswith(".zip"):


def main():
    print("Hello, choose the correct path to organize:")
    folder = input()
    if check_folder(folder) == 1:
       exit()
    make_folders(folder)
    organize_files(folder)

main()
