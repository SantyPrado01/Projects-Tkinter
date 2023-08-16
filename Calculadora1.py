from tkinter import *


def sumar(a,b):
    cuenta = int(a) + int(b)
    resultado.config(state=NORMAL)
    resultado.insert(0,str(cuenta))
    resultado.config(state=DISABLED)

def restar(a,b):
    cuenta = a - b
    resultado.config(state=NORMAL)
    resultado.insert(0,str(cuenta))
    resultado.config(state=DISABLED)

    
def multiplicacion(a,b):
    cuenta = a * b
    resultado.config(state=NORMAL)
    resultado.insert(0,str(cuenta))
    resultado.config(state=DISABLED)


def division(a,b):
    cuenta = a / b
    resultado.config(state=NORMAL)
    resultado.insert(0,str(cuenta))
    resultado.config(state=DISABLED)


def potencia(a,b):
    cuenta = a ** b
    resultado.config(state=NORMAL)
    resultado.insert(0,str(cuenta))
    resultado.config(state=DISABLED)


def borrar():
    entry_numero_uno.delete(0, END)
    entry_numero_dos.delete(0, END)
    resultado.config(state=NORMAL)
    resultado.delete(0, END)
    resultado.config(state=DISABLED)

ventana = Tk()
ventana.title('Calculadora 1')

texto_numero_uno = Label(ventana, text='Primer Numero')
texto_numero_uno.grid(column=0, row=0)

entry_numero_uno = Entry(ventana)
entry_numero_uno.grid(column=1, row=0)

texto_numero_dos = Label(ventana, text='Segundo Numero')
texto_numero_dos.grid(column=0, row=1)

entry_numero_dos = Entry(ventana)
entry_numero_dos.grid(column=1, row=1)

texto_resultado = Label(ventana, text='Resultado: ')
texto_resultado.grid(column=0, row=2)

resultado = Entry(ventana, state=DISABLED)
resultado.grid(column=1, row=2)

boton_suma = Button(ventana, width=5,text='+', command=lambda:sumar(entry_numero_uno.get(),entry_numero_dos.get()))
boton_suma.grid(column=0, row=3)

boton_resta = Button(ventana, text='-', command=lambda:restar(entry_numero_uno.get(),entry_numero_dos.get()))
boton_resta.grid(column=1, row=3)

boton_multiplicacion = Button(ventana, text='x', command=lambda:multiplicacion(entry_numero_uno.get(),entry_numero_dos.get()))
boton_multiplicacion.grid(column=0, row=4)

boton_division = Button(ventana, text='/', command=lambda:division(entry_numero_uno.get(),entry_numero_dos.get()))
boton_division.grid(column=1, row=4)

boton_exponente = Button(ventana, text='^', command=lambda:potencia(entry_numero_uno.get(),entry_numero_dos.get()))
boton_exponente.grid(column=0, row=5)

boton_clear = Button(ventana, text='Borrar', command=borrar)
boton_clear.grid(column=1, row=5)

ventana.mainloop()