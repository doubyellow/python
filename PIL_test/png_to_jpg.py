# coding=utf-8
import os.path

from PIL import Image

root_file_path = r"C:\Users\ASUS\Pictures\Camera Roll"

for file_name in os.listdir(root_file_path):
    if ".png" in file_name:
        file = os.path.join(root_file_path, file_name)
        new_file = os.path.join(root_file_path, file_name.split(".")[0] + ".jpg")
        im = Image.open(file)
        im = im.convert('RGB')
        im.save(new_file, quality=95)
