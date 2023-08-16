from tkinter import *

def calcular():
    try:
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

    except ValueError:
        ventana_emergente = Toplevel(ventana)
        ventana_emergente.title('Error')
        mensaje_error = Label(ventana_emergente, text='Tienes que ingresar un numero')
        mensaje_error.pack()   


ventana = Tk()
ventana.title('Calculadora con Radiobutton')
ventana.resizable(width=False, height=False)

texto_numero_uno = Label(ventana, text='Primer Numero', font=10)
texto_numero_uno.grid(column=0, row=0)

entry_numero_uno = Entry(ventana, font=10)
entry_numero_uno.grid(column=1, row=0,pady=8, ipady=8, padx=10, ipadx=10)

texto_numero_dos = Label(ventana, text='Segundo Numero', font=10)
texto_numero_dos.grid(column=0, row=1)

entry_numero_dos = Entry(ventana, font=10)
entry_numero_dos.grid(column=1, row=1,pady=8, ipady=8, padx=10, ipadx=10)

seleccion_operacion = StringVar()
seleccion_operacion.set("+")

radiobutton_suma = Radiobutton(ventana, text="+", variable=seleccion_operacion, value="+", font=10)
radiobutton_suma.grid(column=3, row=0)

radiobutton_resta = Radiobutton(ventana, text="-", variable=seleccion_operacion, value="-", font=10)
radiobutton_resta.grid(column=3, row=1)

radiobutton_multiplicacion = Radiobutton(ventana, text="x", variable=seleccion_operacion, value="*", font=10)
radiobutton_multiplicacion.grid(column=3, row=2)

radiobutton_division = Radiobutton(ventana, text="/", variable=seleccion_operacion, value="/", font=10)
radiobutton_division.grid(column=3, row=3)

radiobutton_potencia = Radiobutton(ventana, text="^", variable=seleccion_operacion, value="^", font=10)
radiobutton_potencia.grid(column=3, row=4)

boton_calcular = Button(ventana, text='Calcular', width=15,height=2, command=calcular)
boton_calcular.grid(column=0, row=3, rowspan=2, columnspan=2)

texto_resultado = Label(ventana, text='Resultado: ', font=10)
texto_resultado.grid(column=0, row=2)

resultado = Entry(ventana, state=DISABLED, font=10)
resultado.grid(column=1, row=2, pady=8, ipady=8, padx=10, ipadx=10)

ventana.mainloop()
