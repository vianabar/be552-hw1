import argparse
import os
import reading_functions as read
import copy
import Circuit

from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
import networkx as nx


# Parse for chassis and input file path arguments
parser = argparse.ArgumentParser(description='Create genetic circuit from input files')
parser.add_argument('-l','--library_path',help='path for chassis libraries dir')
parser.add_argument('-c','--chassis_name',help='chassis name')
#parser.add_argument('-o','--output',help='path for the left and right output CSVs for vertext-wise cortical thickness from freesurfer output')

args = parser.parse_args()

chassis_name = args.chassis_name
library_path = args.library_path

# Get input signals from *.input.json file
input_signals = read.read_input_json(library_path + '/' + chassis_name + '.input.json')[0]

# Get output signals from *.output.json file
output_signals = read.read_output_json(library_path + '/' + chassis_name + '.output.json')[0]

    
# Get assignment from *.UCF.json file
ucf_signals = read.read_ucf_json(library_path + '/' + chassis_name + '.UCF.json')[0]


# Creating main GUI window
root = Tk()
root.title("Genetic Circuit Design Automation")
# root.iconbitmap('filepath/iconname.ico')
root.geometry("1920x1080")

# Creating frames
frame = LabelFrame(root, width = 700, height = 500, text="Main Frame", pady=5)
frame.grid(row=0, column=0, columnspan=3, padx=20)
frame.grid_propagate(0)

container = LabelFrame(root, width = 700, height = 450)
canvas = Canvas(container, width=650, height = 450)
scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas, width = 600, height = 450)

container.grid(row=0, column=0, columnspan=3, sticky=W, padx=20)
canvas.grid(row=0, column=0, columnspan=3, sticky=W, padx=20)
scrollbar.grid(row=0, column = 2, columnspan=3,sticky=E)


scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)


canvas.create_window((0, 0), window=scrollable_frame, anchor=W)
canvas.configure(yscrollcommand=scrollbar.set)

plot_frame = LabelFrame(root, width = 680 , height = 500, text="Circuit Visualization", pady=5)
plot_frame.grid(row=0, column=3, columnspan=4)
plot_frame.grid_propagate(0)

p_frame = LabelFrame(root, width = 200 , height = 200, text="Promoters:")
p_frame.grid(row=1, column=0, rowspan=4)
p_frame.grid_propagate(0)

g_frame = LabelFrame(root, width = 200 , height = 200, text="UCF Gates:")
g_frame.grid(row=1, column=1, rowspan=4)
g_frame.grid_propagate(0)

o_frame = LabelFrame(root, width = 200 , height = 200, text="Output Gates:")
o_frame.grid(row=1, column=2, rowspan=4)
o_frame.grid_propagate(0)


# Function for gates combobox
def selected_g(event):
	gate = combo1.get()
	return 

	# myLabel = Label(p_frame, text = combo1.get()).grid()

# # Function for gates combobox
# def selected_g(event):
# 	myLabel = Label(g_frame, text = combo2.get()).grid()

# # Function for output combobox
def selected_op(event):
	return

# Function for operations to optimize circuit

def get_xval():
	xval = float(xval_entry.get())
	gate = combo1.get()
	operation_str = combo2.get()

	c.operate(operation_str, xval, gate)
	generate_circuit()

# Function for upload button for user to upload txt file with commands
def upload():
	filetypes = (
		('text files', '*.txt'),
		('spreadsheet files', '*.xlsx')

	)

	filename = fd.askopenfilename(
		title='Open a file',
		initialdir=os.getcwd(),
		filetypes=filetypes
		)

	with open(filename) as f:
		lines = f.readlines()

	global c
	c = Circuit.Circuit()

	for line in lines:
		if not line.isspace():
			exec(line)


	# mb.showinfo(
	# 	title='Selected File',
	# 	message=better_lines
	# )

# Generates genetic circuit stats and graph based on gates and connections that user created
def generate_circuit():

	try:
		c
	except NameError:
		print("Error! No gates assigned yet!")
		mb.showinfo(
			title='Error!',
			message="No gates assigned yet!"
		)

	if c.V == 0:
		print("Error! No gates assigned yet!")
		mb.showinfo(
			title='Error!',
			message="No gates assigned yet!"
		)
	else:
		button_circuit['state'] = 'disabled'

		# Call BFS function and display circuit stats (e.g. score, truthtable) on window
		stats = c.BFS()
		myLabel = Label(scrollable_frame, text = stats, anchor=E, justify=LEFT, font = "monaco").grid()

		# Create graph and visualize it -> display on plot_frame
		G = c.visualize()
		
		f = plt.figure(figsize=(5,4))
		a = f.add_subplot(111)
		ax = plt.gca()
		ax.margins(0.3)
		ax.patch.set_alpha(0.0)
		plt.axis('off')
		plt.box(False)

		# Drawing the graph
		pos=nx.circular_layout(G)
		nx.draw_networkx(G,ax=a, arrows=True, font_size=6, font_color='k', edge_color='y', node_color = 'b', node_size=300)
		
		# Placing the canvas on the frame
		canvas = FigureCanvasTkAgg(f, plot_frame)
		canvas.draw()
		canvas.get_tk_widget().grid()

		gates_dict = dict()
		for name in c.adjList:
			if(name != c.root.name):
				gates.append(name)

		combo1['values'] = gates

    
# Automatically performs the operations that best optimize the circuit
def optimize_circuit():
	#connect with optimization function and produce message window comparing
	#the results of the old and optimized circuit
	return

# Clears all gates selected/created and erases graph + stats from window
def reset():
	if button_circuit['state'] == 'disabled':
		button_circuit['state'] = 'normal'

	for widget in p_frame.winfo_children():
		widget.destroy()

	for widget in g_frame.winfo_children():
		widget.destroy()

	for widget in o_frame.winfo_children():
		widget.destroy()

	for widget in scrollable_frame.winfo_children():
		widget.destroy()

	for widget in plot_frame.winfo_children():
		widget.destroy()

	c.clear() # does not seem to work

	# need to delete gate objects

# Automatically retrieving list of promoter names, gate names and output names
# promoters = read.read_input_json(library_path + '/' + chassis_name + '.input.json')[1]

# UCF_gates = read.read_ucf_json(library_path + '/' + chassis_name + '.UCF.json')[1]

# output_gates = read.read_output_json(library_path + '/' + chassis_name + '.output.json')[1]

gates=[]

operations = (
	"stretch",
	"increase slope",
	"decrease slope",
	"stronger_prom",
	"weaker_prom",
	"stronger RBS",
	"weaker RBS"
	)

# Creating comboboxes for different selections user can make in designing circuit
combo1 = ttk.Combobox(root, value=gates)
combo1.set("Select gate to modify")
combo1.bind("<<ComboboxSelected>>", selected_g)
combo1['state'] = 'readonly'
combo1.grid(row=1, column=3)

# combo2 = ttk.Combobox(root, value=UCF_gates)
# combo2.set("Select UCF gate(s)")
# combo2.bind("<<ComboboxSelected>>", selected_g)
# combo2['state'] = 'readonly'
# combo2.grid(row=2, column=3)

# combo3 = ttk.Combobox(root, value=output_gates)
# combo3.set("Select output gate(s)")
# combo3.bind("<<ComboboxSelected>>", selected_o)
# combo3['state'] = 'readonly'
# combo3.grid(row=3, column=3)

combo2 = ttk.Combobox(root, value=operations)
combo2.set("Select operation to perform")
combo2.bind("<<ComboboxSelected>>", selected_op)
combo2['state'] = 'readonly'
combo2.grid(row=1, column=5, columnspan=1)

xval = StringVar()
xval.set("Enter x value for operation: ")
xval_entry = Entry(root,bd =5, textvariable = xval, width=20)
xval_entry.grid(row=2, column=5)
button_xval = Button(root, text = "Ok", command=get_xval, width=1)
button_xval.grid(row=2, column=6, sticky=W)
root.grid_columnconfigure(4, weight=1)
root.grid_columnconfigure(3, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(4, weight=1)

button_upload = Button(root, text = "Upload file", command=upload)
button_upload.grid(row=4, column=3)

button_circuit = Button(root, text="Design circuit", command=generate_circuit, bg='yellow')
button_circuit.grid(row=1, column=4)

button_optimize = Button(root, text="Optimize circuit", command=optimize_circuit)
button_optimize.grid(row=2, column=4)

button_reset = Button(root, text="Start over", command=reset)
button_reset.grid(row=4, column=4)

button_quit = Button(root, text="Exit", command=root.quit, bg='red')
button_quit.grid(row=4, column=5)

root.mainloop()