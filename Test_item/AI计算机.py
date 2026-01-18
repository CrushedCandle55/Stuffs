import tkinter as tk
import math


class Calculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculator")

        # 创建文本框
        self.text = tk.Entry(self.root, width=50, borderwidth=5)

        # 创建按钮
        self.button_1 = tk.Button(self.root, text="1", padx=40, pady=20, command=lambda: self.button_click(1))
        self.button_2 = tk.Button(self.root, text="2", padx=40, pady=20, command=lambda: self.button_click(2))
        self.button_3 = tk.Button(self.root, text="3", padx=40, pady=20, command=lambda: self.button_click(3))
        self.button_4 = tk.Button(self.root, text="4", padx=40, pady=20, command=lambda: self.button_click(4))
        self.button_5 = tk.Button(self.root, text="5", padx=40, pady=20, command=lambda: self.button_click(5))
        self.button_6 = tk.Button(self.root, text="6", padx=40, pady=20, command=lambda: self.button_click(6))
        self.button_7 = tk.Button(self.root, text="7", padx=40, pady=20, command=lambda: self.button_click(7))
        self.button_8 = tk.Button(self.root, text="8", padx=40, pady=20, command=lambda: self.button_click(8))
        self.button_9 = tk.Button(self.root, text="9", padx=40, pady=20, command=lambda: self.button_click(9))
        self.button_0 = tk.Button(self.root, text="0", padx=40, pady=20, command=lambda: self.button_click(0))
        self.button_add = tk.Button(self.root, text="+", padx=39, pady=20, command=self.addition)
        self.button_subtract = tk.Button(self.root, text="-", padx=41, pady=20, command=self.subtraction)
        self.button_multiply = tk.Button(self.root, text="*", padx=40, pady=20, command=self.multiplication)
        self.button_divide = tk.Button(self.root, text="/", padx=41, pady=20, command=self.division)
        self.button_clear = tk.Button(self.root, text="C", padx=40, pady=20, command=self.clear)
        self.button_equal = tk.Button(self.root, text="=", padx=91, pady=20, command=self.equal)
        self.button_sin = tk.Button(self.root, text="sin", padx=36, pady=20, command=self.sin)
        self.button_cos = tk.Button(self.root, text="cos", padx=36, pady=20, command=self.cos)
        self.button_tan = tk.Button(self.root, text="tan", padx=36, pady=20, command=self.tan)
        self.button_sqrt = tk.Button(self.root, text="sqrt", padx=30, pady=20, command=self.sqrt)
        self.button_power = tk.Button(self.root, text="x^2", padx=33, pady=20, command=self.power)

        # 将按钮放置在界面上
        self.text.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self.button_clear.grid(row=1, column=0)
        self.button_sin.grid(row=1, column=1)
        self.button_cos.grid(row=1, column=2)
        self.button_tan.grid(row=1, column=3)

        self.button_7.grid(row=2, column=0)
        self.button_8.grid(row=2, column=1)
        self.button_9.grid(row=2, column=2)
        self.button_divide.grid(row=2, column=3)

        self.button_4.grid(row=3, column=0)
        self.button_5.grid(row=3, column=1)
        self.button_6.grid(row=3, column=2)
        self.button_multiply.grid(row=3, column=3)

        self.button_1.grid(row=4, column=0)
        self.button_2.grid(row=4, column=1)
        self.button_3.grid(row=4, column=2)
        self.button_subtract.grid(row=4, column=3)

        self.button_0.grid(row=5, column=0)
        self.button_clear.grid(row=5, columnspan=2)
        self.button_add.grid(row=5, column=3)

        self.button_power.grid(row=6, columnspan=2)
        self.button_sqrt.grid(row=6, columnspan=2)

        self.button_equal.grid(row=7, columnspan=4)

    def button_click(self, number):
        current = str(self.text.get())
        current += str(number)
        self.text.delete(0, "end")
        self.text.insert(0, current)

    def addition(self):
        first_number = float(self.text.get())
        global f_num
        global math_operation
        math_operation = "addition"
        f_num = first_number
        self.text.delete(0, "end")

    def subtraction(self):
        first_number = float(self.text.get())
        global f_num
        global math_operation
        math_operation = "subtraction"
        f_num = first_number
        self.text.delete(0, "end")

    def multiplication(self):
        first_number = float(self.text.get())
        global f_num
        global math_operation
        math_operation = "multiplication"
        f_num = first_number
        self.text.delete(0, "end")

    def division(self):
        first_number = float(self.text.get())
        global f_num
        global math_operation
        math_operation = "division"
        f_num = first_number
        self.text.delete(0, "end")

    def clear(self):
        self.text.delete(0, "end")

    def equal(self):
        second_number = float(self.text.get())
        self.text.delete(0, "end")

        if math_operation == "addition":
            result = f_num + second_number
        elif math_operation == "subtraction":
            result = f_num - second_number
        elif math_operation == "multiplication":
            result = f_num * second_number
        elif math_operation == "division":
            result = f_num / second_number

        if result.is_integer():
            result = int(result)

        self.text.insert(0, result)

    def sin(self):
        value = float(self.text.get())
        result = math.sin(value)
        if result.is_integer():
            result = int(result)
        self.text.delete(0, "end")
        self.text.insert(0, result)

    def cos(self):
        value = float(self.text.get())
        result = math.cos(value)
        if result.is_integer():
            result = int(result)
        self.text.delete(0, "end")
        self.text.insert(0, result)

    def tan(self):
        value = float(self.text.get())
        result = math.tan(value)
        if result.is_integer():
            result = int(result)
        self.text.delete(0, "end")
        self.text.insert(0, result)

    def sqrt(self):
        value = float(self.text.get())
        result = math.sqrt(value)
        if result.is_integer():
            result = int(result)
        self.text.delete(0, "end")
        self.text.insert(0, result)

    def power(self):
        value = float(self.text.get())
        result = value ** 2
        if result.is_integer():
            result = int(result)
        self.text.delete(0, "end")
        self.text.insert(0, result)

    def run(self):
         self.root.mainloop()

calculator = Calculator()
calculator.run()