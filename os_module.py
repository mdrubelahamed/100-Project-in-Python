import os

# Define the path to the parent folder
parent_folder = os.getcwd()

# Loop through the folders and rename them
for day_number in range(1, 22):
    old_folder_name = os.path.join(parent_folder, f'day {day_number}')
    new_folder_name = os.path.join(parent_folder, f'project {day_number}')
    
    # Use os.rename to rename the folder
    os.rename(old_folder_name, new_folder_name)

print("Folders renamed successfully.")
