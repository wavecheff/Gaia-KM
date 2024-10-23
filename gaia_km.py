import tkinter as tk
from tkinter import messagebox

def calcular_km_menorquina(kilometros, tarifa_real=0.26, tarifa_detectada=0.19):
    """
    Calcula cuántos kilómetros se deben declarar para que con la tarifa detectada (0.19 €/km)
    se reciba el importe correcto correspondiente a la tarifa real (0.26 €/km).
    """
    try:
        kilometros = float(kilometros)
        if kilometros <= 0:
            raise ValueError("El número de kilómetros debe ser mayor que 0.")
        
        importe_real = kilometros * tarifa_real
        kilometros_ajustados = importe_real / tarifa_detectada
        return round(kilometros_ajustados, 2)
    
    except ValueError as ve:
        messagebox.showerror("Error", f"Entrada no válida: {ve}")
        return None
    except Exception as e:
        messagebox.showerror("Error", f"Ha ocurrido un error inesperado: {e}")
        return None

def mostrar_resultado():
    km = entry_km.get()
    
    if not km:
        messagebox.showerror("Error", "El campo de kilómetros no puede estar vacío.")
        return

    try:
        resultado = calcular_km_menorquina(km)
        if resultado:
            label_resultado.config(text=f"Debes declarar: {resultado} km")
        else:
            label_resultado.config(text="")
    except ValueError:
        label_resultado.config(text="")

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("GaiaKm - Conversor de kilómetros")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack(padx=20, pady=20)

label_instrucciones = tk.Label(frame, text="Introduce los kilómetros detectados a 0.19 €/km:")
label_instrucciones.grid(row=0, column=0, pady=10)

entry_km = tk.Entry(frame)
entry_km.grid(row=1, column=0, pady=10)

boton_calcular = tk.Button(frame, text="Calcular", command=mostrar_resultado)
boton_calcular.grid(row=2, column=0, pady=10)

label_resultado = tk.Label(frame, text="", font=("Helvetica", 12))
label_resultado.grid(row=3, column=0, pady=20)

# Botón para salir
boton_cerrar = tk.Button(frame, text="Cerrar", command=root.quit)
boton_cerrar.grid(row=4, column=0, pady=10)

# Iniciar la aplicación
root.mainloop()

