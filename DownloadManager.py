# Programmer: Andrew Speelman
# Description: Script that will sort the specified folder by year and month
#              /2019/12
#
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import json
import time
from datetime import datetime
from time import gmtime, strftime

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        #Sort every file in the directory into 'Direcory/year/month'
        for filename in os.listdir(folder):
            time = datetime.now()
            year = time.strftime("%Y")
            month = time.strftime("%m")
            YEAR_EXISTS = False
            MONTH_EXISTS = False
            folder_name = folder + "\\" + year + "\\" + month

            for year_folder in os.listdir(folder):
                if year_folder == year:
                    YEAR_EXISTS = True
                    folder_name = folder_name + "\\" + year

                    #Folder already exists, check month folder
                    for month_folder in os.listdir(folder_name):
                        if month_folder == month:
                            MONTH_EXISTS = True
                            folder_name = folder_name + "\\" + month
            #If the year or month folder does not exist, create it.
            if not YEAR_EXISTS:
                os.mkdir(folder + "\\" + year)
            if not MONTH_EXISTS:
                os.mkdir(folder + "\\" + year + "\\" + month)


            src = folder + "\\" + filename
            new_destination = folder_name + "\\" + filename
            os.rename(src, new_destination)

folder = "C:\\Users\\Drew\\Desktop\\testFolder1"
folder_destination = "C:\\Users\\Drew\\Desktop\\testFolder2"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder, recursive=True)
observer.start()
try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
