# jpgtopngconverter
import sys
import os
from PIL import Image

img_folder = sys.argv[1]
output_folder = sys.argv[2]

print(img_folder, output_folder)

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(img_folder):
    img = Image.open(f"{img_folder}{filename}")
    # this will return a tuple with the name at 0 idx and extension at 1idx
    clean_name = os.path.splitext(filename)[0]
    img.save(f"{output_folder}{clean_name}.png", "png")
    print("all done")
