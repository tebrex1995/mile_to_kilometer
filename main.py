from tkinter import *

window = Tk()
window.title("Mile to kilometer")
window.minsize(width=100, height=100)
FONT = ("Arial", 16, "normal")


def calculate():
    km = int(entry.get()) * 1.609344
    calculation.config(text=str(km))


#Entry
entry = Entry(width=10)
entry.insert(END, "0")
entry.grid(row=1,column=2)

#Labels
first_label = Label(text="is equal to ",font=FONT)
first_label.grid(column=0,row=2)

miles_label = Label(text="Miles", font=FONT)
miles_label.grid(column=3,row=1)

km_label = Label(text="km",font=FONT)
km_label.grid(column=3,row=2)

calculation = Label(text=0,font=FONT)
calculation.grid(column=2,row=2)

# #Button
button = Button(text="Calculate", command=calculate)
button.grid(row=1,column=1)






window.mainloop()
