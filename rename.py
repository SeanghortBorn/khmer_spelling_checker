import os
# for i in range(1, 16):
    # participant = f"p{i}"
participant = "p16"
folder_path = "keystrokes/"+participant

if not os.path.exists(folder_path):
    print(f"Folder '{folder_path}' not found.")
    exit()
files = os.listdir(folder_path)
for index, filename in enumerate(files):
    old_path = os.path.join(folder_path, filename)
    if os.path.isdir(old_path):
        continue
    new_filename = f"{participant}art{index+1}{os.path.splitext(filename)[1]}"
    new_path = os.path.join(folder_path, new_filename)
    os.rename(old_path, new_path)
    print(f"Renamed: {filename} -> {new_filename}")