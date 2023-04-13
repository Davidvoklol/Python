import tkinter as tk

class Gui:
	def __init__(self):
		self.root = tk.Tk()
		self.root.geometry("400x500")
		self.root.title()
		
		self.input = ""
		
		self.frame = tk.Frame(self.root)
		self.frame.columnconfigure(0, weight=1)
		self.frame.columnconfigure(1, weight=1)
		self.frame.columnconfigure(2, weight=1)
		self.frame.columnconfigure(3, weight=1)
		self.frame.pack(fill="x", padx=40, pady=20)
		
		self.label = tk.Label(self.frame, text="")
		self.label.grid(row=0, columnspan=4)
		
		self.one = tk.Button(self.frame, command=lambda: self.get_value("1"), text="1")
		self.one.grid(row=1, column=0, sticky= tk.W + tk.E)
		self.twoo = tk.Button(self.frame, text="2")
		self.twoo.grid(row=1, column=1, sticky= tk.W + tk.E)
		self.three = tk.Button(self.frame, text="3")
		self.three.grid(row=1, column=2, sticky= tk.W + tk.E)
		self.c = tk.Button(self.frame, command=self.clear, text="C")
		self.c.grid(row=1, column=3, sticky= tk.W +tk.E)
		
		self.four = tk.Button(self.frame, text="4")
		self.four.grid(row=2, column=0, sticky= tk.W + tk.E)
		self.five = tk.Button(self.frame, text="5")
		self.five.grid(row=2, column=1, sticky= tk.W + tk.E)
		self.six = tk.Button(self.frame, text="6")
		self.six.grid(row=2, column=2, sticky= tk.W + tk.E)
		self.ac = tk.Button(self.frame, text="AC")
		self.ac.grid(row=2, column=3, sticky= tk.W + tk.E)
		
		self.seven = tk.Button(self.frame, text="7")
		self.seven.grid(row=3, column=0, sticky= tk.W + tk.E)
		self.eight = tk.Button(self.frame, text="8")
		self.eight.grid(row=3, column=1, sticky= tk.W + tk.E)
		self.nine = tk.Button(self.frame, text="9")
		self.nine.grid(row=3, column=2, sticky= tk.W + tk.E)
		
		self.zero = tk.Button(self.frame, text="0").grid(row=4, columnspan=3, sticky= tk.W + tk.E)
		self.root.mainloop()
	
	def get_value(self, value):
		self.input += value
		self.label.config(text=self.input)
	
	def clear(self):
		self.input = ""
		self.label.config(text=self.input)

Gui()