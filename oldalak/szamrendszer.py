import tkinter as tk
from tkinter import messagebox

class Gui:
	def __init__(self):
		self.root = tk.Tk()
		self.root.geometry("400x500")
		self.root.title("Egyes számrendszer")
		
		self.input_value = ""
		
		self.frame = tk.Frame(self.root)
		self.frame.columnconfigure(0, weight=1)
		self.frame.columnconfigure(1, weight=1)
		self.frame.columnconfigure(2, weight=1)
		self.frame.columnconfigure(3, weight=1)
		self.frame.pack(fill="x", padx=40, pady=20)
		
		self.input = tk.Label(self.frame, text="", width=5, bg="gray")
		self.input.grid(row=0, columnspan=2, sticky= tk.W + tk.E, padx=10, pady=10)

		self.output = tk.Label(self.frame, text="", bg="gray")
		self.output.grid(row=0, column=2, columnspan=2, sticky= tk.W + tk.E, padx=10, pady=10)
		
		self.one = tk.Button(self.frame, command=lambda: self.get_value("1"), text="1")
		self.one.grid(row=1, column=0, sticky= tk.W + tk.E)
		self.twoo = tk.Button(self.frame, command=lambda: self.get_value("2"), text="2")
		self.twoo.grid(row=1, column=1, sticky= tk.W + tk.E)
		self.three = tk.Button(self.frame, command=lambda: self.get_value("3"), text="3")
		self.three.grid(row=1, column=2, sticky= tk.W + tk.E)
		self.c = tk.Button(self.frame, command=self.clear, text="Clear")
		self.c.grid(row=1, column=3, sticky= tk.W +tk.E)
		
		self.four = tk.Button(self.frame, command=lambda: self.get_value("4"), text="4")
		self.four.grid(row=2, column=0, sticky= tk.W + tk.E)
		self.five = tk.Button(self.frame, command=lambda: self.get_value("5"), text="5")
		self.five.grid(row=2, column=1, sticky= tk.W + tk.E)
		self.six = tk.Button(self.frame, command=lambda: self.get_value("6"), text="6")
		self.six.grid(row=2, column=2, sticky= tk.W + tk.E)
		self.backspace = tk.Button(self.frame, command=self.backspace, text="⌫")
		self.backspace.grid(row=2, column=3, sticky= tk.W + tk.E)
		
		self.seven = tk.Button(self.frame, command=lambda: self.get_value("7"), text="7")
		self.seven.grid(row=3, column=0, sticky= tk.W + tk.E)
		self.eight = tk.Button(self.frame, command=lambda: self.get_value("8"), text="8")
		self.eight.grid(row=3, column=1, sticky= tk.W + tk.E)
		self.nine = tk.Button(self.frame, command=lambda: self.get_value("9"), text="9")
		self.nine.grid(row=3, column=2, sticky= tk.W + tk.E)
		
		self.zero = tk.Button(self.frame, command=lambda: self.get_value("0"), text="0").grid(row=4, columnspan=3, sticky= tk.W + tk.E)
		self.root.mainloop()
	
	def get_value(self, value):
		if len(self.input_value) != 20:
			self.input_value += value
			self.input.config(text=self.input_value)
		else:
			tk.messagebox.showinfo(self.root, message="valami nem jo gec\n(elérted a max karakterszámot)")
	
	def clear(self):
		self.input_value = ""
		self.input.config(text=self.input_value)

	def backspace(self):
		self.input_value = self.input_value[0:len(self.input_value) - 1]
		self.input.config(text=self.input_value)

Gui()