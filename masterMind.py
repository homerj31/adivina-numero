#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random 
codigo="".join(list(map(lambda x: str(x), random.sample(range(0,9), 4))))

 

print ("##### Bienvenido/a al Mastermind! ######\n")

print ("Tienes que adivinar un numero de 4 cifras distintas")

propuesta = raw_input("¿Que codigo propones?: ")

 

# bucle hasta que el numero introducido coincida con el codigo aleatorio

intentos = 0

while propuesta != codigo:

    intentos += 1

    aciertos = 0

    coincidencias = 0

 

    # recorremos la propuesta y verificamos en el codigo

    for i in range(4):

        if propuesta[i] == codigo[i]:

            aciertos = aciertos + 1

        elif propuesta[i] in codigo:

            coincidencias = coincidencias + 1

    print ("Tu propuesta (", propuesta, ") tiene", aciertos, "aciertos y", coincidencias, "coincidencias.")

    # pedimos siguiente propuesta*

    propuesta = input("Propón otro codigo: ")

 

print ("Felicitaciones! Adivinaste el codigo en", intentos, "intentos.")
