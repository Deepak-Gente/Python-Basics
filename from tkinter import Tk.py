
from tkinter import Tk, Button

def fun():
    print("Button Clicked")
    return

root = Tk()
root.geometry("500x300")
root.title("GUI")

b = Button(root, text="Click me", command=fun)
b.pack()  # This line places the button on the window

root.mainloop()  # This starts the GUI event loop



#########################################################################


from tkinter import Tk, Button, Label, Entry

def fun():
    name = e1.get()
    age = e2.get()
    print(f"{name} is {age} years old")
    return

root = Tk()
root.title("GUI")

l1 = Label(root, text="Enter Name :", font="Candara 20")
l1.grid(row=0, column=0)

e1 = Entry(root, font="Candara 20")
e1.grid(row=0, column=1)

l2 = Label(root, text="Enter Age :", font="Candara 20")
l2.grid(row=1, column=0)

e2 = Entry(root, font="Candara 20")
e2.grid(row=1, column=1)

b1 = Button(root, text="Details", command=fun, font="Candara 15")
b1.grid(row=2, column=0)

b2 = Button(root, text="Exit", command=quit, font="Candara 15")
b2.grid(row=2, column=1)

root.mainloop()


from tkinter import Tk, Button, Label, Entry

root = Tk()
root.title("Calculator")
root.geometry("500x400")

l= Label(root, text="Calculator", font="Candara 20")
l.place(x=200, y=2)

l1 = Label(root, text="Enter First Num :", font="Candara 20")
l1.place(x=10, y=50)

e1 = Entry(root, font="Candara 20",width=10)
e1.place(x=250,y=50)

l2 = Label(root, text="Enter Second Num :", font="Candara 20")
l2.place(x=10, y=150)

e2 = Entry(root, font="Candara 20",width=10)
e2.place(x=250,y=150)

l3 = Label(root, text="Result :", font="Candara 20")
l3.place(x=10, y=250)

e3 = Entry(root, font="Candara 20",width=10)
e3.place(x=250,y=250)

b1=Button(root, text="add", width=10)
b1.place(x=10,y=350)

root.mainloop()
