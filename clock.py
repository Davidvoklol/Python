import tkinter as tk
import time


window = tk.Tk()
window.geometry("800x500")
window.title("Clock")
window.config(bg="black")

title = tk.Label(window, text="Clock", font=("Arial", 70, "bold"), bg="black", fg="white")
title.pack()


labelframe = tk.Frame(window, bg="black")


labelframe.columnconfigure(0, weight=1)
labelframe.columnconfigure(1, weight=1)
labelframe.columnconfigure(2, weight=1)




def get_time():
    thetime = time.strftime("%H:%M:%S")
    display_time.config(text=thetime)
    worldclock.after(200, get_time)

worldclock = tk.Label(labelframe, text="World clock", font=("Arial", 20, "bold"), bg="gray")
worldclock.grid(row=0, column=0, sticky=tk.W+tk.E, padx=5)

display_time = tk.Label(labelframe, text="", font=("Arial", 15), bg="gray")
display_time.grid(row=1, column=0, sticky=tk.W+tk.E, padx=5, pady=5)
get_time()




counter = tk.Label(labelframe, text="Counter", font=("Arial", 20, "bold"), bg="Blue")
counter.grid(row=0, column=2, sticky=tk.W+tk.E, padx=5)




Timer = tk.Label(labelframe, text="Timer", font=("Arial", 20, "bold"), bg="green")
Timer.grid(row=0, column=1, sticky=tk.W+tk.E, padx=5)




labelframe.pack(pady=20, padx=10, fill="x")







window.mainloop()