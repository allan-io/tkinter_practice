from tkinter import *
window = Tk()
window.title("Mile to Km converter")
window.minsize(width=200, height=200)
window.config(padx=50, pady=50)

def calculate(event=""):
    miles = float(usr_input.get())
    km = miles * 1.609
    output.config(text=f"{km:.2f}")

label_1 = Label(text="Miles", font=("Arial", 24))
label_1.grid(column=2, row=0)
# my_label["text"] = "New Text"
label_2 = Label(text="is equal to", font=("Arial", 24))
label_2.grid(column=0, row=1)

label_3 = Label(text="Km", font=("Arial", 24))
label_3.grid(column=2, row=1)

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

output = Label(text="0", font=("Arial", 24))
output.grid(column=1, row=1)

usr_input = Entry(width=10, )
usr_input.grid(column=1, row=0)

#

#
# button = Button(text="click me", command=button_clicked)
# button.grid(column=1, row=1)
#
# new_button = Button(text="New Button")
# new_button.grid(column=2, row=0)




window.bind("<Return>", calculate)

window.mainloop()
