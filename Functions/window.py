from Functions.functions import *


# Row One
button_7 = tk.Button(command = lambda: edit_numbers("7"), text="7", font=("Times New Roman", 30), width=4)  # Lambda with no params used to prevent calling of function with argument
button_7.grid(column=0, row=2)

button_8 = tk.Button(command = lambda: edit_numbers("8"), text="8", font=("Times New Roman", 30), width=4)
button_8.grid(column=1, row=2)

button_9 = tk.Button(command = lambda: edit_numbers("9"),text="9", font=("Times New Roman", 30), width=4)
button_9.grid(column=2, row=2)

button_div = tk.Button(command = lambda: add_signe("/"), text="/", font=("Times New Roman", 30), width=4)
button_div.grid(column=3, row=2)


# Row Two
button_4 = tk.Button(command = lambda: edit_numbers("4"),text="4", font=("Times New Roman", 30), width=4)
button_4.grid(column=0, row=3)

button_5 = tk.Button(command = lambda: edit_numbers("5"),text="5", font=("Times New Roman", 30), width=4)
button_5.grid(column=1, row=3)

button_6 = tk.Button(command = lambda: edit_numbers("6"),text="6", font=("Times New Roman", 30), width=4)
button_6.grid(column=2, row=3)

button_mul = tk.Button(command = lambda: add_signe("x"), text="x", font=("Times New Roman", 30), width=4)
button_mul.grid(column=3, row=3)


# Row Three
button_1 = tk.Button(command = lambda: edit_numbers("1"),text="1", font=("Times New Roman", 30), width=4)
button_1.grid(column=0, row=4)

button_2 = tk.Button(command = lambda: edit_numbers("2"),text="2", font=("Times New Roman", 30), width=4)
button_2.grid(column=1, row=4)

button_3 = tk.Button(command = lambda: edit_numbers("3"),text="3", font=("Times New Roman", 30), width=4)
button_3.grid(column=2, row=4)

button_sub = tk.Button(command = lambda: add_signe("-"), text="-", font=("Times New Roman", 30), width=4)
button_sub.grid(column=3, row=4)


# Row Four
button_0 = tk.Button(command = lambda: edit_numbers("0"),text="0", font=("Times New Roman", 30), width=4)
button_0.grid(column=0, row=5)

button_dot = tk.Button(command = lambda: edit_numbers("."), text=".", font=("Times New Roman", 30), width=4)
button_dot.grid(column=1, row=5)

button_log = tk.Button(command = lambda: add_signe("log"), text="log", font=("Times New Roman", 30), width=4)
button_log.grid(column=2, row=5)

button_add = tk.Button(command = lambda: add_signe("+"), text="+", font=("Times New Roman", 30), width=4)
button_add.grid(column=3, row=5)


# Row Five
button_sine = tk.Button(command= lambda: add_signe("sin"), text="sin", font=("Times New Roman", 30), width=4)
button_sine.grid(column=0, row=6)

button_cosine = tk.Button(command= lambda: add_signe("cos"), text="cos", font=("Times New Roman", 30), width=4)
button_cosine.grid(column=1, row=6)

button_tangent = tk.Button(command= lambda: add_signe("tan"), text="tan", font=("Times New Roman", 30), width=4)
button_tangent.grid(column=2, row=6)

button_equal = tk.Button(command= calculate, text="=", font=("Times New Roman", 30), width=4)
button_equal.grid(column=3, row=6)


# Row Five
button_radian = tk.Button(command = lambda: add_signe("rad"), text = "rad", font = ("Times New Roman", 30), width = 4)
button_radian.grid(column = 0, row = 7)

button_exponential = tk.Button(command = lambda: add_signe("e"), text = "e", font = ("Times New Roman", 30), width = 4)
button_exponential.grid(column = 1, row = 7)

button_pi = tk.Button(command = lambda: add_signe(" π"), text = " π", font = ("Times New Roman", 30), width = 4)
button_pi.grid(column = 2, row = 7)

button_delete = tk.Button(command = lambda: delete(), text = "Del", font = ("Times New Roman", 30), width = 4)
button_delete.grid(column = 3, row = 7)
