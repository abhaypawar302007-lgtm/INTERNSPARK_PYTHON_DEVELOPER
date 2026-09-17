import os
import shutil
import logging

logging.basicConfig(
    filename="file_operations.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


folder = input("Enter folder path: ")
operation = input("Choose operation (rename/sort/clean): ").lower()

def rename_files(folder):
    try:
        for i, filename in enumerate(os.listdir(folder)):
            old_path = os.path.join(folder, filename)
            if os.path.isfile(old_path):
                new_name = f"file_{i}{os.path.splitext(filename)[1]}"
                new_path = os.path.join(folder, new_name)
                os.rename(old_path, new_path)
                logging.info(f"Renamed {filename} -> {new_name}")
    except Exception as e:
        logging.error(f"Error renaming files: {e}")

def sort_files(folder):
    try:
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            if os.path.isfile(file_path):
                ext = filename.split('.')[-1]
                ext_folder = os.path.join(folder, ext)
                os.makedirs(ext_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(ext_folder, filename))
                logging.info(f"Moved {filename} -> {ext}/")
    except Exception as e:
        logging.error(f"Error sorting files: {e}")

def clean_files(folder):
    try:
        for filename in os.listdir(folder):
            if filename.endswith(('.tmp', '.log', '.bak')):
                file_path = os.path.join(folder, filename)
                os.remove(file_path)
                logging.info(f"Deleted {filename}")
    except Exception as e:
        logging.error(f"Error cleaning files: {e}")

if operation == "rename":
    rename_files(folder)
elif operation == "sort":
    sort_files(folder)
elif operation == "clean":
    clean_files(folder)
else:
    print("Invalid operation selected.")
