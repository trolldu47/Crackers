import wget, os, shutil
from zipfile import ZipFile 

os.system('taskkill /IM Crackers.exe')

path = "."
disable = 0

for f in os.listdir(path):
    if f == ".git":
        disable = 1
    
    elif f == ".gitignore":
        disable = 1
    
    elif f == "updater.exe":
        disable = 1
    
    elif f == "updater.py":
        disable = 1
        
    if disable == 0:
        try:    
            os.remove(f)
        
        except WindowsError:
            shutil.rmtree(f)    
    
    else:
        disable = 0
        
url = 'https://github.com/trolldu47/Crackers/releases/download/Python/Crackers_file.zip'
filename = wget.download(url)

with ZipFile(filename, 'r') as zip:
    zip.extractall()
    
os.system('start Crackers.exe')