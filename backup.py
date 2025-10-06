import os
import shutil
from datetime import datetime

# Source folder to backup
source_folder = "C:/Users/Dell/Desktop/Devops/Python"

# Backup destination folder
backup_folder = "C:/Users/Dell/Desktop/Devops/Python/backups"

# Create folders if they don't exist
if not os.path.exists(source_folder):
    os.makedirs(source_folder)
    print(f"Source folder '{source_folder}' was missing. Created an empty folder.")

if not os.path.exists(backup_folder):
    os.makedirs(backup_folder)

# Timestamp for unique backup
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
backup_name = "logs_backup_" + timestamp
backup_path = os.path.join(backup_folder, backup_name)

# Inform the user that backup is starting
print(f"\nStarting backup of '{source_folder}'...")
print(f"Backup will be saved as: {backup_path}.zip")

# Perform the backup
shutil.make_archive(backup_path, 'zip', source_folder)

# Inform the user that backup is completed
print(f"Backup completed successfully! File created at:\n{backup_path}.zip")
