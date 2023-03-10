from PIL import Image
import os
import shutil

directory = "train_data/FUNSD/training_data/images" # Replace with the directory where your images are stored
same_dim_folder = "train_data/FUNSD/training_data/same" # Replace with the directory where you want to store images with same dimensions
diff_dim_folder = "train_data/FUNSD/training_data/diff" # Replace with the directory where you want to store images with different dimensions

for filename in os.listdir(directory):
    if filename.endswith(".jpg") or filename.endswith(".png"): # Add any other image formats you want to check for
        filepath = os.path.join(directory, filename)
        with Image.open(filepath) as im:
            width, height = im.size
            if width == height:
                shutil.move(filepath, same_dim_folder)
            else:
                shutil.move(filepath, diff_dim_folder)
    
print("Done!")
