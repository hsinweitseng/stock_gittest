import xlrd
import MySQLdb
import time
import os
import glob

import ftplib
import time
import sys

def main():
	sys.path.append(os.path.dirname(os.path.abspath(__file__)))
	os.chdir(os.path.dirname(os.path.abspath(__file__)))

	Current_Directory = os.getcwd()		
	print(Current_Directory)
	All_File_List = glob.glob("*")
	
	print('All files')
	for FileName in All_File_List:
		print(FileName)
		
	print('Python program module finished')
	
	#	Python_SMS to cell phone-----------------
	import Python_sms
	#Python_sms.Send_SMS('Testing all python execute batch')

	#--------------------------------------------------------
	#Testing between syncying two computers.

	print('Back up everying to 99 Automation backup folder')
	time.sleep(1)

	import HT_ftpUploadEverything_python_coding_backup
	#HT_ftpUploadEverything_python_coding_backup.UploadEverything()
	#print('finished upload')

	#--------------------------------------
	print('import HT_download everything.py')
	time.sleep(1)
	import HT_download_everything

	#import python27_upload_excel_mysql
	#python27_upload_excel_mysql.Upload_Excel_MySQL()

if __name__ == '__main__':
    main()
