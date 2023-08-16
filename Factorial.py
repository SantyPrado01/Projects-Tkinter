from tkinter import *

contador = 0

def factorial():
    global contador
    try:
        numero_factorial = int(numero_entry.get())
        if contador < numero_factorial:
            contador += 1
            calculo = contador * numero_factorial
            texto_resultado_num = Label(ventana, text=calculo)
            texto_resultado_num.grid(column=3, row=1)
    except ValueError:
        ventana_emergente = Toplevel(ventana)
        ventana_emergente.title('Error')
        mensaje_error = Label(ventana_emergente, text='Tienes que ingresar un numero')
        mensaje_error.pack()
        
ventana = Tk()
ventana.title('Factorial')

texto_factorial = Label(
    ventana,
    text='''La función factorial se representa con un signo de exclamación “!” detrás de un número. 
    Esta exclamación quiere decir que hay que multiplicar todos los números enteros positivos que hay entre ese número y el 1.'''
    ,
    justify=CENTER     
)
texto_factorial.grid(column=0, row=0, columnspan=4)

texto = Label(ventana, text='Factorial de: ')
texto.grid(column=0, row=1)

numero_entry = Entry(ventana)
numero_entry.grid(column=1, row=1)

texto_resultado = Label(ventana, text='Resultado')
texto_resultado.grid(column=2, row=1)

boton = Button(ventana, text='Siguiente', command=factorial)
boton.grid(column=4, row=1)

ventana.mainloop()