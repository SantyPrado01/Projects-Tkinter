from tkinter import *

def aumentar_contador():
    valor_actual = int(contador_numero.cget('text'))
    nuevo_valor = valor_actual + 1
    contador_numero.config(text=str(nuevo_valor))

ventana = Tk()
ventana.title('Contador Creciente')

texto = Label(ventana, text='Contador')
texto.pack()

contador_numero = Label(ventana, text='80')
contador_numero.pack()

boton_aumentar = Button(ventana, text='Aumentar (+)', command=aumentar_contador)
boton_aumentar.pack()

ventana.mainloop()