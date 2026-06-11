import tkinter as tk
from tkinter import messagebox
import random

#Ventana principal
ventana = tk.Tk()
ventana.title("Tic tac toe")
ventana.geometry("500x600")

#Crear el tablero 3x3
tablero = [["" for _ in range(3)]for _ in range(3)]

#X y O
turno = "X"

def clic(fila,columna): #Gestiona el movimiento de los jugadores
    global turno

    if botones[fila][columna]["text"] == "":
        botones[fila][columna]["text"] = turno

        ganador = verificar_ganador()

        if ganador:
            messagebox.showinfo(
                "Ganador",
                f"Gano {ganador}"
            )
            return
        if empate():
            messagebox.showinfo(
                "Resultado",
                "Empate"
            )
            return
        if turno == "X":
            turno = "O"
        else: 
            turno = "X"
        turno_de.config(text=f"Turno: {turno}")
    #Para jugar con la computadora
    if modo == "Computadora" and turno == "O":
        movimiento_computadora()
        ganador = verificar_ganador()
        if ganador:
            messagebox.showinfo(
                "Ganador",
                "Gano 0"
            )
            return
        if empate():
            messagebox.showinfo(
                "Resultado",
                "Empate"
                )
            return
        turno = "X"
        turno_de.config(text=f"Turno: {turno}")
botones = []

for fila in range(3):
    fila_botones = []

    for columna in range(3):
        boton = tk.Button(
            ventana,
            text="",
            width=10,
            height=4,
            font=("Arial" ,20),
            command=lambda f=fila, c=columna: clic(f,c)
        )

        boton.grid(row=fila, column=columna)
        fila_botones.append(boton)

    botones.append(fila_botones)

#Verificar ganador
def verificar_ganador(): #verifica si existe un ganador revisando las filas, columnas y diagonales

    for i in range(3): 
        if(botones[i][0]["text"] == #Filas
           botones[i][1]["text"] ==
           botones[i][2]["text"] != ""):
            return botones[i][0]["text"]
        
        if(botones[0][i]["text"] == #Columnas
           botones[1][i]["text"] ==
           botones[2][i]["text"] != ""):
            return botones[0][i]["text"]
        
    #Diagonal principal
    if (botones[0][0]["text"] ==
        botones[1][1]["text"] ==
        botones[2][2]["text"] != ""):
        return botones[0][0]["text"]
    
    #Diagonal secundaria
    if (botones[0][2]["text"] ==
        botones[1][1]["text"] ==
        botones[2][0]["text"] != ""):
        return botones[0][2]["text"]
    
    return None 

ganador = verificar_ganador()

if ganador:
    messagebox.showinfo(
        "Ganador",
        f"Gano {ganador}"
    )

#En caso de empate 
def empate(): #Verifica si la partida termina en empate revisando si hay botones vacios, si no hay y no hay ganador, es empate
    for fila in botones:
        for boton in fila:
            if boton["text"] == "":
                return False
            
    return True

if empate():
    messagebox.showinfo(
        "Resultado",
        "Empate"
    )

#Humano vs Computadora
def movimiento_computadora(): #Revisa cada movimiento aleatorio de la computadora
    disponibles = []

    for f in range(3):
        for c in range(3):
            if botones[f][c]["text"] == "":
                disponibles.append((f,c))

    if disponibles:
        fila,columna = random.choice(disponibles)
        botones[fila][columna]["text"] = "O"

#Humano vs Humano
modo = "Humano vs Humano"
def humano_vs_humano(): #Para jugar humano contra humano
    global modo
    modo = "Humano vs Humano"

def humano_vs_computadora(): #Para jugar humano contra computadora
    global modo
    modo = "Computadora"

#Botones para elegir si jugar contra otro humano o contra la computadora
tk.Button(
    ventana,
    text="Humano vs Humano",
    command=humano_vs_humano
).grid(row=4,column=0,columnspan=3)

tk.Button(
    ventana,
    text="Humano vs Computadora",
    command=humano_vs_computadora
).grid(row=5,column=0,columnspan=3)

#Boton para reinciar la partida 
def reiniciar(): #Para reiniciar el tablero o la partida, reinicia el turno
    global turno

    turno = "X"

    for fila in botones:
        for boton in fila:
            boton.config(text="")
    turno_de.config(text="Turno: X")
tk.Button(
        ventana,
        text="Reiniciar",
        command=reiniciar
    ).grid(row=7, column=0, columnspan=3)

#Mostrar de quien es turno (X o O)
turno_de = tk.Label(
    ventana,
    text="Turno de X",
    font=("Arial",14)
)

#Actualizar movimientos 
turno_de.grid(row=6, column=0, columnspan=3)
turno_de.config(
    text=f"Turno: {turno}"
)
ventana.mainloop()