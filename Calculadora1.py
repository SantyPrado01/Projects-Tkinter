from tkinter import *


def sumar(a,b):
    try:
        cuenta = int(a) + int(b)
        resultado.config(state=NORMAL)
        resultado.insert(0,str(cuenta))
        resultado.config(state=DISABLED)
    except ValueError:
        ventana_emergente = Toplevel(ventana)
        ventana_emergente.title('Error')
        mensaje_error = Label(ventana_emergente, text='Tienes que ingresar un numero')
        mensaje_error.pack()

def restar(a,b):
    try:
        cuenta = int(a) - int(b)
        resultado.config(state=NORMAL)
        resultado.insert(0,str(cuenta))
        resultado.config(state=DISABLED)
    except ValueError:
        ventana_emergente = Toplevel(ventana)
        ventana_emergente.title('Error')
        mensaje_error = Label(ventana_emergente, text='Tienes que ingresar un numero')
        mensaje_error.pack()

    
def multiplicacion(a,b):
    try:
        cuenta = int(a) * int(b)
        resultado.config(state=NORMAL)
        resultado.insert(0,str(cuenta))
        resultado.config(state=DISABLED)
    except ValueError:
        ventana_emergente = Toplevel(ventana)
        ventana_emergente.title('Error')
        mensaje_error = Label(ventana_emergente, text='Tienes que ingresar un numero')
        mensaje_error.pack()

def division(a,b):
    try:
        cuenta = int(a) / int(b)
        resultado.config(state=NORMAL)
        resultado.insert(0,str(cuenta))
        resultado.config(state=DISABLED)
    except ValueError:
        ventana_emergente = Toplevel(ventana)
        ventana_emergente.title('Error')
        mensaje_error = Label(ventana_emergente, text='Tienes que ingresar un numero')
        mensaje_error.pack()


def potencia(a,b):
    try:
        cuenta = int(a) ** int(b)
        resultado.config(state=NORMAL)
        resultado.insert(0,str(cuenta))
        resultado.config(state=DISABLED)
    except ValueError:
        ventana_emergente = Toplevel(ventana)
        ventana_emergente.title('Error')
        mensaje_error = Label(ventana_emergente, text='Tienes que ingresar un numero')
        mensaje_error.pack()


def borrar():
    entry_numero_uno.delete(0, END)
    entry_numero_dos.delete(0, END)
    resultado.config(state=NORMAL)
    resultado.delete(0, END)
    resultado.config(state=DISABLED)

ventana = Tk()
ventana.title('Calculadora 1')
ventana.resizable(width=False, height=False)

texto_numero_uno = Label(ventana, text='Primer Numero', font=10)
texto_numero_uno.grid(column=0, row=0)

entry_numero_uno = Entry(ventana, font=10, width=10)
entry_numero_uno.grid(column=1, row=0, pady=8, ipady=8, padx=10, ipadx=10)

texto_numero_dos = Label(ventana, text='Segundo Numero', font=10)
texto_numero_dos.grid(column=0, row=1)

entry_numero_dos = Entry(ventana, font=10, width=10)
entry_numero_dos.grid(column=1, row=1,pady=8, ipady=8, padx=10, ipadx=10)

texto_resultado = Label(ventana, text='Resultado: ', font=10)
texto_resultado.grid(column=0, row=2)

resultado = Entry(ventana, state=DISABLED, font=10, width=10)
resultado.grid(column=1, row=2,pady=8, ipady=8, padx=10, ipadx=10)

boton_suma = Button(ventana, width=12, height=3 ,text='+', font=16,command=lambda:sumar(entry_numero_uno.get(),entry_numero_dos.get()))
boton_suma.grid(column=0, row=3)

boton_resta = Button(ventana, width=12, height=3 ,text='-',font=16, command=lambda:restar(entry_numero_uno.get(),entry_numero_dos.get()))
boton_resta.grid(column=1, row=3)

boton_multiplicacion = Button(ventana, width=12, height=3 ,text='x', font=16,command=lambda:multiplicacion(entry_numero_uno.get(),entry_numero_dos.get()))
boton_multiplicacion.grid(column=0, row=4)

boton_division = Button(ventana, width=12, height=3 ,text='/',font=16, command=lambda:division(entry_numero_uno.get(),entry_numero_dos.get()))
boton_division.grid(column=1, row=4)

boton_exponente = Button(ventana, width=12, height=3 ,text='^',font=16, command=lambda:potencia(entry_numero_uno.get(),entry_numero_dos.get()))
boton_exponente.grid(column=0, row=5)

boton_clear = Button(ventana, width=12, height=3 ,text='Borrar',font=16, command=borrar)
boton_clear.grid(column=1, row=5)

ventana.mainloop()