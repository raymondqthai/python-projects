# install module below in terminal
# pip install schedule


# load module
import os
import shutil
import datetime
import schedule
import time


# setup directories
source_dir = "/Users/'insert_username'/Photos"
destination_dir = "/Users/'insert_username'/Automated_File_Backup"


# create function
def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    # create a [today's date] folder inside [destination_dir] folder
    dest_dir = os.path.join(dest, str(today)) 
    
    try:
        # copy [source_dir] to [destination_dir]
        shutil.copytree(source, dest_dir)
        print(f"Folder copied to: {dest_dir}")
    except FileExistsError:
        print(f"Folder already exists in {dest}")


# run function to test that it works
#copy_folder_to_directory(source_dir, destination_dir)


# "lambda:" works similar to "def Lambda()" below
"""
def Lambda():
    copy_folder_to_directory(source_dir, destination_dir)
"""


# schedule task to backup daily at [set time]
schedule.every().day.at("08:00").do(lambda: copy_folder_to_directory(source_dir, destination_dir))


# create an infinite loop to run schedule check for task every 60 seconds
while True:
    schedule.run_pending()
    time.sleep(60)
