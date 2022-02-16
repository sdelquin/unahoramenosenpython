#!/usr/bin/env python

import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class SimpleHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"hay un nuevo fichero {event.src_path}!")


def main():
    my_observer = Observer()
    my_observer.schedule(my_event_handler, '.', recursive=True)
    my_observer.start()
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        my_observer.stop()
        my_observer.join()


if __name__ == "__main__":
    main()
