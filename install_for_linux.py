import os, shutil, subprocess


g = 0
desktop = ["[Desktop Entry]", "Name=Youtube Video Downloader", "Terminal=false", "Type=Application"]
directory1 = os.getcwd()
name = ".Youtube_downloader"

os.chdir("..")
for i in os.getcwd():
    if i == "/":
        g += 1

while g > 2:
    os.chdir("..")
    g -= 1

directory2 = os.getcwd() + "/" + ".Youtube_downloader"
print (os.getcwd())
os.mkdir(name)
shutil.copy2(directory1 + "/main.py", name); shutil.copy2(directory1 + "/ui.py", name); shutil.copy2(directory1 + "/icon.jpg", name)
desktop.append("Exec=python3 " + directory2 + "/main.py")
desktop.append("Icon=" + directory2 + "/icon.jpg")

q = subprocess.check_output(["xdg-user-dir", "DESKTOP"]).decode("UTF-8")
os.chdir(q[:len(q)-1])

with open("Youtube_downloader.desktop", "w") as file:
    for i in desktop:
        file.write(i + "\n")
