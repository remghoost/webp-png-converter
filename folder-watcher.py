import os
import subprocess
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileConversionHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return

        file_path = event.src_path
        if file_path.endswith('.webp'):
            self.convert_file(file_path)

    def convert_file(self, file_path):
        base, ext = os.path.splitext(file_path)
        
        # This is where you'd specify what to append to the file name
        output_path = base + "_converted.png"
        
        command = ["ffmpeg", "-y", "-i", file_path, output_path]
        subprocess.run(command)
        print(f"Converted {file_path} to {output_path}")

if __name__ == "__main__":
    # Set the path to the your folder
    downloads_folder = os.path.expanduser("path/to/folder")
    
    event_handler = FileConversionHandler()
    observer = Observer()
    observer.schedule(event_handler, downloads_folder, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
