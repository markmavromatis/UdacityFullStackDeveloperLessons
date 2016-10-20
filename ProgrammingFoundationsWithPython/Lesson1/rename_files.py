import os
import re

def get_filenames():
    folder = "./prank_after"
    all_files = os.listdir(folder) # current directory
    print all_files
    
def rename_files():

    print "Inside rename_files"
    # 1) Get file names from folder
    folder = "./prank_after"
    all_files = os.listdir(folder) # current directory
    # 2) Iterate over each file
    for each_file_name in all_files:        
        # 3) Get the name of the file
        oldName = each_file_name
        # 4) Remove numbers
        # In the demo, they use the string translate() method.
        newName = "".join(re.findall("[a-zA-Z\.]+", oldName))
        # 5) Rename file to new name
        print oldName + " " + newName
        os.rename(os.path.join(folder, oldName), os.path.join(folder, newName))
        
# rename_files();
get_filenames()
