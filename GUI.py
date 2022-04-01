import os
import reading_functions as read
import copy
import Circuit

from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox as mb
# from PIL import ImageTK, Image
# pip install Pillow

chassis_name = 'Eco1C1G1T1'
input_dir = os.getcwd() + '/input/' 

# Get input signals from *.input.json file
input_signals = read.read_input_json(input_dir + chassis_name + '.input.json')[0]

       
# Get output signals from *.output.json file
output_signals = read.read_output_json(input_dir + chassis_name + '.output.json')[0]

    
# Get assignment from *.UCF.json file
ucf_signals = read.read_ucf_json(input_dir + chassis_name + '.UCF.json')[0]


root = Tk()
root.title("Genetic Circuit Design Automation")
# root.iconbitmap('filepath/iconname.ico')
root.geometry("1280x720")

# Creating frames
frame = LabelFrame(root, width = 1200, height = 500, text="Main Frame", pady=5)
frame.grid(row=0, column=0, columnspan=5, padx=20)
frame.grid_propagate(0)


container = ttk.Frame(root, width = 1200, height = 500)
canvas = Canvas(container)
scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

container.grid(row=0, column=0, columnspan=5, padx=20)
canvas.grid(padx=400, sticky=W)
scrollbar.grid(padx=400, sticky=E)


scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)


p_frame = LabelFrame(root, width = 200 , height = 200, text="Promoters:")
p_frame.grid(row=1, column=0, rowspan=4)
p_frame.grid_propagate(0)


g_frame = LabelFrame(root, width = 200 , height = 200, text="UCF Gates:")
g_frame.grid(row=1, column=1, rowspan=4)
g_frame.grid_propagate(0)

o_frame = LabelFrame(root, width = 200 , height = 200, text="Output Gates:")
o_frame.grid(row=1, column=2, rowspan=4)
o_frame.grid_propagate(0)

# Function for promoters combobox
def selected_p(event):
	# name = combo1.get()
	# new_gate = copy.deepcopy(input_signals[name])
	myLabel = Label(p_frame, text = combo1.get()).grid()

# Function for gates combobox
def selected_g(event):
	myLabel = Label(g_frame, text = combo2.get()).grid()

# Function
def selected_o(event):
	myLabel = Label(o_frame, text = combo3.get()).grid()

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


	#pass filename into function that will read lines of command

def generate_circuit():
	
	button_circuit['state'] = 'disabled'

	stats = c.BFS()
	myLabel = Label(scrollable_frame, text = stats ).grid()

	#call function that will create graph and visualize it -> display on frame

def optimize_circuit():
	#connect with optimization function and produce message window comparing
	#the results of the old and optimized circuit
	return

def reset():
	if button_circuit['state'] == 'disabled':
		button_circuit['state'] = 'normal'

	for widget in p_frame.winfo_children():
		widget.destroy()

	for widget in g_frame.winfo_children():
		widget.destroy()

	for widget in o_frame.winfo_children():
		widget.destroy()

	for widget in frame.winfo_children():
		widget.destroy()



promoters = read.read_input_json(input_dir + chassis_name + '.input.json')[1]

UCF_gates = read.read_ucf_json(input_dir + chassis_name + '.UCF.json')[1]

output_gates = read.read_output_json(input_dir + chassis_name + '.output.json')[1]


# # clicked = StringVar()
# # clicked.set("Select Promoters")

# # drop = OptionMenu(root, clicked, *promoters)
# # drop.pack()

combo1 = ttk.Combobox(root, value=promoters)
combo1.set("Select Promoter(s)")
combo1.bind("<<ComboboxSelected>>", selected_p)
combo1['state'] = 'readonly'
combo1.grid(row=1, column=3)

combo2 = ttk.Combobox(root, value=UCF_gates)
combo2.set("Select UCF gate(s)")
combo2.bind("<<ComboboxSelected>>", selected_g)
combo2['state'] = 'readonly'
combo2.grid(row=2, column=3)

combo3 = ttk.Combobox(root, value=output_gates)
combo3.set("Select output gate(s)")
combo3.bind("<<ComboboxSelected>>", selected_o)
combo3['state'] = 'readonly'
combo3.grid(row=3, column=3)

button_upload = Button(root, text = "Upload file", command=upload)
button_upload.grid(row=4, column=3)

button_circuit = Button(root, text="Design circuit", command=generate_circuit)
button_circuit.grid(row=1, column=4)

button_optimize = Button(root, text="Optimize circuit", command=optimize_circuit)
button_optimize.grid(row=2, column=4)

button_reset = Button(root, text="Start over", command=reset)
button_reset.grid(row=3, column=4)

button_quit = Button(root, text="Exit", command=root.quit)
button_quit.grid(row=4, column=4)


# #my_img = ImageTk.PhotoImage(Image.open("filename.png"))
# #my_label = Label(image=my_img)
# #my_label.pack()

root.mainloop()