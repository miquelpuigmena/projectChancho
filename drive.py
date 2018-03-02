from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
import constants as C
def upload_file_to_drive(title, path):
	gauth = GoogleAuth()
	gauth.LocalWebserverAuth() 
	drive = GoogleDrive(gauth)
	priv_trash_file_from_drive(title)
	file1 = drive.CreateFile({'title': title})
	file1.SetContentFile(path)
	file1.Upload()
	
def download_file_from_drive(title, path):
	file_down = priv_get_file_from_drive(title)
	if file_down != 0:
		gauth = GoogleAuth()
		gauth.LocalWebserverAuth() 
		drive = GoogleDrive(gauth)
		file2 = drive.CreateFile({'id': file_down['id']})
		os.remove(path)
		file2.GetContentFile(path)

def priv_trash_file_from_drive(title):
	file_to_trash = priv_get_file_from_drive(title)
	if file_to_trash != 0:
		gauth = GoogleAuth()
		gauth.LocalWebserverAuth() 
		drive = GoogleDrive(gauth)
		file_trash = drive.CreateFile({'id': file_to_trash['id']})
		file_trash.Trash()

def priv_get_file_from_drive(title):
	gauth = GoogleAuth()
	gauth.LocalWebserverAuth() 
	drive = GoogleDrive(gauth)
	file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
	for files in file_list:
		if files['title']==title:
			return files
	return 0

