#!/usr/bin/env python3

#  Use PIL to Iterate through each file in the folder and  for each file
#        Rotate the image 90° clockwise
#        Resize the image from 192x192 to 128x128
#        Save the image to a new folder in .jpeg format
#  Converted file name is free but updated images should be placed in /opt/icons/

from glob import glob
import os
from PIL import Image

counter = 0
source_directory = "images_2/"
destination_directory = "icons"

def process_image(source_directory, destination_directory):
  with Image.open(source_directory) as img:
    try:
      print(img.filename, f"{img.format} {img.size} {img.mode}")
    #  img.rotate(-90).resize((128,128)).save(os.path.join(destination_directory, "JPEG", quality=100)
    except Exception as e:
      print("Exception:", e)

# create list of pictures for processing
pics2process = glob(os.path.join(source_directory, "*"))
for pic in pics2process:
    process_image(pic, pic + ".jpeg")
    counter +=1
print(f"{counter} images processed")