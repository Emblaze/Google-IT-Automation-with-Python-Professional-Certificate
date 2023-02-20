#!/usr/bin/env python3
from multiprocessing import Pool
import subprocess
from os import path
from os import walk

# source path
src = "data/prod/"
# destination path
dest = "data/prod_backup/"
# list of file names to be stored
files = []
for (dir_path, dir_names, file_names) in walk(src, topdown=True):
  for f in file_names:
    files.append(path.join(dir_path, f))
# Checking length of list, for debugging purposes
# print(len(files))

def backup(files):
  print("Backuping {}".format(files))
  subprocess.call(["rsync", "-arq", src, dest])

if __name__ == "__main__":
  # Create a pool of specific number of CPUs
  p = Pool(len(files))
  # Start each task within the pool
  p.map(backup, files)