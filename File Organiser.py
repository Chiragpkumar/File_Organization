import os
import shutil
import tkinter as tk
from tkinter import filedialog

# Function to organize files in a directory
def organize_files(directory):
    # Dictionary mapping file extensions to folder names
    extensions = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Documents": [".txt", ".pdf", ".doc", ".docx", ".ppt", ".pptx", ".xls", ".xlsx"],
        "Videos": [".mp4", ".avi", ".mkv", ".mov"],
        "Music": [".mp3", ".wav", ".flac"]
    }

    # Create folders if they don't exist already
    for folder in extensions.keys():
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Organize files based on their extensions
    for file in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file)):
            file_extension = os.path.splitext(file)[1].lower()
            moved = False

            for folder, extensions_list in extensions.items():
                if file_extension in extensions_list:
                    src_path = os.path.join(directory, file)
                    dest_path = os.path.join(directory, folder, file)
                    
                    if not os.path.exists(dest_path):
                        shutil.move(src_path, dest_path)
                        moved = True
                        break

            if not moved:
                # Handle files with unknown extensions or do something else
                print(f"File {file} could not be categorized.")

    print("File organization complete.")

# Example usage with tkinter GUI
def main():
    # GUI setup
    root = tk.Tk()
    root.title("File Organizer")

    def select_directory():
        directory = filedialog.askdirectory()
        if directory:
            organize_files(directory)
            tk.messagebox.showinfo("Organize Files", "File organization complete.")

    select_button = tk.Button(root, text="Select Directory", command=select_directory)
    select_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
