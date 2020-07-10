#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random 
codigo="".join(list(map(lambda x: str(x), random.sample(range(0,9), 4))))
print(codigo)

def numero():
	while True:
		codi = raw_input("¿Que codigo propones?: ")
		if len(codi) == 4:
			return codi
			break
		else:
			print("Asegurese de que su código contienen 4 dígitos.")
			

print ("##### Bienvenido/a al Mastermind! ######\n")

print ("Tienes que adivinar un numero de 4 cifras distintas")

propuesta = numero()

# bucle hasta que el numero introducido coincida con el codigo aleatorio

intentos = 0

while propuesta != codigo:
	intentos += 1
	aciertos = 0
	coincidencias = 0
	
	for i in range(4):
		if propuesta[i] == codigo[i]:
			aciertos = aciertos + 1
		elif propuesta[i] in codigo:
			coincidencias = coincidencias + 1
	
	print ("Tu propuesta (", propuesta, ") tiene", aciertos, "aciertos y", coincidencias, "coincidencias.")
	propuesta = numero()

print ("Felicitaciones! Adivinaste el codigo en", intentos, "intentos.")
