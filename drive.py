from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
import constants as C
def uploadCache_to_drive_CSV():
	gauth = GoogleAuth()
	gauth.LocalWebserverAuth() 
	drive = GoogleDrive(gauth)
	file1 = drive.CreateFile({'title': C.cache_tag})
	file1.SetContentFile(C.cachepath_tag)
	file1.Upload()
	file_id = open(C.path_file_drive_cache_id, 'r').read()
	priv_trashCache_CSV_from_drive(file_id)
	file_id = open(C.path_file_drive_cache_id, 'w').write(file1['id'])
	
def downloadCache_CSV_from_drive():
	gauth = GoogleAuth()
	gauth.LocalWebserverAuth() 
	drive = GoogleDrive(gauth)
	file_id = open(C.path_file_drive_cache_id, 'r').read()
	file2 = drive.CreateFile({'id': file_id})
	os.remove(C.cachepath_tag)
	file2.GetContentFile(C.cachepath_tag)

def priv_trashCache_CSV_from_drive(file_id):
	gauth = GoogleAuth()
	gauth.LocalWebserverAuth() 
	drive = GoogleDrive(gauth)
	file_trash = drive.CreateFile({'id': file_id})
	file_trash.Trash()


