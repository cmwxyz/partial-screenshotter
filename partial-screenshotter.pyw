import pyautogui
import tkinter as tk
import os
import re
from pathlib import Path


class oui_gui:

    def __init__(self):
        
        self.root = tk.Tk()
        self.root.attributes('-alpha', .01)
        self.root.attributes('-fullscreen', True)
        self.root.attributes("-topmost", True)

        self.surface = tk.Canvas(self.root, cursor="cross", bg="gray1")
        self.surface.pack(fill=tk.BOTH, expand=tk.YES)
        
        self.surface.bind("<ButtonPress-1>", self.you_click)
        self.surface.bind("<ButtonRelease-1>", self.you_die)

        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0

        self.download_path = os.path.abspath(r'C:\Users\YOURUSERNAMEHERE\Desktop')

        self.my_filename_pre = "screenshot-"
        self.my_filename_num = 1
        self.my_filename_suf = ".png"
        self.my_filename = self.my_filename_pre + str(self.my_filename_num) + self.my_filename_suf
        self.pattern = re.compile("^screenshot-(\d+)\.png$")

        self.root.mainloop()
        print("goodbye")

    def you_click(self, event):
        self.x1 = event.x
        self.y1 = event.y
        print("you clicked at: " + str(event.x) + "," + str(event.y))

    def check_filename(self):
        for filename in os.listdir(self.download_path):
            result = self.pattern.search(filename)	
            if result == None:
                continue
            if int(result.group(1)) == self.my_filename_num:
                self.my_filename_num += 1
            self.my_filename = self.my_filename_pre + str(self.my_filename_num) + self.my_filename_suf

    def get_quadtuple(self):
        if self.x1 < self.x2 and self.y1 < self.y2:
            self.t1 = self.x2-self.x1
            self.t2 = self.y2-self.y1
            return (self.x1, self.y1, self.t1, self.t2)
        elif self.x1 > self.x2 and self.y1 > self.y2:
            self.t1 = self.x1-self.x2
            self.t2 = self.y1-self.y2
            return (self.x2, self.y2, self.t1, self.t2)
        elif self.x1 > self.x2 and self.y1 < self.y2:
            self.t1 = self.x1-self.x2
            self.t2 = self.y2-self.y1
            return (self.x2, self.y1, self.t1, self.t2)
        elif self.x1 < self.x2 and self.y1 > self.y2:
            self.t1 = self.x2-self.x1
            self.t2 = self.y1-self.y2
            return (self.x1, self.y2, self.t1, self.t2)
        else:
            print("something went wrong")
            return (1, 1, 300, 300)

    def you_die(self, event):
        self.x2 = event.x
        self.y2 = event.y
        
        self.width = 1
        self.height = 1

        self.quadtuple = self.get_quadtuple()

        print("you released at: " + str(event.x) + "," + str(event.y))
        self.check_filename()
        self.my_screenshot = pyautogui.screenshot(region=self.quadtuple)
        self.my_screenshot.save(Path(self.download_path) / Path(self.my_filename))
        exit()
    
oui_gui()
