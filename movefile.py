import os
import shutil
import time
import random
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:\Users\Dell"
to_dir = "C:\Users\Dell\Downloads"

list_of_files = os.listdir(from_dir)

class FileEventHandler(FileSystemEventHandler):
  def on_created(self,event):
    print(f'hey,{event.src_path} has been created')

  def on_deleted(self,event):
    print(f'hey,{event.src_path} has been deleted')

  def on_modified(self,event):
    print(f'hey,{event.src_path} has been modified')

  def on_moved(self,event):
    print(f'hey,{event.src_path} has been moved')

event_handler = FileMovementHandler()


# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()

#print(list_of_files)
for file_name in list_of_files:

    name, extension = os.path.splitext(file_name)
    #print(name)
    #print(extension)

    if extension == '':
        continue
    if extension in ['.txt', '.docx', '.doc', '.pdf']:

        path1 = from_dir + '/' + file_name                       
        path2 = to_dir + '/' + "Document_files"                          
        path3 = to_dir + '/' + "Document_Files" + '/' + file_name   
        #print("path1 " , path1)
        #print("path3 ", path3)

        
        if os.path.exists(path2):
          print("Moving " + file_name + ".....")

          
          shutil.move(path1, path3)

        else:
          os.makedirs(path2)
          print("Moving " + file_name + ".....")
          shutil.move(path1, path3)
try :
  while True :
    time.sleep(2)
    print("running")

except KeyboardInterrupt:
  observer.stop


