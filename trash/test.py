import os
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class RestartHandler(FileSystemEventHandler):
    def __init__(self, script):
        self.script = script

    def on_modified(self, event):
        if event.src_path.endswith('.py'):
            print(f"{event.src_path} has been modified, restarting the bot...")
            os.execv(sys.executable, ['python'] + [self.script])

if __name__ == "__main__":
    script_to_run = 'main2.py'  # Replace with the name of your bot script

    event_handler = RestartHandler(script_to_run)
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
