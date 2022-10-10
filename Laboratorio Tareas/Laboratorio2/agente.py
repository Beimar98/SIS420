#!/usr/bin/env python
# coding: utf-8

# In[115]:





# # agente basado en objetos
# # Universitarios: 
# # -Beimar Miguel Ceron
# -Maidy Rocio Mamani Lugo
# 
# -Jorge Rodrigo Morant Jalacori
# 
# -Segovia Vargas Gerson
# 
# -Carlos Alberto Mora Vallejos 
# 
# -Felix Antonio Flores Yampara

# In[1]:


import random
from tkinter import Y 

def crear_mapa_laberinto(numero_filas, numero_columnas, numero_paredes, numero_espacios):
    # Se crea un mapa lleno de paredes
    mapa_laberinto = []
    numero_paredes_generadas = 0
    for fila in range(0, numero_filas):
        fila_mapa_laberinto = []
        for columna in range(0, numero_columnas):
            fila_mapa_laberinto.append('#')
        mapa_laberinto.append(fila_mapa_laberinto)

    #Se ubica aleatoriamente un punto de inicio y a partir de ese punto se llenan espacios
    numero_espacios_generados = 0
    fila_posicion_actual = random.randrange(numero_filas)
    columna_posicion_actual = random.randrange(numero_columnas)
    mapa_laberinto[fila_posicion_actual][columna_posicion_actual] = ' '
    numero_espacios_generados += 1

    # Agente = Y
    ficha_fila = random.randrange(numero_filas)
    ficha_columnas = random.randrange(numero_columnas)
    mapa_laberinto[fila_posicion_actual][columna_posicion_actual] = 'Y'


    while numero_espacios_generados < numero_espacios:
        direccion = random.randrange(4)
        if direccion == 0 and fila_posicion_actual > 0:
            fila_posicion_actual -= 1
        elif direccion == 1 and fila_posicion_actual < numero_filas - 1:
            fila_posicion_actual += 1
        elif direccion == 2 and columna_posicion_actual > 0:
            columna_posicion_actual -= 1
        else:
            if columna_posicion_actual < numero_columnas - 1:
                    columna_posicion_actual += 1
            
        if mapa_laberinto[fila_posicion_actual][columna_posicion_actual] == '#':
            mapa_laberinto[fila_posicion_actual][columna_posicion_actual] = ' '     
            numero_espacios_generados += 1

    return mapa_laberinto

numero_filas = int(input('Introduzca el número de filas del laberinto: '))
numero_columnas = int(input('Introduzca el número de columnas del laberinto: '))
numero_paredes = int(input('Introduzca el número de paredes del laberinto: '))
numero_espacios = numero_filas * numero_columnas - numero_paredes

laberinto = crear_mapa_laberinto(numero_filas, numero_columnas, numero_paredes, numero_espacios)

# insertar x en una posicion aleatoria en el laberinto

while True:
    x_=random.randrange(numero_filas)
    y_=random.randrange(numero_columnas)
    if laberinto[x_][y_] == ' ':
        laberinto[x_][y_] = 'X'
        break

for fila_mapa_laberinto in laberinto:
    print(fila_mapa_laberinto)


# In[71]:


# copiar laberinto sin mutar
laberinto2 = laberinto.copy()


# In[72]:


def posicion_x(laberinto):
    for i in range(len(laberinto)):
        for j in range(len(laberinto[i])):
            if laberinto[i][j] == 'X':
                return i,j

def posicion_y(laberinto):
    for i in range(len(laberinto)):
        for j in range(len(laberinto[i])):
            if laberinto[i][j] == 'Y':
                return i,j

def win(laberinto):
    x,y = posicion_x(laberinto)
    a,b = posicion_y(laberinto)
    if x == a and y == b:
        print("Ganaste")
        return True
    else:
        return False

def printLaberinto(laberinto):
    for fila_mapa_laberinto in laberinto:
        print(fila_mapa_laberinto)


# In[116]:


def agente2(laberinto):
  x,y = posicion_x(laberinto)
  a,b = posicion_y(laberinto)
  # mover la "y" hacia la "x" sin pasar por paredes
  if x > a:
    print("abajo")
    if laberinto[a+1][b] != '#':
      print("abajo-2")
      laberinto[a+1][b] = 'Y'
      laberinto[a][b] = '*'
      a = a+1
      return
    elif laberinto[a][b+1] != '#':
      print("derecha")
      laberinto[a][b+1] = 'Y'
      laberinto[a][b] = '*'
      b = b+1
      return
    elif laberinto[a][b-1] != '#':
      print("izquierda")
      laberinto[a][b-1] = 'Y'
      laberinto[a][b] = '*'
      b = b-1
      return
    elif laberinto[a-1][b] != '#':
      print("arriba")
      laberinto[a-1][b] = 'Y'
      laberinto[a][b] = '*'
      a = a-1
      return
  elif x < a:
    print("arriba")
    if laberinto[a-1][b] != '#':
      print("arriba-2")
      laberinto[a-1][b] = 'Y'
      laberinto[a][b] = '*'
      a = a-1
      return
    elif laberinto[a][b+1] != '#':
      print("derecha")
      laberinto[a][b+1] = 'Y'
      laberinto[a][b] = '*'
      b = b+1
      return
    elif laberinto[a][b-1] != '#':
      print("izquierda")
      laberinto[a][b-1] = 'Y'
      laberinto[a][b] = '*'
      b = b-1
      return
    elif laberinto[a+1][b] != '#':
      print("abajo")
      laberinto[a+1][b] = 'Y'
      laberinto[a][b] = '*'
      a = a+1
      return

  elif y > b:
    print("derecha")
    if laberinto[a][b+1] != '#':
      print("derecha-2")
      laberinto[a][b+1] = 'Y'
      laberinto[a][b] = '*'
      b = b+1
      return
    elif laberinto[a+1][b] != '#':
      print("abajo")
      laberinto[a+1][b] = 'Y'
      laberinto[a][b] = '*'
      a = a+1
      return
    elif laberinto[a-1][b] != '#':
      print("arriba")
      laberinto[a-1][b] = 'Y'
      laberinto[a][b] = '*'
      a = a-1
      return
    elif laberinto[a][b-1] != '#':
      print("izquierda")
      laberinto[a][b-1] = 'Y'
      laberinto[a][b] = '*'
      b = b-1
      return

  elif y < b:
    print("izquierda")
    if laberinto[a][b-1] != '#':
      print("izquierda-2")
      laberinto[a][b-1] = 'Y'
      laberinto[a][b] = '*'
      b = b-1
      return
    elif laberinto[a+1][b] != '#':
      print("abajo")
      laberinto[a+1][b] = 'Y'
      laberinto[a][b] = '*'
      a = a+1
      return
    elif laberinto[a-1][b] != '#':
      print("arriba")
      laberinto[a-1][b] = 'Y'
      laberinto[a][b] = '*'
      a = a-1
      return
    elif laberinto[a][b+1] != '#':
      print("derecha")
      laberinto[a][b+1] = 'Y'
      laberinto[a][b] = '*'
      b = b+1
      return
      
  return laberinto
  


# In[6]:


# agente basado en el modelo movimiento de "y" abajo y derecha hasta llegar a la ficha x
def agente(laberinto):
  y_fila, y_columna = posicion_y(laberinto)
  cont = 0
  while(cont < 10):
    cont += 1
    print("-----------------------------------")
    # ver si se puede mover hacia abajo
    if y_fila < len(laberinto) - 1 and laberinto[y_fila + 1][y_columna] != '#' and laberinto[y_fila + 1][y_columna] != '*':
      y_fila += 1
      laberinto[y_fila][y_columna] = 'Y'
      laberinto[y_fila - 1][y_columna] = '*'
      printLaberinto(laberinto)
      if win(laberinto):
        break
    # ver si se puede mover a la derecha
    elif y_columna < len(laberinto[y_fila]) - 1 and laberinto[y_fila][y_columna + 1] != '#' and laberinto[y_fila][y_columna + 1] != '*':
      y_columna += 1
      laberinto[y_fila][y_columna] = 'Y'
      laberinto[y_fila][y_columna - 1] = '*'
      printLaberinto(laberinto)
      if win(laberinto):
        break
    # ver si se puede mover hacia arriba
    elif y_fila > 0 and laberinto[y_fila - 1][y_columna] != '#' and laberinto[y_fila - 1][y_columna] != '*':
      y_fila -= 1
      laberinto[y_fila][y_columna] = 'Y'
      laberinto[y_fila + 1][y_columna] = '*'
      printLaberinto(laberinto)
      if win(laberinto):
        break
    # ver si se puede mover a la izquierda
    elif y_columna > 0 and laberinto[y_fila][y_columna - 1] != '#' and laberinto[y_fila][y_columna - 1] != '*':
      y_columna -= 1
      laberinto[y_fila][y_columna] = 'Y'
      laberinto[y_fila][y_columna + 1] = '*'
      printLaberinto(laberinto)
      if win(laberinto):
        break


agente(laberinto)


# In[121]:


agente2(laberinto)
printLaberinto(laberinto)


# In[52]:


laberinto = laberinto2


# In[75]:


printLaberinto(laberinto2)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




