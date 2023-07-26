import tkinter as tk
import datetime

# Función para guardar la información del personal
def guardar_informacion():
    nombre = entry_nombre.get()
    apellido_1 = entry_apellido_1.get()
    apellido_2 = entry_apellido_2.get()
    puesto = entry_puesto.get()

    # Obtener la fecha y hora actual
    fecha_hora = datetime.datetime.now()

    # Crear una cadena con los datos y la fecha y hora
    datos_guardados = f"Nombre: {nombre}\nApellido 1: {apellido_1}\nApellido 2: {apellido_2}\nPuesto: {puesto}\nFecha y Hora: {fecha_hora}\n\n"

    # Guardar los datos en un archivo de texto
    with open("datos_personal.txt", "a") as archivo:
        archivo.write(datos_guardados)

    # Limpiar los campos de entrada después de guardar
    entry_nombre.delete(0, tk.END)
    entry_apellido_1.delete(0, tk.END)
    entry_apellido_2.delete(0, tk.END)
    entry_puesto.delete(0, tk.END)

# Crear la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Sistema de Asistencia del Personal Bancario")

# Crear etiquetas y campos de entrada para la información del personal
etiqueta_nombre = tk.Label(ventana_principal, text="Nombre:")
etiqueta_nombre.pack()
entry_nombre = tk.Entry(ventana_principal)
entry_nombre.pack()

etiqueta_apellido_1 = tk.Label(ventana_principal, text="Primer Apellido:")
etiqueta_apellido_1.pack()
entry_apellido_1 = tk.Entry(ventana_principal)
entry_apellido_1.pack()

etiqueta_apellido_2 = tk.Label(ventana_principal, text="Segundo Apellido:")
etiqueta_apellido_2.pack()
entry_apellido_2 = tk.Entry(ventana_principal)
entry_apellido_2.pack()

etiqueta_puesto = tk.Label(ventana_principal, text="Puesto:")
etiqueta_puesto.pack()
entry_puesto = tk.Entry(ventana_principal)
entry_puesto.pack()

# Crear botón de asistencia para guardar la información del personal
boton_asistencia = tk.Button(ventana_principal, text="Registrar Asistencia", command=guardar_informacion)
boton_asistencia.pack()

# Iniciar el bucle principal del programa
ventana_principal.mainloop()


