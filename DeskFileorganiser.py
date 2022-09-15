import shutil
import os

Username = os.getenv("USERNAME")
os.chdir('C:/Users/' + Username + '/OneDrive/Desktop')

try:
    os.mkdir('Photos')
except Exception as e:
    pass
try:
    os.mkdir('Videos')
except Exception as e:
    pass
try:
    os.mkdir('Audio')
except Exception as e:
    pass
try:
    os.mkdir('Documents')
except Exception as e:
    pass
try:
    os.mkdir('EXE')
except Exception as e:
    pass
try:
    os.mkdir('Zips')
except Exception as e:
    pass
try:
    os.mkdir('PDF')
except Exception as e:
    pass
try:
    os.mkdir('etc')
except Exception as e:
    pass
try:
    os.mkdir('python')
except Exception as e:
    pass
try:
    os.mkdir('Folders')
except Exception as e:
    pass
try:
    os.mkdir('Html project')
except Exception as e:
    pass

Folders = ["Folders", "Html project" "python", "etc", "PDF", "Zips", "EXE",
           "Documents", "Audio", "Videos", "Photos"]

image_format = ['jpg', 'png', 'gif', 'jpeg', 'tiff', 'webp', 'jfif']
video_format = ['mp4', 'mkv', 'avi', 'webm']
audio_format = ['mp3', 'wav']
doc_format = ['txt', 'htm', 'html', 'log', 'ahk']
exe_format = ['exe', 'msi', 'jar']
zip_format = ['zip', 'rar', 'gz']
pdf_format = ['pdf', 'pptx']
py_format = ['py', 'pyw']


files = os.listdir('./')
print(files)

for file in files:
    if os.path.isdir(file):
        if file in Folders:
            continue
        else:
            shutil.move(file, 'Folders/' + file)
    if os.path.isfile(file):
        ext = (file.split('.')[-1]).lower()

        if ext in image_format:
            shutil.move(file, 'Photos/' + file)
        elif ext in video_format:
            shutil.move(file, 'Videos/' + file)
        elif ext in audio_format:
            shutil.move(file, 'Audio/' + file)
        elif ext in doc_format:
            shutil.move(file, 'Documents/' + file)
        elif ext in exe_format:
            shutil.move(file, 'EXE/' + file)
        elif ext in py_format:
            shutil.move(file, 'python/' + file)
        elif ext in zip_format:
            shutil.move(file, 'Zips/' + file)
        elif ext in pdf_format:
            shutil.move(file, 'PDF/' + file)
        else:
            shutil.move(file, 'etc/' + file)
