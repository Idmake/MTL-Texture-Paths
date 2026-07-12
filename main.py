import tkinter.filedialog

open_types = (["MTL File", "*.mtl"], ["All Files", "*.*"])
mtl_file_path = tkinter.filedialog.askopenfilename(filetypes=open_types)

save_types = [("MTL File", "*.mtl"), ("Any File", "*.*")]
new_file_path = tkinter.filedialog.asksaveasfilename(filetypes=save_types, defaultextension=save_types)

if mtl_file_path == "" or new_file_path == "":
    quit()

old_lines = []
new_lines = []

with open(file=mtl_file_path, mode="r") as mtl_file:
    old_lines = mtl_file.read().splitlines()

# Lets get rid of the file path before the file name

for line in old_lines:
    if line.find("map_Kd") != -1 or line.find("map_d") != -1:

        # don't get the full path, only the file name
        path_parts = line.split(sep="/")
        filename_part = path_parts[len(path_parts) - 1]


        # get map_Kd or map_d
        map_part = line.split()[0]
        new_lines.append(map_part + " " + filename_part + "\n")
    else:
        new_lines.append(line + "\n")

print("End reading")


with open(new_file_path, "w") as new_file:
    for line in new_lines:
        new_file.write(line)

print("End saving")
