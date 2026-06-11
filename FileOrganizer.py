'''
Build a File Organizer using Python that can automatically sort and organize files on your system. 
The program can categorize files into folders such as Images, Documents, Videos, Music, and Others, 
making your workspace clean and efficient.
'''
# python3 "/Users/Admin/Documents/PYTHON/python project/FileOrganizer.py"
import os

def arrange_files(files, ext):
    files_with_ext = [file for file in files if file.endswith(ext)]
    print(files_with_ext)
    # i = 1
    # for file in files_with_ext:
    #     os.rename(file, f"photo-{i}{ext}")
    #     i+=1 
    if not(os.path.exists("images")):
        os.mkdir("images")
        
    for i, file in enumerate(files_with_ext): # enumerate() returns both the index and the value of the item in the list
        os.rename(file, f"images/photo-{i+1}{ext}")

if __name__=="__main__":
    files = os.listdir()
    arrange_files(files, ".png")
