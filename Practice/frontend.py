import backend
from tkinter import *

window = Tk()

window.wm_title("BookStore")


def get_selected_row(event):
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except IndexError:
        pass


def view_command():
    for row in backend.view():
        list1.insert(END, row)


def insert_command():
    list1.delete(0, END)
    backend.insert(title_txt.get(), author_txt.get(),
                   year_txt.get(), isbn_txt.get())
    list1.delete(0, END)
    list1.insert(END, (title_txt.get(), author_txt.get(),
                       year_txt.get(), isbn_txt.get()))


def search_command():
    list1.delete(0, END)
    for row in backend.search(title_txt.get(), author_txt.get(), year_txt.get(), isbn_txt.get()):
        list1.insert(END, row)


def delete_command():
    backend.delete(selected_tuple[0])


def update_command():
    backend.update(selected_tuple[0], title_txt.get(
    ), author_txt.get(), year_txt.get(), isbn_txt.get())


title_lbl = Label(window, text="Title")
title_lbl.grid(row=0, column=0)

# title_txt = Text(window, height=1, width=20)
# title_txt.grid(row=0, column=1)

author_lbl = Label(window, text="Author")
author_lbl.grid(row=0, column=2)

# author_txt = Text(window, height=1, width=20)
# author_txt.grid(row=0, column=3)

year_lbl = Label(window, text="Year")
year_lbl.grid(row=1, column=0)

# year_txt = Text(window, height=1, width=20)
# year_txt.grid(row=0, column=3)

isbn_lbl = Label(window, text="ISBN")
isbn_lbl.grid(row=1, column=2)

# isbn_txt = Text(window, height=1, width=20)
# isbn_txt.grid(row=0, column=3)

list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

title_txt = StringVar()
e1 = Entry(window, textvariable=title_txt)
e1.grid(row=0, column=1)

author_txt = StringVar()
e2 = Entry(window, textvariable=author_txt)
e2.grid(row=0, column=3)

year_txt = StringVar()
e3 = Entry(window, textvariable=year_txt)
e3.grid(row=1, column=1)

isbn_txt = StringVar()
e4 = Entry(window, textvariable=isbn_txt)
e4.grid(row=1, column=3)


btn1 = Button(window, text="View all", width=12, command=view_command)
btn1.grid(row=2, column=3)

btn2 = Button(window, text="Search entry", width=12, command=search_command)
btn2.grid(row=3, column=3)

btn3 = Button(window, text="Add entry", width=12, command=insert_command)
btn3.grid(row=4, column=3)

btn4 = Button(window, text="Update", width=12, command=update_command)
btn4.grid(row=5, column=3)

btn5 = Button(window, text="Delete", width=12, command=delete_command)
btn5.grid(row=6, column=3)

btn6 = Button(window, text="Close", width=12, command=window.destroy)
btn6.grid(row=7, column=3)

window.mainloop()
