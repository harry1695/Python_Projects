# when last image is uploaded we get an error so the uploaded image is not deleted.
import threading, time
from instabot import Bot
import os, glob
from datetime import datetime


def job():
    bot = Bot()
    bot.login(username="Your_Username",
              password="Your_Password")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    # check if the folder is empty or not
    path = "Path of the image folder"
    directory = os.listdir(path)

    if len(directory) == 0:
        print("Empty directory")
        print(current_time)
        return
    else:
        print("Not empty directory")
        parent_dir = path
        extensions = ['*.jpg', '*.REMOVE_ME']

        for pdf_file in glob.glob(os.path.join(parent_dir, '*.jpg')):
            file_name = os.path.basename(pdf_file)
            print(pdf_file)
            print(file_name)
            for dfile in glob.glob(os.path.join(parent_dir, '*.REMOVE_ME')):
                dfile_name = os.path.basename(dfile)
                print(dfile)
                print(dfile_name)
                os.remove(dfile)
                print(dfile)
                print(dfile_name)

        bot.upload_photo(pdf_file)
        print("An Image named", file_name, " Was Uploaded at", current_time)


# the code for scheduling the action
WAIT_TIME_SECONDS = 3
ticker = threading.Event()
while not ticker.wait(WAIT_TIME_SECONDS):
    job()



