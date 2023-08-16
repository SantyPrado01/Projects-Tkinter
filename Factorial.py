from tkinter import *

contador = 0

def factorial():
    global contador
    try:
        numero_factorial = int(numero_entry.get())
        if contador < numero_factorial:
            contador += 1
            calculo = contador * numero_factorial
            texto_resultado_num = Label(ventana, text=calculo, font=12)
            texto_resultado_num.grid(column=1, row=2,pady=8, ipady=8, padx=10, ipadx=10)
    except ValueError:
        ventana_emergente = Toplevel(ventana)
        ventana_emergente.title('Error')
        mensaje_error = Label(ventana_emergente, text='Tienes que ingresar un numero')
        mensaje_error.pack()
        
ventana = Tk()
ventana.title('Factorial')
ventana.resizable(width=False, height=False)

texto_factorial = Label(
    ventana,
    text='''La función factorial se representa con un signo de exclamación “!” detrás de un número. 
    Esta exclamación quiere decir que hay que multiplicar 
    todos los números enteros positivos que hay entre ese número y el 1.'''
    ,
    justify=CENTER, font=12     
)
texto_factorial.grid(column=0, row=0, columnspan=4,pady=8, ipady=8, padx=10, ipadx=10)

texto = Label(ventana, text='Factorial de: ', font=12)
texto.grid(column=0, row=1,pady=8, ipady=8, padx=10, ipadx=10)

numero_entry = Entry(ventana, font=12)
numero_entry.grid(column=1, row=1,pady=8, ipady=8, padx=10, ipadx=10)

texto_resultado = Label(ventana, text='Resultado', font=12)
texto_resultado.grid(column=0, row=2,pady=8, ipady=8, padx=10, ipadx=10)

boton = Button(ventana, text='Siguiente', command=factorial, font=12)
boton.grid(column=0, row=3,pady=8, ipady=8, padx=10, ipadx=10)

ventana.mainloop()