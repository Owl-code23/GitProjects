from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

def calculate():
    input = float(entry.get())
    convert = input * 1.609
    result["text"] = f"{convert:.2f}"

is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

miles_unit = Label(text="Miles")
miles_unit.grid(column=2, row=0)

km_unit = Label(text="Km")
km_unit.grid(column=2, row=1)

result = Label(text="0")
result.grid(column=1, row=1)

entry = Entry(width=10)
entry.grid(column=1, row=0)

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

window.mainloop()