#!/usr/bin/env python3
#  Use PIL to Iterate through each file in the folder and  for each file
#        Rotate the image 90° anti-clockwise
#        Resize the image from 192x192 to 128x128
#        Save the image to a new folder in .jpeg format
#  Converted file name is free but updated images should be placed in /opt/icons/
from glob import glob
from pathlib import Path
from PIL import Image

counter = 0
# files in source have no extension, we must selected them all
source = Path("images").glob("*")
destination = Path("/opt/icons/")

def process_image(infile, outfile):
  """
  Expects a TIFF image without extension as input
  Returns a jpeg image that has rotate 90° anti-clockwise and resized to 128x128 in the /opt/icons directory as output
  """
  with Image.open(infile) as img:
    try:
      print(img.filename, f"{img.format}")
      if img.mode != "RGB":
        print("Image mode:", f"{img.mode}")
        img = img.convert("RGB")
      print(f"{outfile}")
      img.rotate(-90).resize((128,128)).save(destination.joinpath(outfile), "JPEG", quality=100)
    except Exception as e:
      print("Exception:", e)


# Removes .DS_Store file in source directory, if present
if source('.DS_Store').exists():
  source(".DS_Store").unlink()
# Iterate over pictures for processing
for path in source:
  process_image(path, path.stem + ".jpeg")
  counter +=1
print(f"{counter} images processed")
