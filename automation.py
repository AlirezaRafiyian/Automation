import os 
import shutil


files = os.listdir()

# Create directories if they dont exist
DIRS = ['Audio', 'Video', 'Images', 'Documents', 'Folders', 'Other']
if not os.path.isdir('./Audio'):
    for d in DIRS:
        os.mkdir('./{}'.format(d))

EXT_AUDIO = ['.wav', '.mp3', '.raw', '.wma']
EXT_VIDEO = ['.mp4', '.m4a', '.m4v', '.f4v', '.f4a', '.m4b', '.m4r', '.f4b', '.mov', '.avi', '.wmv', '.flv']
EXT_IMAGE = ['.jpg', '.jpeg', '.png', '.svg', '.gif', '.bmp']
EXT_DOUCMENT = ['.txt', '.pdf', '.doc', 'docx', '.odt', '.html']


# Run main script
for f in files:
    name, extension = os.path.splitext(f)

    if extension in EXT_IMAGE:
        shutil.move(f, './Images/{}'.format(f))
    elif extension in EXT_AUDIO:
        shutil.move(f, './Audio/{}'.format(f))
    elif extension in EXT_VIDEO:
        shutil.move(f, './Video/{}'.format(f))
    elif extension in EXT_DOUCMENT:
        shutil.move(f, './Documents/{}'.format(f))
    else:
        if os.path.isdir(name):
            if name not in DIRS:
                shutil.move(f, './Folders/{}'.format(f))
        else: 
            if f != 'automation.py':
                shutil.move(f, './Other/{}'.format(f))