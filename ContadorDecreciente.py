from tkinter import *

def disminuir_contador():
    valor_actual = int(contador_numero.cget('text'))
    nuevo_valor = valor_actual - 1
    contador_numero.config(text=str(nuevo_valor))

ventana = Tk()
ventana.title('Contador Decreciente')
ventana.resizable(width=False, height=False)

texto = Label(ventana, text='Contador', font=16)
texto.pack(pady=8, ipady=8, padx=10, ipadx=10)

contador_numero = Label(ventana, text='80', font=16)
contador_numero.pack(pady=8, ipady=8, padx=10, ipadx=10)

boton_disminuir = Button(ventana, text='Disminuir (-)', command=disminuir_contador, font=16)
boton_disminuir.pack(pady=8, ipady=8, padx=10, ipadx=10)

ventana.mainloop()