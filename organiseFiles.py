import os
from pathlib import Path  #pip install pathlib

folder_dict = {
	"Images": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
			".heif", ".psd"],
	"Videos": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
			".qt", ".mpg", ".mpeg", ".3gp",".mkv"],
	"Documents": [".doc", ".pptx", ".pdf", ".docx", ".doc", ".xla",],
	"Audio": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
			".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
	"Text": [".txt", ".in", ".out"],
	"PDF": [".pdf"],
	"Python": [".py"],
	"XML": [".xml"],
	"EXE": [".exe"]

}

FILE_FORMATS = {file_format: directory
				for directory, file_formats in folder_dict.items()
				for file_format in file_formats}

def organize():
	for entry in os.scandir():
		if entry.is_dir():
			continue
		file_path = Path(entry)
		file_format = file_path.suffix.lower()
		if file_format in FILE_FORMATS:
			directory_path = Path(FILE_FORMATS[file_format])
			directory_path.mkdir(exist_ok=True)
			file_path.rename(directory_path.joinpath(file_path))

		for dir in os.scandir():
			try:
				os.rmdir(dir)
			except:
				pass

organize()
