import time  
from watchdog.observers import Observer  
from watchdog.events import PatternMatchingEventHandler 
import sys
import socket
import datetime
import os

class MyHandler(PatternMatchingEventHandler):
    patterns = "*"

    def process(self, event):
        """
        event.event_type 
            'modified' | 'created' | 'moved' | 'deleted'
        event.is_directory
            True | False
        event.src_path
            C:\site
        """
        # the file will be processed there
        print(event.src_path, event.event_type)  
        
        now = datetime.datetime.now()

        log_stream = str(now) + ' ' + str(event.src_path) + ' [' + str(os.path.getsize(event.src_path)) + ' byte ]' + ' ' + str(event.event_type)
        
        clients = [socket.socket(socket.AF_INET, socket.SOCK_STREAM) for i in range(MAX_CONNECTIONS)]
        for client in clients:
            client.connect(address_to_server)

        for i in range(MAX_CONNECTIONS):
            clients[i].send(bytes(log_stream, encoding='UTF-8'))
        
    def on_any_event(self, event):
        print(os.path.getsize(event.src_path))
    
    def on_modified(self, event):
        self.process(event)

    def on_created(self, event):
        self.process(event)

    def on_deleted(self, event):
        self.process(event)

    def on_moved(self, event):
        self.process(event)

if __name__ == '__main__':

    MAX_CONNECTIONS = 1
    
    address_to_server = ('localhost', 8686)

    args = sys.argv[1:]
    observer = Observer()
    observer.schedule(MyHandler(), path=args[0] if args else '.', recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(2)
            observer.join()
    except KeyboardInterrupt:
        observer.stop()

