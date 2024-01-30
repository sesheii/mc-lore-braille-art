# import nbtlib
# import tkinter
# import customtkinter


# customtkinter.set_appearance_mode("System")
# customtkinter.set_default_color_theme("blue")

# app = customtkinter.CTk()
# app.geometry('720x1200')
# app.title('MC braille to nbt')
# app.mainloop()

# def open_file_selection():
#     filename = fd.askopenfilename()
#     return filename


# nbt_file_path = 'D:\\Minecraft\\game\\hotbar.nbt' # path to hotbar.nbt in minecraft directory
# nbt_file = nbtlib.load(nbt_file_path)

# row_num = 4 # row number in "Saved Toolbars" tab, starts with 0
# col_num = 7 # column number in "Saved Toolbars" tab, starts with 0

# image_path = open_file_selection().replace('/', '\\')
# subprocess.call(f'ascii-image-converter.exe {image_path} -H 20 -b --dither --save-txt .\\txt-images')   

# filename, extension = os.path.splitext(os.path.basename(image_path))
# image_file_name = f'.\\txt-images\\{filename}-ascii-art.txt'

# my_compound = []
# with open(image_file_name, 'r') as f:
#     for row in f:
#         my_compound.append(String('§l§7' + row.strip()))

# lore_list_tag = nbtlib.List(my_compound)
# nbt_file[Path(f'{row_num}[{col_num}].tag.display.Lore')] = lore_list_tag
# nbt_file.save(nbt_file_path)


import nbtlib
import subprocess
from tkinter import filedialog as fd
from nbtlib import String, Path
import os


def open_file_selection():
    filename = fd.askopenfilename()
    return filename


nbt_file_path = 'D:\\Minecraft\\game\\hotbar.nbt' # path to hotbar.nbt in minecraft directory
nbt_file = nbtlib.load(nbt_file_path)

row_num = 7 # row number in "Saved Toolbars" tab, starts with 0
col_num = 5 # column number in "Saved Toolbars" tab, starts with 0

# image_path = open_file_selection().replace('/', '\\')
image_path = 'D:\\Downloads\\IMG1207.jpg'
print(image_path)

# uncomment one of these to change what the result looks like

# subprocess.call(f'ascii-image-converter.exe {image_path} -H 30 -b --threshold 140 --save-txt .\\txt-images')
# subprocess.call(f'ascii-image-converter.exe {image_path} -H 30 -b --dither --save-txt .\\txt-images')
# subprocess.call(f'ascii-image-converter.exe {image_path} -H 20 -b --threshold 210 --save-txt .\\txt-images')
subprocess.call(f'ascii-image-converter.exe {image_path} -H 20 -b --dither --save-txt .\\txt-images')   

filename, extension = os.path.splitext(os.path.basename(image_path))
image_file_name = f'.\\txt-images\\{filename}-ascii-art.txt'

my_compound = []
with open(image_file_name, 'r') as f:
    for row in f:
        my_compound.append(String('§l§7' + row.strip()))

lore_list_tag = nbtlib.List(my_compound)
print(nbt_file[Path(f'{row_num}[{col_num}].tag.display.Lore')])
nbt_file[Path(f'{row_num}[{col_num}].tag.display.Lore')] = lore_list_tag
nbt_file.save(nbt_file_path)