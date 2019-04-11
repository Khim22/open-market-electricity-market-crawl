from tkinter import *


FONT = ('Arial', 12)

root = Tk()
#root.withdraw()
root.title('Open Market Electricity Crawl')
root.geometry('650x350')

def create_option_menu_row(label_text, list, row_num, container_frame):
    rowFrame = Frame(container_frame)
    rowFrame.grid(column=0, row=row_num, padx=10, pady=10)
    label = Label(rowFrame, text=label_text, font=FONT, anchor="w")
    label.grid(row=0, column=0)

    variable = StringVar(rowFrame)
    variable.set(list[0]) # default value

    menuwidth = len(max(list, key=len))
    w = OptionMenu(rowFrame, variable, *list)

    w.config(width = menuwidth)
    w.grid(row=0, column=1, columnspan=2)

titleFrame = Frame(root)
titleFrame.grid(column=0, row=0, padx=20, pady=20)
titleFrame.columnconfigure(0, weight=1)
titleFrame.rowconfigure(0, weight=1)

title = Label(titleFrame, text='Open Market Electricity Crawl', font=('Arial Bold', 30))
title.grid(row=1, column=0, columnspan=3, padx=20, pady=20)

rowFrame = Frame(titleFrame)
rowFrame.grid(column=0, row=2, padx=20, pady=20)
consumerTypeLabel = Label(rowFrame, text='Consumer Type', font=FONT, anchor="w")
consumerTypeLabel.grid(row=2, column=0)

variable = StringVar(rowFrame)
options =["one", "two", "three", "ninetynine"]
variable.set(options[0]) # default value

menuwidth = len(max(options, key=len))
w = OptionMenu(rowFrame, variable, *options)

w.config(width = menuwidth)
w.grid(row=2, column=1, columnspan=2)
# btn = Button(root, text='Crawl!')
# label.pack(fill='x')
housing_types =  ["HDB 1-Room", "HDB 2-Room", "HDB 3-Room", "HDB 4-Room", "HDB 5-Room", "HDB Executive", "Apartment", "Terrace", "Semi-Detached", "Bungalow" ]
create_option_menu_row("Housing Type", housing_types, 3, titleFrame)
root.mainloop()

