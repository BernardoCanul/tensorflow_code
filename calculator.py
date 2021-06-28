from tkinter import *

root = Tk()
root.title("Calculadora basica")
root.resizable(0, 0)


# ---------- FUNCTIONS ----------
def button_click(number):
    text_display = display.get()
    new_text_display = text_display + str(number)
    if number == "=":
        try:
            resultado = eval(text_display)
            display.delete(0, END)
            display.insert(0, resultado)
        except:
            mensaje_error = "Ha ocurrido un error, verificar la entrada"
            display.delete(0, END)
            display.insert(0, mensaje_error)
    else:
        display.delete(0, END)
        display.insert(0, new_text_display)


def button_clear():
    display.delete(0, END)


# ---------- CREATE WIDGETS ----------
display = Entry(root, width=50, borderwidth=10)

PADDING_X = 35
PADDING_Y = 25

btn_1 = Button(root, text="1", padx=PADDING_X, pady=PADDING_Y, command=lambda: button_click(1))
btn_2 = Button(root, text="2", padx=PADDING_X, pady=PADDING_Y, command=lambda: button_click(2))
btn_3 = Button(root, text="3", padx=PADDING_X, pady=PADDING_Y, command=lambda: button_click(3))
btn_4 = Button(root, text="4", padx=PADDING_X, pady=PADDING_Y, command=lambda: button_click(4))
btn_5 = Button(root, text="5", padx=PADDING_X, pady=PADDING_Y, command=lambda: button_click(5))
btn_6 = Button(root, text="6", padx=PADDING_X, pady=PADDING_Y, command=lambda: button_click(6))
btn_7 = Button(root, text="7", padx=PADDING_X, pady=PADDING_Y, command=lambda: button_click(7))
btn_8 = Button(root, text="8", padx=PADDING_X, pady=PADDING_Y, command=lambda: button_click(8))
btn_9 = Button(root, text="9", padx=PADDING_X, pady=PADDING_Y, command=lambda: button_click(9))
btn_0 = Button(root, text="0", padx=PADDING_X, pady=PADDING_Y, command=lambda: button_click(0))
btn_add = Button(root, text="+", padx=PADDING_X, pady=PADDING_Y, command=lambda: button_click("+"))
btn_substract = Button(root, text="-", padx=PADDING_X, pady=PADDING_Y, command=lambda: button_click("-"))
btn_multiply = Button(root, text="x", padx=PADDING_X, pady=PADDING_Y, command=lambda: button_click("*"))
btn_divide = Button(root, text="/", padx=PADDING_X, pady=PADDING_Y, command=lambda: button_click("/"))
btn_equal = Button(root, text="=", padx=PADDING_X, pady=PADDING_Y, command=lambda: button_click("="))
btn_parentesis_1 = Button(root, text="(", padx=(PADDING_X + 46), pady=PADDING_Y, command=lambda: button_click("("))
btn_parentesis_2 = Button(root, text=")", padx=(PADDING_X + 46), pady=PADDING_Y, command=lambda: button_click(")"))
btn_clear = Button(root, text="C", padx=PADDING_X, pady=PADDING_Y, command=button_clear)

# ---------- PLACE WIDGETS ----------
display.grid(row=0, column=0, columnspan=4, padx=5, pady=10)

btn_1.grid(row=3, column=0)
btn_2.grid(row=3, column=1)
btn_3.grid(row=3, column=2)
btn_add.grid(row=3, column=3)

btn_4.grid(row=2, column=0)
btn_5.grid(row=2, column=1)
btn_6.grid(row=2, column=2)
btn_substract.grid(row=2, column=3)

btn_7.grid(row=1, column=0)
btn_8.grid(row=1, column=1)
btn_9.grid(row=1, column=2)
btn_multiply.grid(row=1, column=3)

btn_divide.grid(row=4, column=0)
btn_0.grid(row=4, column=1)
btn_equal.grid(row=4, column=2)
btn_clear.grid(row=4, column=3)

btn_parentesis_1.grid(row=5, column=0, columnspan=2)
btn_parentesis_2.grid(row=5, column=2, columnspan=2)

root.mainloop()
