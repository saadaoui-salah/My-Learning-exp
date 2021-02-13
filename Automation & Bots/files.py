import os
import shutil

current_dir = os.path.dirname(__file__)

for filename in os.listdir(current_dir):
    
    if filename.endswith((".png",".jpg")):
        os.mkdir("images")
        shutil.copy(filename,"images")
        os.remove(filename)
        print("image was saved")