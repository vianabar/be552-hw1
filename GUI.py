from tkinter import *

root = Tk()
root.title("Genetic Circuit Design Automation")

# Button function
def myClick():
	myLabel = Label(root, text="Hello " + e.get())
	myLabel.pack()

# Creating an Entry Widget
e = Entry(root, width=35, borderwidth=5)
e.grid(row=1, column=1, columnspan=3, padx=10, pady=10)
e.insert(0,"Enter your name: ")

# # Creating a Label Widget
# myLabel1 = Label(root, text="Hello World!")
# myLabel2 = Label(root, text="This is line 2")

# # Put onto screen
# myLabel1.grid(row=0, column=0)
# myLabel2.grid(row=1, column=1)

# Creating a Button
myButton = Button(root, text="Enter your name!", command=myClick)
#other parameters for button: state=DISABLED, padx=50, pady=50, fg, bg
myButton.pack()





root.mainloop()

