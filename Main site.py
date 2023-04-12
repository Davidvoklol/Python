import tkinter as tk
from tkinter import messagebox
import time



class Window:
    def __init__(self, bg):
        self.bg = bg
        self.window = tk.Tk()
        self.window.geometry("800x500")
        self.window.title("Main site")
        self.window.config(bg=self.bg)
        self.time = tk.Label(self.window, text="00:00", bg="gray", fg="white")
        self.time.pack(pady=10)
        self.thetime()
        self.window.mainloop()
    
    def thetime(self):
        time_var = time.strftime("%H:%M")
        self.time.config(text=str(time_var))
        self.time.after(200, self.thetime)

        

Window("black")