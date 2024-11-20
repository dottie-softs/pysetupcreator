import os
import subprocess
import shutil

# idk why but it is there
def create_executable(py_script):
    print(f"Creating executable from {py_script}...")
    result = subprocess.run(["pyinstaller", "--onefile", py_script], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    if result.returncode != 0:
        print(f"Error creating executable: {result.stderr.decode()}")
        return False
    
    print(f"Executable created at {os.path.join('dist', py_script.replace('.py', '.exe'))}")
    return True

# As you can see you have the template usage
def create_inno_script(app_name, app_version, exe_path):
    script_content = f"""
[Setup]
AppName={app_name}
AppVersion={app_version}
DefaultDirName={{pf}}\\{app_name}
DefaultGroupName={app_name}
OutputDir=./output
OutputBaseFilename={app_name}Installer
Compression=lzma
SolidCompression=yes

[Files]
Source: "{exe_path}"; DestDir: "{{app}}"; Flags: ignoreversion

[Icons]
Name: "{{startmenu}}\\{app_name}"; Filename: "{{app}}\\{app_name}.exe"
"""
    script_file = "installer.iss"
    with open(script_file, "w") as f:
        f.write(script_content)
    
    print(f"Inno Setup script created: {script_file}")
    return script_file

def compile_inno_script(script_file):
    print(f"Compiling {script_file} with Inno Setup...")
    result = subprocess.run(["iscc", script_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    if result.returncode != 0:
        print(f"Error compiling Inno Setup script: {result.stderr.decode()}")
        return False
    
    print("Installer created successfully.")
    return True

# For more advanced brains - this is the main code for creating setup lmao
def create_installer(py_script, app_name, app_version):
    if not create_executable(py_script):
        return
    
    exe_path = os.path.join("dist", py_script.replace(".py", ".exe"))
    
    script_file = create_inno_script(app_name, app_version, exe_path)
    
    compile_inno_script(script_file)
    
    if os.path.exists("installer.iss"):
        os.remove("installer.iss")
    if os.path.exists("dist"):
        shutil.rmtree("dist")

# Example of creating installer:
create_installer("app.py", "MyApp", "1.0")
