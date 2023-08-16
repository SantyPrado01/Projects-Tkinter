from tkinter import *

def disminuir_contador():
    valor_actual = int(contador_numero.cget('text'))
    nuevo_valor = valor_actual - 1
    contador_numero.config(text=str(nuevo_valor))

ventana = Tk()
ventana.title('Contador Decreciente')

texto = Label(ventana, text='Contador')
texto.pack()

contador_numero = Label(ventana, text='80')
contador_numero.pack()

boton_disminuir = Button(ventana, text='Disminuir (-)', command=disminuir_contador)
boton_disminuir.pack()

ventana.mainloop()