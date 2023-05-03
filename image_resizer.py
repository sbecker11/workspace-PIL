import os
import sys
from PIL import Image
import images2gif

def resize_img_files(src_folder:str, dst_folder:str, new_pixel_width:int, dst_file_prefix: str="r_") -> None:
    """
    takes a src_folder, dst_folder, new pixel_width and a prefix
    reads all gif, jpg and png files from src_folder, resizes each
    to have the new pixel width, and write each resized image to 
    a file in the dst_folder with prefix added to the dst filename.
    """
    
    # Loop through files in folder
    for file_name in os.listdir(src_folder):
        
        # skip files that have already been resized
        if file_name.startswith(dst_file_prefix):
            continue
        
        # Check if file is GIF
        if file_name.endswith(".gif"):
            src_file_path = src_folder + '/' + file_name
            dst_file_path = dst_folder + '/' + dst_file_prefix + file_name
            gif_processed = images2gif.resize_gif_file(src_file_path, dst_file_path, new_pixel_width)
            print(f"gif_processed:{gif_processed}")
        else:
            # Check if file is a JPG or PNG image
            if file_name.endswith(".jpg") or file_name.endswith(".png"):
                # Open image using Pillow
                src_image_path = os.path.join(src_folder, file_name)
                image = Image.open(src_image_path)

                # Calculate new height while preserving aspect ratio
                width, height = image.size
                aspect_ratio = height / width
                new_height = round(new_pixel_width * aspect_ratio)

                # Resize image using Pillow
                resized_image = image.resize((new_pixel_width, new_height))

                # Save resized image to dst_folder with prefixed filename
                resized_image_path = os.path.join(dst_folder, f"{dst_file_prefix}{file_name}")
                resized_image.save(resized_image_path)
                print(f"src_image_path:{src_image_path} resized_image_path:{resized_image_path}")

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
