#!/usr/bin/env python

import time
import json
import pathlib

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class ChatEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        filename = event.src_path
        with open(filename, encoding='utf-8') as fin:
            chat = json.load(fin)
            print("{name} says: {message}".format(**chat))


def main():
    HOME_DIR = pathlib.Path('./')
    print("Starting ChatDog", end=" ")
    event_handler = ChatEventHandler()
    observer = Observer()
    observer.schedule(event_handler, HOME_DIR, recursive=False)
    observer.start()
    print("[OK]")
    try:
        while True:
            time.sleep(10)
    finally:
        observer.stop()
        observer.join()


if __name__ == "__main__":
    main()
