import os
import sys
import shutil
import configparser
import customtkinter as ctk
from tkinter import filedialog, messagebox

CONFIG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.ini")
BUTTON_WIDTH = 150

icon_path = os.path.abspath("Ark_INI_Loader_icon.ico")

ini_file_names = []
ini_file_paths = {}

def load_config():
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    return config

def save_config():
    """Save the current paths to config.ini without duplicates."""
    config = configparser.ConfigParser()
    
    config.read(CONFIG_FILE)
    
    if 'Paths' not in config:
        config['Paths'] = {}
    config['Paths']['BaseFile'] = base_file_entry.get()
    
    if 'INI_Files' not in config:
        config['INI_Files'] = {}
    
    for name, path in ini_file_paths.items():
        if name not in config['INI_Files']:
            config['INI_Files'][name] = path
    
    with open(CONFIG_FILE, 'w') as configfile:
        config.write(configfile)

def load_saved_ini_files():
    """Load previously saved INI file paths from the config file without duplicates."""
    config = load_config()
    if 'INI_Files' in config:
        for name, path in config['INI_Files'].items():
            if name not in ini_file_paths:
                ini_file_names.append(name)
                ini_file_paths[name] = path
        update_dropdown_menu()

def replace_ini(base_file, new_file):
    #shutil.copy(base_file, f"{base_file}.backup")
    shutil.copy(new_file, base_file)

def browse_base_file():
    path = filedialog.askopenfilename(title="Select BaseDeviceProfiles.ini", filetypes=[("INI files", "*.ini")])
    if path:
        base_file_entry.delete(0, ctk.END)
        base_file_entry.insert(0, path)
        save_config()

def load_single_ini_file():
    """Load a single INI file and add it to the list."""
    ini_file = filedialog.askopenfilename(title="Select an INI File", filetypes=[("INI files", "*.ini")])
    if ini_file:
        file_name = os.path.basename(ini_file)
        if file_name not in ini_file_names:
            ini_file_names.append(file_name)
            ini_file_paths[file_name] = ini_file
            update_dropdown_menu()
            save_config()

def load_new_ini_files(directory=None):
    """Load all INI files from a selected directory, avoiding duplicates in memory and config."""
    new_files_dir = directory if directory else filedialog.askdirectory(title="Select Folder with New INI Files")
    if new_files_dir:
        for f in os.listdir(new_files_dir):
            if f.endswith('.ini'):
                full_path = os.path.join(new_files_dir, f)
                if f not in ini_file_paths:
                    ini_file_names.append(f)
                    ini_file_paths[f] = full_path
        update_dropdown_menu()
        new_files_dir_label.configure(text=new_files_dir)
        save_config()

def clear_ini_list():
    """Clear the list of loaded INI files and reset the dropdown."""
    global ini_file_names, ini_file_paths
    ini_file_names = []
    ini_file_paths = {}
    new_file_var.set("")
    update_dropdown_menu()
    save_config()

def update_dropdown_menu():
    """Update the dropdown menu with the current list of INI files."""
    new_file_menu.configure(values=ini_file_names) 
    if ini_file_names:
        new_file_var.set(ini_file_names[0])
    else:
        new_file_var.set("")

def preview_ini_file(selected_file_name):
    """Display the content of the selected INI file in the preview box."""
    file_path = ini_file_paths.get(selected_file_name)
    if file_path and os.path.isfile(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            ini_preview_textbox.delete("1.0", ctk.END)
            ini_preview_textbox.insert("1.0", content) 
        except UnicodeDecodeError:
            ini_preview_textbox.delete("1.0", ctk.END)
            ini_preview_textbox.insert("1.0", "Unable to preview file. Unsupported encoding.")

def on_apply_button_click():
    base_file = base_file_entry.get()
    selected_file_name = new_file_var.get()
    new_file = ini_file_paths.get(selected_file_name)
    
    if not base_file:
        messagebox.showwarning("Input Error", "Please select the BaseDeviceProfiles.ini file.")
        return
    
    if not new_file:
        messagebox.showwarning("Input Error", "Please select a new INI file to replace with.")
        return
    
    if not os.path.isfile(base_file):
        messagebox.showerror("File Error", f"The specified base file does not exist: {base_file}")
        return
    
    if not os.path.isfile(new_file):
        messagebox.showerror("File Error", f"The specified new file does not exist: {new_file}")
        return

    try:
        replace_ini(base_file, new_file)
        messagebox.showinfo("Success", f"The BaseDeviceProfiles.ini file has been replaced with {selected_file_name}.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# window theme
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# main window
root = ctk.CTk()
root.title("Ark INI Loader")
try:
    root.iconbitmap(icon_path)
except Exception as e:
    print(f"Failed to set icon: {e}")
root.geometry("1000x750")

# Path Section
path_label = ctk.CTkLabel(root, text="Path to BaseDeviceProfiles.ini")
path_label.pack(padx=20, pady=(20, 5))
path_frame = ctk.CTkFrame(root)
path_frame.pack(fill="x", padx=20, pady=5)

base_file_entry = ctk.CTkEntry(path_frame, width=700)
base_file_entry.grid(row=0, column=0, padx=(0, 10), pady=10)
ctk.CTkButton(path_frame, text="Browse", command=browse_base_file, width=150).grid(row=0, column=1, pady=10)

# INI Selection Section
ini_frame = ctk.CTkFrame(root)
ini_frame.pack(fill="x", padx=20, pady=(10, 10))

# Labels for instructions
ctk.CTkLabel(ini_frame, text="Select INI Files to Import ino the program").grid(row=0, column=0, padx=(0, 10), pady=(10, 5), sticky="w")

# Folder-based loading
ctk.CTkLabel(ini_frame, text="Import INI Files from a Folder:").grid(row=1, column=0, padx=(0, 10), pady=5, sticky="w")
new_files_dir_label = ctk.CTkLabel(ini_frame, text="(No folder selected)", width=500, anchor="w")
new_files_dir_label.grid(row=1, column=1, padx=5, sticky="w")
ctk.CTkButton(ini_frame, text="Import Folder", command=load_new_ini_files, width=150).grid(row=1, column=2, padx=5)

# Single file loading
ctk.CTkLabel(ini_frame, text="Import Single INI File:").grid(row=2, column=0, padx=(0, 10), pady=5, sticky="w")
ctk.CTkButton(ini_frame, text="Import Single File", command=load_single_ini_file, width=150).grid(row=2, column=1, padx=5, sticky="w")

# Dropdown menu 
ctk.CTkLabel(ini_frame, text="Select Imported INI File:").grid(row=3, column=0, padx=(0, 10), pady=5, sticky="w")
new_file_var = ctk.StringVar(root)
new_file_menu = ctk.CTkOptionMenu(ini_frame, variable=new_file_var, values=[], command=preview_ini_file)
new_file_menu.grid(row=3, column=1, padx=5, pady=5, sticky="w")

# Clear INI List
clear_button = ctk.CTkButton(ini_frame, text="Clear INI List", command=clear_ini_list, width=150, fg_color="red")
clear_button.grid(row=3, column=2, pady=(5, 5), sticky="e")

# Preview Box for Selected INI File
preview_label = ctk.CTkLabel(root, text="Preview of Selected INI File:")
preview_label.pack(padx=20, pady=(10, 5))

# Frame for the Preview Box 
preview_frame = ctk.CTkFrame(root, width=850, height=300) 
preview_frame.pack_propagate(False)  
preview_frame.pack(padx=20, pady=(10, 10))

# Textbox for INI file preview
ini_preview_textbox = ctk.CTkTextbox(preview_frame, wrap="word")
ini_preview_textbox.pack(fill="both", expand=True)  

# Apply Button Section
apply_button = ctk.CTkButton(root, text="Load into Ark config files", command=on_apply_button_click, width=150, fg_color="green")
apply_button.pack(pady=(10, 20))

# Load previous settings and saved INI files
config = load_config()
base_file_path = config.get('Paths', 'BaseFile', fallback="")
base_file_entry.insert(0, base_file_path)
load_saved_ini_files()

# Footer label
footer_label = ctk.CTkLabel(root, text="Made by GoofyAhhDev", anchor="e")
footer_label.pack(side="bottom", anchor="se", padx=10, pady=5)

root.mainloop()
