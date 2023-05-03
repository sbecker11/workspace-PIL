# image_resizer - a python script that resizes a directory of image files  

## OpenAI
Most of this code was actually written by **OpenAI** from this request:

    "Write a python app that takes src_folder, dst_folder, new pixel_width,  
    and dst_file_prefix as command line parameters. Read all gif, jpg and png   
    files from src_folder, resize each image to have the same new pixel   
    width, and write each resized image to the dst_folder with its filename
    prefixed with the given dst_file_oprefix."


## Installation:
    % python3.9 -m venv venv
    % source venv/bin/activate
    % pip import -r requirements

## Usage:
    % python image_resizer.py 
    USAGE: python image_resizer.py <src_folder> <dst_folder> <new_pixel_width> <dst_file_prefix>

## Functionality: 
image_resizer is a python script that:  
1. takes a src_folder, dst_folder, new pixel_width and a dst_file_prefix  
1. reads all gif, jpg and png file_names from src_folder,  
1. resizes each to have the new pixel width,  
2. writes each resized image to (dst_file prefix + file_name) to the dst_folder  

## Cavaets:  
Unfortunately, the resized version of any animated gif file is not animated.

