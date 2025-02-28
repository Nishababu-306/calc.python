from tkinter import *

root = Tk()
e = Entry(root, width=50, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

f_num = None
operation = None

def button_operations(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    global f_num
    global operation
    f_num = float(e.get())
    operation = "+"
    e.delete(0, END)

def button_sub():
    global f_num
    global operation
    f_num = float(e.get())
    operation = "-"
    e.delete(0, END)

def button_multiply():
    global f_num
    global operation
    f_num = float(e.get())
    operation = "*"
    e.delete(0, END)

def button_division():
    global f_num
    global operation
    f_num = float(e.get())
    operation = "/"
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)
    
    if operation == "+":
        result = f_num + float(second_number)
    elif operation == "-":
        result = f_num - float(second_number)
    elif operation == "*":
        result = f_num * float(second_number)
    elif operation == "/":
        if float(second_number) != 0:
            result = f_num / float(second_number)
        else:
            result = "Error: Division by zero"
    else:
        result = "Error: Invalid operation"
    
    e.insert(0, result)

button_1 = Button(root, text="1", padx=40, pady=30, command=lambda: button_operations(1))
button_2 = Button(root, text="2", padx=40, pady=30, command=lambda: button_operations(2))
button_3 = Button(root, text="3", padx=40, pady=30, command=lambda: button_operations(3))
button_4 = Button(root, text="4", padx=40, pady=30, command=lambda: button_operations(4))
button_5 = Button(root, text="5", padx=40, pady=30, command=lambda: button_operations(5))
button_6 = Button(root, text="6", padx=40, pady=30, command=lambda: button_operations(6))
button_7 = Button(root, text="7", padx=40, pady=30, command=lambda: button_operations(7))
button_8 = Button(root, text="8", padx=40, pady=30, command=lambda: button_operations(8))
button_9 = Button(root, text="9", padx=40, pady=30, command=lambda: button_operations(9))
button_0 = Button(root, text="0", padx=40, pady=30, command=lambda: button_operations(0))

button_clear = Button(root, text="Clear", padx=40, pady=30, command=button_clear)
button_eq = Button(root, text="=", padx=40, pady=30, command=button_equal)
button_plus = Button(root, text="+", padx=40, pady=30, command=button_add)
button_minus = Button(root, text="-", padx=40, pady=30, command=button_sub)
button_mult = Button(root, text="*", padx=40, pady=30, command=button_multiply)
button_div = Button(root, text="/", padx=40, pady=30, command=button_division)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1)
button_eq.grid(row=4, column=2)
button_plus.grid(row=1, column=3)
button_minus.grid(row=2, column=3)
button_mult.grid(row=3, column=3)
button_div.grid(row=4, column=3)

root.mainloop()
