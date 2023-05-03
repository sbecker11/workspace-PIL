# image_resizer - a python script that resizes a directory of image files  

## OpenAI
Most of this code was actually written by **OpenAI** from this request:

    "Write a python app that takes src_folder, dst_folder, new pixel_width, and dst_file_prefix as command line parameters. Read all jpg and png files from src_folder, resize each image to have the ame new pixel width, and write each resized image a file to the dst_folder prefixed with the given dst_file_oprefix."


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
1. reads all gif, jpg and png files from src_folder,   
1. resizes each to have the new pixel width,   
1. writes each resized image to dst_file in the dst_folder   
1. with prefix added to dst file  

## Attention:
This module uses the images2gif module which is  
Copyright (C) 2012, Almar Klein, Ant1, Marius van Voorden  
    
## Bugs:  
Unfortunately, gif file resizing functionality is currently failing.

