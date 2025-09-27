# 🌌 Ark INI Loader

Ark INI Loader is a Windows application designed to quickly load and replace your **INI** files for the game **ARK: Survival Evolved**.  
This tool allows you to easily **import, preview, and apply custom INI configurations** to streamline your gameplay settings.

---

## ✨ Features

- **Load Base Config File**  
  Select the primary `BaseDeviceProfiles.ini` (formerly known as ConsoleVariables) configuration file.

- **Import INI Files**  
  Import individual INI files or batch-load multiple INI files from a selected folder.

- **Preview and Apply**  
  Preview the contents of each imported INI file and apply it to the base config with a single click.

- **Backup Creation**  
  Creates a backup of your base file before any changes are applied.

- **Custom INI List Management**  
  Easily clear the INI list or select specific configurations.

---

## 📥 Installation

1. Download the latest release from the [Releases](../../releases) page.  
2. Extract the `.zip` file contents to a directory of your choice.  
3. Run **`Ark INI Loader.exe`** to start the application.  

> 🔹 Note: This application is built with **Python + PyInstaller**, so **no Python installation is required** to run the executable.

---

## 🚀 Usage

1. **Set Base File Path**  
   Click **Browse** to select the `BaseDeviceProfiles.ini` file you wish to modify.  

2. **Import INI Files**  
   - *Load Folder:* Import all `.ini` files from a selected folder.  
   - *Load Single File:* Import a single `.ini` file from anywhere on your system.  

3. **Select and Preview**  
   Choose an imported INI file from the dropdown to preview its contents.  

4. **Apply Configuration**  
   Click **Apply** to replace the base file with the selected INI file.  

5. **Clear INI List**  
   Remove all loaded INI files from the dropdown with the **Clear INI List** button.  

---

## 🖥️ Requirements

- Windows OS  

---

## 🛠️ Troubleshooting

⚠️ **Windows Defender False Positive**  
This executable may be flagged by **Windows Defender** as a Trojan (false positive) due to the PyInstaller bundling process.  

👉 To fix this:  
- Add an **exception in Windows Defender**.  

> ✅ No issues have been reported with Avira Prime, Bitdefender Total Security, or Bitdefender GravityZone.

---

## 🤝 Contributing

Contributions are welcome! 🎉  
If you'd like to contribute to the Ark INI Loader project:  
- Submit a pull request  
- Or open an issue on GitHub  

Contributions for new features, bug fixes, and documentation improvements are encouraged.  

---

## 📜 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.  

---

## 👤 Author

**Discord @bandzz4life**  
Made with ❤️ (and a little frustration) to streamline ARK INI management.
