import os, shutil


desktop = ["[Desktop Entry]", "Name=Youtube Video Downloader", "Terminal=false", "Type=Application"]
directory1 = os.getcwd()
name = ".Youtube_downloader"

os.chdir("..")
directory2 = os.getcwd() + "/" + ".Youtube_downloader"
os.mkdir(name)
shutil.copy2(directory1 + "/main.py", name); shutil.copy2(directory1 + "/ui.py", name); shutil.copy2(directory1 + "/icon.jpg", name)
desktop.append("Exec=python3 " + directory2 + "/main.py")
desktop.append("Icon=" + directory2 + "/icon.jpg")

try:
    os.chdir("Работчий стол")
except:
    try:
        os.chdir("Рабочий стол")
    except:
        os.chdir("Desktop")

with open("Youtube_downloader.desktop", "w") as file:
    for i in desktop:
        file.write(i + "\n")
