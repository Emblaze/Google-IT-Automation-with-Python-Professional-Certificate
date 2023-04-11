#!/usr/bin/env python3

# using the PIL library to update all images within ~/supplier-data/images directory to the following specifications:
# Size: Change image resolution from 3000x2000 to 600x400 pixel
# Format: Change image format from .TIFF to .JPEG
# After processing the images, save them in the same path ~/supplier-data/images, with a JPEG extension.

from glob import glob
from pathlib import Path
from PIL import Image

counter = 0
# files in source have no extension, we must selected them all
source = Path("supplier-data/images").glob("*.tiff")
destination = Path("supplier-data/images")

def process_image(infile, outfile):
  """
  Expects a RGBA 3000x2000 TIFF image with extension as input
  Returns a RGB 600x400 jpeg image in the origin directory as output
  """
  with Image.open(infile) as img:
    try:
      print(img.filename, f"{img.format}")
      if img.mode != "RGB":
        print("Image mode:", f"{img.mode}")
        img = img.convert("RGB")
      print(f"{outfile}")
      img.resize((600,400)).save(destination.joinpath(outfile), "JPEG", quality=100)
    except Exception as e:
      print("Exception:", e)

# Iterate over pictures for processing
for path in source:
  process_image(path, path.stem + ".jpeg")
  counter +=1
print(f"{counter} images processed")