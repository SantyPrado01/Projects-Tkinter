from tkinter import *
cont = 2
def añadir_pelicula():
    global cont
    pelicula = pelicula_entry.get()
    peliculas = []
    peliculas.append(pelicula)
    for i in peliculas:
        peliculas_mostrar = Label(ventana, text=i, font=16)
        peliculas_mostrar.grid(column=1, row=cont,pady=8, ipady=8, padx=10, ipadx=10)
        cont += 1
    pelicula_entry.delete(0, END)
    
ventana = Tk()

ventana.title('Peliculas')
ventana.resizable(width=False, height=False)

texto_entrada = Label(ventana, text='Escribe el titulo de la Pelicula:', font=16)
texto_entrada.grid(column=0, row=1,pady=8, ipady=8, padx=10, ipadx=10)

pelicula_entry = Entry(ventana, font=16)
pelicula_entry.grid(column=0, row=2,pady=8, ipady=8, padx=10, ipadx=10)

pelicula_boton = Button(ventana, text='Añadir', command=añadir_pelicula, font=16)
pelicula_boton.grid(column=0, row=3,pady=8, ipady=8, padx=10, ipadx=10)

mostrar_peliculas = Label(ventana, text='Peliculas', font=16)
mostrar_peliculas.grid(column=1, row=1,pady=8, ipady=8, padx=10, ipadx=10)


ventana.mainloop()