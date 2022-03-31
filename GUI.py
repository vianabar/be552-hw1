import os
import reading_functions as read

from tkinter import *
from tkinter import ttk
# from PIL import ImageTK, Image
# pip install Pillow

chassis_name = 'Eco1C1G1T1'
input_dir = os.getcwd() + '/input/' 

root = Tk()
root.title("Genetic Circuit Design Automation")
# root.iconbitmap('filepath/iconname.ico')
root.geometry("1280x720")

frame = LabelFrame(root, width = 800, height = 500, text="This is my frame..", padx=100, pady=5)
frame.pack(expand=True, fill='both')
frame.pack_propagate(0)

p_frame = LabelFrame(root, width = 200 , height = 200, text="Promoters:")
p_frame.pack(side = LEFT)
p_frame.pack_propagate(0)


g_frame = LabelFrame(root, width = 200 , height = 200, text="UCF Gates:")
g_frame.pack(side = LEFT)
g_frame.pack_propagate(0)

o_frame = LabelFrame(root, width = 200 , height = 200, text="Output Gates:")
o_frame.pack(side = LEFT)
o_frame.pack_propagate(0)


def selected_p(event):
	myLabel = Label(p_frame, text = combo1.get()).pack()

def selected_g(event):
	myLabel = Label(g_frame, text = combo2.get()).pack()

def selected_o(event):
	myLabel = Label(o_frame, text = combo3.get()).pack()

def generate_circuit():
	myLabel = Label(frame, text = "Circuit will show here").pack()
	button_circuit['state'] = 'disabled'

def reset():
	if button_circuit['state'] == 'disabled':
		button_circuit['state'] = 'normal'

	# for widget in p_frame.winfo_children():
 #       widget.destroy()


promoters = read.read_input_json(input_dir + chassis_name + '.input.json')[1]

UCF_gates = read.read_ucf_json(input_dir + chassis_name + '.UCF.json')[1]

output_gates = read.read_output_json(input_dir + chassis_name + '.output.json')[1]


# promoters = [
# 	"Promoter1", 
# 	"Promoter2", 
# 	"Promoter3", 
# 	"Promoter4"
# ]

# UCF_gates = [
# 	"UCF_g1", 
# 	"UCF_g2", 
# 	"UCF_g3", 
# 	"UCF_g4"
# ]

# output_gates = [
# 	"output_g1", 
# 	"output_g2", 
# 	"output_g3", 
# 	"output_g4"
# ]


# clicked = StringVar()
# clicked.set("Select Promoters")

# drop = OptionMenu(root, clicked, *promoters)
# drop.pack()

combo1 = ttk.Combobox(root, value=promoters)
combo1.set("Select Promoter(s)")
combo1.bind("<<ComboboxSelected>>", selected_p)
combo1['state'] = 'readonly'
combo1.pack()

combo2 = ttk.Combobox(root, value=UCF_gates)
combo2.set("Select UCF gate(s)")
combo2.bind("<<ComboboxSelected>>", selected_g)
combo2['state'] = 'readonly'
combo2.pack()

combo3 = ttk.Combobox(root, value=UCF_gates)
combo3.set("Select output gate(s)")
combo3.bind("<<ComboboxSelected>>", selected_o)
combo3['state'] = 'readonly'
combo3.pack()

button_reset = Button(root, text="Start over", command=reset)
button_reset.pack(side=RIGHT)

button_circuit = Button(root, text="Design circuit", command=generate_circuit)
button_circuit.pack(side=RIGHT)

button_quit = Button(root, text="Exit", command=root.quit)
button_quit.pack(side= BOTTOM)

#my_img = ImageTk.PhotoImage(Image.open("filename.png"))
#my_label = Label(image=my_img)
#my_label.pack()

root.mainloop()