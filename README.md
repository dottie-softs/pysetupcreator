# Python setup compiler

### 1. Install _PyInstaller_

You can install this module via *pip*:

```

pip install pyinstaller

```

### 2. Features

* File Collection: Gather files that will be packaged in the installer.
* Registry & Shortcuts: Optionally add registry keys, shortcuts, or other configurations.
* Installer Configuration: Provide options for customizing the installation process (e.g., choosing install paths, adding prerequisites).
* Executable Creation: Finally, create an installer executable.

### 3. Creating Setup

If you want to compile setup with python you need do first use pyinstaller:

```

pyinstaller --onefile [appname].py


```

This will create a single .exe file in the dist folder.

You need to get Inno Setup Compiler from [official website](https://jrsoftware.org/isdl.php)

Next step is creating empty .iss file.

Follow this content:

```

[Setup]
AppName=MyApp
AppVersion=1.0
DefaultDirName={pf}\MyApp
DefaultGroupName=MyApp
OutputDir=.\output
OutputBaseFilename=MyAppInstaller
Compression=lzma
SolidCompression=yes

[Files]
Source: "dist\app.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{startmenu}\MyApp"; Filename: "{app}\app.exe"

```

This will make a config for our compiler.

*Info*

Explanation of the Script:
Setup: Contains metadata about your application, such as name, version, and default installation path.
Files: Defines which files to include in the installer. Here, we specify the app.exe file created by PyInstaller.
Icons: Creates a shortcut in the Start Menu.

# How This Script Works:
* create_executable: Uses PyInstaller to create the .exe file.
* create_inno_script: Generates an Inno Setup script dynamically.
* compile_inno_script: Uses Inno Setup's compiler (iscc) to generate the installer.
* create_installer: Automates the entire process.

# Run the Python Setup Creator
### Run the Python script by executing it in the terminal. This will automatically:
### Create the executable using PyInstaller.
### Generate the Inno Setup script.
### Compile the installer using Inno Setup.