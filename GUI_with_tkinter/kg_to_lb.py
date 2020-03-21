from tkinter import *


window = Tk()


def km_to_other():
    gram = float(e1_value.get())*1000.0
    txt1.insert(END, gram)
    ounce = float(e1_value.get())*2.20462
    txt2.insert(END, ounce)
    pound = float(e1_value.get())*35.274
    txt3.insert(END, pound)


kg = Label(window, text="kg")
kg.grid(row=0, column=0)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=2)

btn1 = Button(window, text="Convert", command=km_to_other)
btn1.grid(row=0, column=3)


txt1 = Text(window, height=1, width=20)
txt1.grid(row=1, column=0)

txt2 = Text(window, height=1, width=20)
txt2.grid(row=1, column=2)

txt3 = Text(window, height=1, width=20)
txt3.grid(row=1, column=3)

window.mainloop()
