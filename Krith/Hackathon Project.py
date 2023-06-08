import tkinter

root = tkinter.Tk()

x = tkinter.StringVar()
y = tkinter.StringVar()
operation = ""

def add_value(num):
    global x, y, operation
    if operation == "":
        x.set(x.get() + str(num))
    else:
        y.set(y.get() + str(num))

def set_operation(op):
    global operation
    operation = op

def clear_values():
    global x, y, operation
    x.set("")
    y.set("")
    operation = ""

def perform_operation():
    t = int(x.get())
    u = int(y.get())
    
    if operation == "add" or operation == "+":
        result = t + u
        label_text = "The sum of numbers is: " + str(result)
        
    elif operation == "sub" or operation == "-":
        result = t - u
        label_text = "The difference of numbers is: " + str(result)
        
    elif operation == "mult" or operation == "*":
        result = t * u
        label_text = "The product of numbers is: " + str(result)
        
    elif operation == "div" or operation == "/":
        result = t / u
        label_text = "The quotient of numbers is: " + str(result)
        
    elif operation == "rem" or operation == "%":
        result = t % u
        label_text = "The remainder is: " + str(result)
        
    else:
        label_text = "Invalid operation"
    
    label2 = tkinter.Label(root, text="Do you wish to continue? Enter numbers in the text space")
    label2.pack()
    label.config(text=label_text)

x_label = tkinter.Label(root, text="X:")
x_label.pack()

x_entry = tkinter.Entry(root, textvariable=x)
x_entry.pack()

button_frame = tkinter.Frame(root)
button_frame.pack()

for i in range(10):
    button = tkinter.Button(button_frame, text=str(i), command=lambda num=i: add_value(num))
    button.grid(row=i//3, column=i%3, padx=5, pady=5)

y_label = tkinter.Label(root, text="Y:")
y_label.pack()

y_entry = tkinter.Entry(root, textvariable=y)
y_entry.pack()

operation_label = tkinter.Label(root, text="Operation:")
operation_label.pack()

operation_buttons_frame = tkinter.Frame(root)
operation_buttons_frame.pack()

operations = ["add", "sub", "mult", "div", "rem"]

for op in operations:
    button = tkinter.Button(operation_buttons_frame, text=op, command=lambda op=op: set_operation(op))
    button.pack(side=tkinter.LEFT, padx=5)

clear_button = tkinter.Button(root, text="Clear", command=clear_values)
clear_button.pack()

calculate_button = tkinter.Button(root, text="Calculate", command=perform_operation)
calculate_button.pack()

label = tkinter.Label(root, text="The sum of numbers are: ")
label.pack()

root.mainloop()
