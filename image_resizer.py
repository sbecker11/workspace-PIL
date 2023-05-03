import os
import sys
from pathlib import Path
from PIL import Image


def resize_img_file(src_file:Path, dst_file:Path,  new_pixel_width:int):

    # Open img using Pillow from src_file
    img = Image.open(src_file)
    
    # Calculate new height while preserving aspect ratio
    width, height = img.size
    aspect_ratio = height / width
    new_height = round(new_pixel_width * aspect_ratio)
    
    # Resize the img
    resized_img = img.resize((new_pixel_width, new_height), Image.ANTIALIAS)
    
    # save the resized img to dst_file
    resized_img.save(dst_file)

    
def resize_img_files(src_folder:str, dst_folder:str, new_pixel_width:int, dst_file_prefix: str="r_") -> None:
    """
    takes a src_folder, dst_folder, new pixel_width and a prefix
    reads all gif, jpg and png files from src_folder, resizes each
    to have the new pixel width, and write each resized image to 
    a file in the dst_folder with prefix added to the dst filename.
    """
    
    src_folder_path = Path(src_folder)
    dst_folder_path = Path(dst_folder)
    
    # gather src_file Paths that end with suffixes
    suffixes = [".gif",".jpg",".png"]
    src_files = [src_file for suffix in suffixes for src_file in src_folder_path.glob(f"*{suffix}")]
    for src_file in src_files:
        
        # skip files that have already been resized
        if src_file.name.startswith(dst_file_prefix):
            continue
              
        # define the dst_file Path          
        dst_file = Path(dst_folder_path / (dst_file_prefix + src_file.name))
        
        # Read img from src_file, resize img, and save srsized img to dst_file
        resize_img_file(src_file, dst_file, new_pixel_width)
        
        print(f"img:{src_file.name} -> {dst_file.name}")

if __name__ == '__main__':
    if len(sys.argv) != 5:
        print(f"USAGE: python {sys.argv[0]} <src_folder> <dst_folder> <new_pixel_width> <dst_file_prefix>")
        sys.exit(-1)

    # Get command line arguments
    src_folder_path = sys.argv[1]
    dst_folder_path = sys.argv[2]
    new_pixel_width = int(sys.argv[3])
    dst_file_prefix = sys.argv[4]

    resize_img_files(src_folder_path, dst_folder_path, new_pixel_width, dst_file_prefix)
    
    print("done")
