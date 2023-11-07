from tkinter import Tk, Button, Entry

# Variables globales para almacenar los valores y la operación
numero1 = 0
operacion = ""

# Función para limpiar la pantalla
def clear():
    pantalla.delete(0, "end")

# Función para manejar los números y la operación seleccionada
def agregar_numero(numero):
    pantalla.insert("end", str(numero))

def agregar_operacion(operador):
    global numero1
    global operacion
    numero1 = float(pantalla.get())
    operacion = operador
    clear()

# Función para realizar la operación y mostrar el resultado
def calcular_resultado():
    try:
        numero2 = float(pantalla.get())
        clear()
        if operacion == "+":
            pantalla.insert(0, str(numero1 + numero2))
        elif operacion == "-":
            pantalla.insert(0, str(numero1 - numero2))
        elif operacion == "*":
            pantalla.insert(0, str(numero1 * numero2))
        elif operacion == "/":
            if numero2 != 0:
                pantalla.insert(0, str(numero1 / numero2))
            else:
                clear()
                pantalla.insert(0, "Error")
    except ValueError:
        clear()
        pantalla.insert(0, "Error")

# Configuración ventana principal
root = Tk()
root.title("Calculadora POO")
root.resizable(0, 0)
root.geometry("550x250")

# Configuración pantalla de salida
pantalla = Entry(root, width=40, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=4, padx=1, pady=1)

# Configuración botones
boton_1 = Button(root, text="1", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: agregar_numero(1)).grid(row=1, column=0, padx=1, pady=1, sticky="ew")
boton_2 = Button(root, text="2", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: agregar_numero(2)).grid(row=1, column=1, padx=1, pady=1, sticky="ew")
boton_3 = Button(root, text="3", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: agregar_numero(3)).grid(row=1, column=2, padx=1, pady=1, sticky="ew")
boton_4 = Button(root, text="4", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: agregar_numero(4)).grid(row=2, column=0, padx=1, pady=1, sticky="ew")
boton_5 = Button(root, text="5", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: agregar_numero(5)).grid(row=2, column=1, padx=1, pady=1, sticky="ew")
boton_6 = Button(root, text="6", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: agregar_numero(6)).grid(row=2, column=2, padx=1, pady=1, sticky="ew")
boton_7 = Button(root, text="7", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: agregar_numero(7)).grid(row=3, column=0, padx=1, pady=1, sticky="ew")
boton_8 = Button(root, text="8", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: agregar_numero(8)).grid(row=3, column=1, padx=1, pady=1, sticky="ew")
boton_9 = Button(root, text="9", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: agregar_numero(9)).grid(row=3, column=2, padx=1, pady=1, sticky="ew")
boton_igual = Button(root, text="=", width=20, height=3, bg="red", fg="white", borderwidth=0, cursor="hand2", command=calcular_resultado).grid(row=4, column=0, columnspan=2, padx=1, pady=1, sticky="ew")
boton_punto = Button(root, text=".", width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0, command=lambda: agregar_numero(".")).grid(row=4, column=2, padx=1, pady=1, sticky="ew")
boton_mas = Button(root, text="+", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=lambda: agregar_operacion("+")).grid(row=1, column=3, padx=1, pady=1, sticky="ew")
boton_menos = Button(root, text="-", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=lambda: agregar_operacion("-")).grid(row=2, column=3, padx=1, pady=1, sticky="ew")
boton_multiplicacion = Button(root, text="*", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=lambda: agregar_operacion("*")).grid(row=3, column=3, padx=1, pady=1, sticky="ew")
boton_division = Button(root, text="/", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=lambda: agregar_operacion("/")).grid(row=4, column=3, padx=1, pady=1, sticky="ew")

root.mainloop()
