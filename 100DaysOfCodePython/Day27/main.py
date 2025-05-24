from tkinter import *
import turtle

window = Tk()
window.title("My First GUI Program")
window.minsize(500, 300)
window.config(padx=100, pady=200)

# bob = turtle.Turtle()
# bob.write("Some text")

#Label
my_label = Label(text="I am a label", font=("Arial", 24, "italic"))
# my_label.pack()
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# my_label["text"] = "New Text"
# my_label.config(text="New Text2")

#Button
def button_clicked():
    my_label["text"] = input.get()
button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1,row=1)

#New Button
button2 = Button(text="Click Me", command=button_clicked)
button2.grid(column=2, row=0)

#Entry
input = Entry(width=30)
input.insert(END, string="Some text to begin with.")
print(input.get())
# input.pack()
input.grid(column=3, row=2)

#Text
text = Text(height=5, width=30)
text.focus()
text.insert(END, "Example of multi-line text entry.")
print(text.get("1.5", END))
# text.pack()

#Spinbox
def spinbox_used():
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()

#Scale
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
# scale.pack()

#Checkbutton
def checkbutton_used():
    print(checked_state.get())
checked_state = IntVar()
checkbutton = Checkbutton(text="Is on?", variable=checked_state, command=checkbutton_used)
checked_state.get()
# checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()

#Listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>",listbox_used)
# listbox.pack()

window.mainloop()