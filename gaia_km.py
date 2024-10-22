import tkinter as tk
from tkinter import messagebox

# Función para realizar la conversión
def convertir_kilometraje():
    try:
        importe = float(entry_importe.get())
        km_declarados = importe / 0.19  # Tarifa incorrecta en La Menorquina
        label_resultado.config(text=f"Debes declarar: {km_declarados:.2f} km")
    except ValueError:
        messagebox.showerror("Error", "Por favor, introduce un valor numérico válido.")

# Creación de la ventana principal
root = tk.Tk()
root.title("GaiaKm - Conversión de Kilómetros")
root.geometry("400x400")

# Arte ASCII de un helado
ascii_helado = """
       .
     --.-"°'-.
    -/       \-
   (    .-.    )
   (  .-._.-.  )
   (    '-'    )
    \  ===  /
     \  ==  /
      \  =  /
       \   /
        \ /
         V
"""

# Etiqueta para el arte ASCII
label_ascii = tk.Label(root, text=ascii_helado, font=("Courier", 12), justify="center")
label_ascii.pack(pady=10)

# Entrada para el importe en euros
label_importe = tk.Label(root, text="Introduce el importe (€):")
label_importe.pack(pady=5)
entry_importe = tk.Entry(root)
entry_importe.pack(pady=5)

# Botón para realizar la conversión
boton_convertir = tk.Button(root, text="Convertir a km", command=convertir_kilometraje)
boton_convertir.pack(pady=10)

# Etiqueta para mostrar el resultado
label_resultado = tk.Label(root, text="")
label_resultado.pack(pady=10)

# Ejecución de la ventana principal
root.mainloop()
