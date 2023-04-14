import tkinter as tk
from tkinter import messagebox

class Gui:
	def __init__(self):
		self.root = tk.Tk()
		self.root.geometry("400x300")
		self.root.title("Számrendszer váltás")
		
		
		self.input_value = ""
		self.output_value = ""
		
		self.frame = tk.Frame(self.root)
		self.frame.columnconfigure(0, weight=1)
		self.frame.columnconfigure(1, weight=1)
		self.frame.columnconfigure(2, weight=1)
		self.frame.columnconfigure(3, weight=1)
		self.frame.pack(fill="x", padx=40, pady=20)
		
		self.input = tk.Label(self.frame, text="", height=1, width=5, bg="black", fg="white", font=("Consolas", 18))
		self.input.grid(row=0, column=1, columnspan=3, sticky= tk.W + tk.E, padx=10, pady=10)

		self.output = tk.Label(self.frame, height=1, width=5, text="", bg="black", fg="white", font=("Consolas", 18))
		self.output.grid(row=1, column=1, columnspan=3, sticky= tk.W + tk.E, padx=10, pady=10)
		
		self.one = tk.Button(self.frame, command=lambda: self.get_value("1"), text="1", font=("Consolas", 15))
		self.one.grid(row=2, column=0, sticky= tk.W + tk.E)
		self.twoo = tk.Button(self.frame, command=lambda: self.get_value("2"), text="2", font=("Consolas", 15))
		self.twoo.grid(row=2, column=1, sticky= tk.W + tk.E)
		self.three = tk.Button(self.frame, command=lambda: self.get_value("3"), text="3", font=("Consolas", 15))
		self.three.grid(row=2, column=2, sticky= tk.W + tk.E)
		self.c = tk.Button(self.frame, command=self.clear, text="Clear", font=("Consolas", 15))
		self.c.grid(row=2, column=3, sticky= tk.W +tk.E)
		
		self.four = tk.Button(self.frame, command=lambda: self.get_value("4"), text="4", font=("Consolas", 15))
		self.four.grid(row=3, column=0, sticky= tk.W + tk.E)
		self.five = tk.Button(self.frame, command=lambda: self.get_value("5"), text="5", font=("Consolas", 15))
		self.five.grid(row=3, column=1, sticky= tk.W + tk.E)
		self.six = tk.Button(self.frame, command=lambda: self.get_value("6"), text="6", font=("Consolas", 15))
		self.six.grid(row=3, column=2, sticky= tk.W + tk.E)
		self.backspace = tk.Button(self.frame, command=self.backspace, text="⌫", font=("Consolas", 15))
		self.backspace.grid(row=3, column=3, sticky= tk.W + tk.E)
		
		self.seven = tk.Button(self.frame, command=lambda: self.get_value("7"), text="7", font=("Consolas", 15))
		self.seven.grid(row=4, column=0, sticky= tk.W + tk.E)
		self.eight = tk.Button(self.frame, command=lambda: self.get_value("8"), text="8", font=("Consolas", 15))
		self.eight.grid(row=4, column=1, sticky= tk.W + tk.E)
		self.nine = tk.Button(self.frame, command=lambda: self.get_value("9"), text="9", font=("Consolas", 15))
		self.nine.grid(row=4, column=2, sticky= tk.W + tk.E)
		
		self.zero = tk.Button(self.frame, command=lambda: self.get_value("0"), text="0", font=("Consolas", 15))
		self.zero.grid(row=5, columnspan=3, sticky= tk.W + tk.E)
		self.root.mainloop()
	
	def get_value(self, value):
		if len(self.output.cget("text")) < 15:
			self.input_value += value
			self.input.config(text=self.input_value)
			self.atvaltas()
		else:
			pass
	
	def clear(self):
		self.input_value = ""
		self.input.config(text="")
		self.output_value = ""
		self.output.config(text="")

	def backspace(self):
		self.input_value = self.input_value[0:len(self.input_value) - 1]
		self.input.config(text=self.input_value)
		self.atvaltas()

	def atvaltas(self):
		if self.input_value != "":
			a = int(self.input_value)
			while a != 0:
				self.output_value += str(a % 2)
				a = int(a / 2)
			self.output.config(text=self.output_value)
			self.output_value = ""
		else:
			self.output_value = ""
			self.output.config(text="")


Gui()