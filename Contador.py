from tkinter import *

def aumentar_contador():
    valor_actual = int(contador_numero.cget('text'))
    nuevo_valor = valor_actual + 1
    contador_numero.config(text=str(nuevo_valor))

def disminuir_contador():
    valor_actual = int(contador_numero.cget('text'))
    nuevo_valor = valor_actual - 1
    contador_numero.config(text=str(nuevo_valor))

def reset():
    contador_numero.config(text='0')

ventana = Tk()
ventana.title('Contador')

texto = Label(ventana, text='Contador')
texto.pack()

contador_numero = Label(ventana, text='0')
contador_numero.pack()

boton_aumentar = Button(ventana, text='Aumentar (+)', command=aumentar_contador)
boton_aumentar.pack()

boton_disminuir = Button(ventana, text='Disminuir (-)', command=disminuir_contador)
boton_disminuir.pack()

boton_reset = Button(ventana,text='Reset', command=reset)
boton_reset.pack()

ventana.mainloop()