===============
Python Trivia 1
===============

Tk file dialogs
===============

Here is a simple way to use Tk to add open/save file dialogs in Python3

.. code-block:: py3

   import os
   import tkinter as tk
   from tkinter import filedialog

   root = tk.Tk()
   root.withdraw()
   
   # get a directory
   directory = filedialog.askdirectory()
   
   # get a list of the csv files in that directory
   file_names = [f for f in os.listdir(directory) if f.endswith('.csv')]
   file_name = os.path.join(directory, file_names[0])  # full path
   
   # get a filename that you can open
   filename = tkFileDialog.askopenfilename(initialfile='data.dat', \
       filetypes=[('data', '*.dat'), ('csv', '*.csv')])

   # get an open file
   openfile = tkFileDialog.askopenfile(mode='r', initialfile='data.dat', \
       filetypes=[('data', '*.dat'), ('csv', '*.csv')])

   # use asksaveasfile/asksaveasfilename for files to write
   
   # make sure other windows work when finished
   root.destroy()


Here is some code that should work in either Python2 or Python3

.. code-block:: py3

   try:
       #python3
       import tkinter as tk
       from tkinter import filedialog
   except:
       #python2
       import Tkinter as tk
       import tkFileDialog as filedialog

   filename = filedialog.askopenfilename(filetypes=[('csv','*.csv')])



TTK Demo 1
==========

.. code-block:: py3

	from tkinter import *
	from tkinter import ttk
	root = Tk()
	button = ttk.Button(root, text="Hello World").grid()
	root.mainloop()


TTK Demo 2
==========

.. code-block:: py3

	from tkinter import *
	from tkinter import ttk

	def calculate(*args):
		try:
		    value = float(feet.get())
		    meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
		except ValueError:
		    pass
		
	root = Tk()
	root.title("Feet to Meters")

	mainframe = ttk.Frame(root, padding="3 3 12 12")
	mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
	mainframe.columnconfigure(0, weight=1)
	mainframe.rowconfigure(0, weight=1)

	feet = StringVar()
	meters = StringVar()

	feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
	feet_entry.grid(column=2, row=1, sticky=(W, E))

	ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
	ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

	ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
	ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
	ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

	for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

	feet_entry.focus()
	root.bind('<Return>', calculate)

	root.mainloop()


TTK Demo 3
==========

.. code-block:: py3

	from tkinter import *
	from tkinter import ttk

	root = Tk()

	content = ttk.Frame(root)
	frame = ttk.Frame(content, borderwidth=5, relief="sunken", width=200, height=100)
	namelbl = ttk.Label(content, text="Name")
	name = ttk.Entry(content)

	onevar = BooleanVar()
	twovar = BooleanVar()
	threevar = BooleanVar()
	onevar.set(True)
	twovar.set(False)
	threevar.set(True)

	one = ttk.Checkbutton(content, text="One", variable=onevar, onvalue=True)
	two = ttk.Checkbutton(content, text="Two", variable=twovar, onvalue=True)
	three = ttk.Checkbutton(content, text="Three", variable=threevar, onvalue=True)
	ok = ttk.Button(content, text="Okay")
	cancel = ttk.Button(content, text="Cancel")

	content.grid(column=0, row=0)
	frame.grid(column=0, row=0, columnspan=3, rowspan=2)
	namelbl.grid(column=3, row=0, columnspan=2)
	name.grid(column=3, row=1, columnspan=2)
	one.grid(column=0, row=3)
	two.grid(column=1, row=3)
	three.grid(column=2, row=3)
	ok.grid(column=3, row=3)
	cancel.grid(column=4, row=3)

	root.mainloop()
