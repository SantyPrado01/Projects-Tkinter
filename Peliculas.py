from tkinter import *
cont = 2
def añadir_pelicula():
    global cont
    pelicula = pelicula_entry.get()
    peliculas = []
    peliculas.append(pelicula)
    for i in peliculas:
        peliculas_mostrar = Label(ventana, text=i)
        peliculas_mostrar.grid(column=1, row=cont)
        cont += 1

ventana = Tk()

ventana.title('Peliculas')

texto_entrada = Label(ventana, text='Escribe el titulo de la Pelicula:')
texto_entrada.grid(column=0, row=1)

pelicula_entry = Entry(ventana)
pelicula_entry.grid(column=0, row=2)

pelicula_boton = Button(ventana, text='Añadir', command=añadir_pelicula)
pelicula_boton.grid(column=0, row=3)

mostrar_peliculas = Label(ventana, text='Peliculas')
mostrar_peliculas.grid(column=1, row=1)


ventana.mainloop()