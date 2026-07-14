import tkinter.filedialog

open_types = (["MTL File", "*.mtl"], ["All Files", "*.*"])
open_title = "Select a .mtl File"
mtl_file_path = tkinter.filedialog.askopenfilename(filetypes=open_types, title=open_title)

save_types = [("MTL File", "*.mtl"), ("Any File", "*.*")]
save_title = "Save as a new .mtl file"
new_file_path = tkinter.filedialog.asksaveasfilename(filetypes=save_types, defaultextension=save_types, title=save_title)

if mtl_file_path == "" or new_file_path == "":
    quit()

old_lines = []
new_lines = []

with open(file=mtl_file_path, mode="r") as mtl_file:
    old_lines = mtl_file.read().splitlines()

# Lets get rid of the file path before the file name

for line in old_lines:
    if line.find("map_Kd") != -1 or line.find("map_d") != -1:

        # don't get the full path, get the last path
        path_parts = line.split(sep=" ")
        filename_part = path_parts[len(path_parts) - 1]

        # don't get any folder behind that
        path_parts = filename_part.split(sep="/")
        filename_part = path_parts[len(path_parts) - 1]

        print("filename: " + filename_part)

        # get map_Kd or map_d
        map_part = line.split(sep=" ")[0]
        new_lines.append(map_part + " " + filename_part + "\n")

        print("map part: " + map_part)

    else:
        new_lines.append(line + "\n")

print("End reading")


with open(new_file_path, "w") as new_file:
    for line in new_lines:
        new_file.write(line)

print("End saving")
