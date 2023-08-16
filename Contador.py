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
ventana.resizable(width=False, height=False)

texto = Label(ventana, text='Contador', font=12)
texto.grid(column=0,row=0, pady=8, ipady=8, padx=10, ipadx=10, columnspan=2)

contador_numero = Label(ventana, text='0', font=12)
contador_numero.grid(column=0, row=1, pady=8, ipady=8, padx=10, ipadx=10, columnspan=2)

boton_aumentar = Button(ventana, text='Aumentar (+)', font=12,command=aumentar_contador)
boton_aumentar.grid(column=0, row=2, pady=8, ipady=8, padx=10, ipadx=10)

boton_disminuir = Button(ventana, text='Disminuir (-)',font=12, command=disminuir_contador)
boton_disminuir.grid(column=1, row=2,pady=8, ipady=8, padx=10, ipadx=10)

boton_reset = Button(ventana,text='Reset', command=reset, font=12)
boton_reset.grid(column=0, row=3, pady=8, ipady=8, padx=10, ipadx=10, columnspan=2)

ventana.mainloop()