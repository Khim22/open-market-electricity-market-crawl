from tkinter import *
import tkinter.ttk as TTK
import constants

FONT = ('Arial', 12)

def create_title_frame(root):
    titleFrame = Frame(root)
    titleFrame.grid(column=0, row=0, padx=20, pady=20)
    titleFrame.columnconfigure(0, weight=1)
    titleFrame.rowconfigure(0, weight=1)
    return titleFrame

def create_row_frame(container_frame, row_num, label_text):
    rowFrame = Frame(container_frame)
    rowFrame.grid(column=0, row=row_num, padx=10, pady=10)
    label = Label(rowFrame, text=label_text, font=FONT, anchor="w")
    label.grid(row=0, column=0)
    return rowFrame


def create_option_menu_row(label_text, list, row_num, container_frame):
    rowFrame = create_row_frame(container_frame,row_num, label_text)
    variable = StringVar(rowFrame)
    variable.set(list[0]) # default value

    menuwidth = len(max(list, key=len))
    w = OptionMenu(rowFrame, variable, *list)

    w.config(width = menuwidth)
    w.grid(row=0, column=1, columnspan=2)

def create_input_row(label_text, row_num, container_frame):
    rowFrame = create_row_frame(container_frame,row_num, label_text)

    input_field = Entry(rowFrame, bd=2, textvariable= IntVar())
    input_field.grid(row=0, column=1, columnspan=2)
    return input_field

def create_list_box_row(label_text, list, row_num, container_frame):
    rowFrame = create_row_frame(container_frame,row_num, label_text)
    listbox = Listbox(rowFrame, selectmode=MULTIPLE, height=5, width=len(max(list, key=len)))
    listbox.insert(0, *list)
    listbox.grid(row=0, column=1)
    scrollbar = Scrollbar(rowFrame, orient="vertical")
    scrollbar.config(command=listbox.yview)
    scrollbar.grid(row=0, column=2)
    listbox.config(yscrollcommand=scrollbar.set)
    return listbox

def submit(control, label):
    value = control.get()
    label.config(text=value)
    # print(g)


root = Tk()
root.title('Open Market Electricity Crawl')
root.geometry('650x550')

titleFrame = create_title_frame(root)

title = Label(titleFrame, text='Open Market Electricity Crawl', font=('Arial Bold', 30))
title.grid(row=1, column=0, columnspan=3, padx=20, pady=20)

create_option_menu_row("Consumer Type", constants.consumer_types, 3, titleFrame)
create_option_menu_row("Housing Type", constants.housing_types, 4, titleFrame)
create_list_box_row("Price Plan Type", constants.price_plan_types, 5, titleFrame)
create_list_box_row("Retailer", constants.retailers, 6, titleFrame)
monthly_consumption_field = create_input_row("Average Monthly Consumption(kWh)", 7, titleFrame)


startButton = Button(titleFrame, text='Submit', command=lambda: submit(monthly_consumption_field, label))
startButton.grid(row=8, columnspan=3)


### Label For Testing retrieving values
rowFrame = Frame(titleFrame)
rowFrame.grid(column=0, row=9, padx=10, pady=10)
label = Label(rowFrame, text=0, font=FONT, anchor="w")
label.grid(row=0, column=0)

root.mainloop()

