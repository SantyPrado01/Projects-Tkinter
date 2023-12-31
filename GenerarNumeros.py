from tkinter import *
import random

def generar_numero():
    numero_uno=numero_seleccionado_uno.get()
    numero_dos=numero_seleccionado_dos.get()
    numero_aleatorio = random.randint(numero_uno, numero_dos)
    resultado = Label(ventana, text=numero_aleatorio)
    resultado.grid(column=1, row=3)

ventana = Tk()
ventana.title('Generar Numeros')
ventana.resizable(width=False, height=False)

numeros_inicio = 1
numeros_fin = 20

numeros_lista = list(range(numeros_inicio, numeros_fin + 1))

numero_seleccionado_uno = IntVar()
numero_seleccionado_uno.set(numeros_lista[0])

numero_seleccionado_dos = IntVar()
numero_seleccionado_dos.set(numeros_lista[0])

texto_numeros = Label(ventana, text='Elige dos numeros y se generara un numero al azar entre ellos.', font=12)
texto_numeros.grid(column=0, row=0, columnspan=2,pady=8, ipady=8, padx=10, ipadx=10)

texto_numero_uno = Label(ventana, text='Elige el numero 1', font=12)
texto_numero_uno.grid(column=0, row=1,pady=8, ipady=8, padx=10, ipadx=10)

numeros_desplegable_uno = OptionMenu(ventana, numero_seleccionado_uno, *numeros_lista)
numeros_desplegable_uno.grid(column=1, row=1,pady=8, ipady=8, padx=10, ipadx=10)

texto_numero_dos = Label(ventana, text='Elige el numero 2', font=12)
texto_numero_dos.grid(column=0, row=2,pady=8, ipady=8, padx=10, ipadx=10)

numeros_desplegable_dos = OptionMenu(ventana, numero_seleccionado_dos, *numeros_lista)
numeros_desplegable_dos.grid(column=1, row=2,pady=8, ipady=8, padx=10, ipadx=10)

texto_numero_generado = Label(ventana, text='Numero generado: ', font=12)
texto_numero_generado.grid(column=0, row=3,pady=8, ipady=8, padx=10, ipadx=10)

boton_generar = Button(ventana, text='Generar Numero', command=generar_numero, font=12)
boton_generar.grid(column=0, row=4, columnspan=2,pady=8, ipady=8, padx=10, ipadx=10)

ventana.mainloop()