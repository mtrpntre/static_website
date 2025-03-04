from textnode import *
from markdown_blocks import *
from inline_markdown import *
from htmlnode import *
from generate import *
import shutil
import os
import sys

dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"
default_basepath = "/"

def from_static_to_public(source_directory, destination_directory):

    os.makedirs(destination_directory, exist_ok=True)
    for item in os.listdir(source_directory):
        source_item = os.path.join(source_directory, item)
        destination_item = os.path.join(destination_directory, item)
        if os.path.isdir(source_item):
            from_static_to_public(source_item, destination_item)
        else:
            shutil.copy2(source_item, destination_item)


def delete_directory_content(directory):
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            shutil.rmtree(item_path)
        else:
            os.remove(item_path)

def main():

    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

   
    delete_directory_content(dir_path_public)
    from_static_to_public(dir_path_static, dir_path_public)
    generate_pages_recursive(dir_path_content, template_path, dir_path_public, basepath)
    print(basepath)
    


        
    
if __name__ == "__main__":
    main()
