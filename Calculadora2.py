from tkinter import *

def calcular():
    a = int(entry_numero_uno.get())
    b = int(entry_numero_dos.get())
    operacion = seleccion_operacion.get()

    if operacion == "+":
        cuenta = a + b
    elif operacion == "-":
        cuenta = a - b
    elif operacion == "*":
        cuenta = a * b
    elif operacion == "/":
        cuenta = a / b
    elif operacion == "^":
        cuenta = a ** b

    resultado.config(state=NORMAL)
    resultado.delete(0, END)
    resultado.insert(0, str(cuenta))
    resultado.config(state=DISABLED)

ventana = Tk()
ventana.title('Calculadora con Radiobutton')

texto_numero_uno = Label(ventana, text='Primer Numero')
texto_numero_uno.grid(column=0, row=0)

entry_numero_uno = Entry(ventana)
entry_numero_uno.grid(column=1, row=0)

texto_numero_dos = Label(ventana, text='Segundo Numero')
texto_numero_dos.grid(column=0, row=1)

entry_numero_dos = Entry(ventana)
entry_numero_dos.grid(column=1, row=1)

seleccion_operacion = StringVar()
seleccion_operacion.set("+")

radiobutton_suma = Radiobutton(ventana, text="+", variable=seleccion_operacion, value="+")
radiobutton_suma.grid(column=0, row=2)

radiobutton_resta = Radiobutton(ventana, text="-", variable=seleccion_operacion, value="-")
radiobutton_resta.grid(column=1, row=2)

radiobutton_multiplicacion = Radiobutton(ventana, text="x", variable=seleccion_operacion, value="*")
radiobutton_multiplicacion.grid(column=0, row=3)

radiobutton_division = Radiobutton(ventana, text="/", variable=seleccion_operacion, value="/")
radiobutton_division.grid(column=1, row=3)

radiobutton_potencia = Radiobutton(ventana, text="^", variable=seleccion_operacion, value="^")
radiobutton_potencia.grid(column=0, row=4)

boton_calcular = Button(ventana, text='Calcular', width=10, command=calcular)
boton_calcular.grid(column=1, row=4)

texto_resultado = Label(ventana, text='Resultado: ')
texto_resultado.grid(column=0, row=5)

resultado = Entry(ventana, state=DISABLED)
resultado.grid(column=1, row=5)

ventana.mainloop()
