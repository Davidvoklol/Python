import tkinter as tk
from tkinter import messagebox
import time
import os



class Window:
    def __init__(self, bg):
        self.bg = bg
        self.window = tk.Tk()
        self.window.geometry("1600x1000")
        self.window.title("Main site")
        self.window.config(bg=self.bg)
        self.time = tk.Label(self.window, text="00:00", bg="gray", fg="white", font=("Terminal", 30, "bold"))
        self.time.pack(pady=10)

        self.menuframe = tk.Frame(self.window, bg=self.bg)
        self.menuframe.columnconfigure(0, weight=1)
        self.menuframe.columnconfigure(1, weight=1)
        self.menuframe.columnconfigure(2, weight=1)
        self.menuframe.pack(fill="x", padx=70, pady=50)

        self.szamrendszer = tk.Button(self.menuframe, command=self.szamrendszer, text="Számrendszer vátó", bg="gray", fg="black", activebackground="gray", activeforeground="black", font=("Consolas", 20, "bold")).grid(row=0, column=0, sticky=tk.W + tk.E)
        self.thetime()
        self.window.mainloop()
    
    def thetime(self):
        time_var = time.strftime("%H:%M:%S")
        self.time.config(text=str(time_var))
        self.time.after(200, self.thetime)
    
    def szamrendszer(self):
        os.startfile("oldalak\\szamrendszer.py")
        self.window.destroy()
        
        

Window("black")