from VALID import OKI, ns
import random
import pickle
import subprocess

def limites(n,MAX):
    while n<0 or n>MAX:
        n=OKI(input("ERROR: El número ha de estar entre 0 y"+str(" "+str(MAX)+": ")))
    return n

def sing_plu(f):
    if f>1:
        co=("intentos")
    else:
        co=("intento")
    return co

while True:
    print("ADIVINA NUMERO-SUPER DESAFIO")
    print("""En este juego el usuario ha de adivinar un número,escogido
al azar por la computadora, dentro de un rango determinado""")
    print("""ESCOJA EL NIVEL DE DIFICULTAD
NIVEL 1: ENTRE 0 Y 100
NIVEL 2: ENTRE 0 Y 1000
NIVEL 3: ENTRE 0 Y 10000
NIVEL 4: ENTRE 0 Y 100000""")
    level=OKI(input("Escriba aquí su opción (de 1 a 4): "))
    while level!=1 and level!=2 and level!=3 and level!=4:
        level=OKI(input("Escriba un número comprendido entre 1 y 4: "))
    MIN=0
    MAX=10**(level+1)
    Di=(" 0 y "+str(MAX))
    numero_elegido=random.randint(MIN,MAX)
    #print(numero_elegido)
    intentos=0
    tu_numero=limites(OKI(input("Escribe un numero comprendido entre"+Di+": ")),MAX)
    diferencia=abs(tu_numero-numero_elegido)
    num_anterior=tu_numero
    intentos+=1
    repes=1 #"repes" contabiliza el número de veces seguidas que se introduce un número.
    while tu_numero!=numero_elegido:
        tu_numero=(limites(OKI(input("Escribe un numero comprendido entre"+Di+": ")),MAX))
        if abs(tu_numero-numero_elegido)>0:
            if tu_numero!=num_anterior:
                if (abs(tu_numero-numero_elegido))<diferencia:
                    print("TE ESTAS ACERCANDO")
                else:
                    print("TE ESTAS ALEJANDO")
            else:
                repes+=1
                print("HAS INTRODUCIDO EL MISMO NÚMERO",repes,"VECES SEGUIDAS")
                
        num_anterior=tu_numero     
        intentos+=1
        if intentos>(MAX/2):
            print(("PERDISTE: Superaste el límite de intentos permitido para este nivel("+str(int((MAX/2)+1))+" intentos)."),(chr(7)))
            break
        diferencia=abs(tu_numero-numero_elegido)
        #print(diferencia)
    if tu_numero==numero_elegido:
        print("¡BINGO!")
        print("Lo lograste en",intentos,sing_plu(intentos))
    conti=ns(input("¿Jugar otra vez?: "))
    if conti==("n"):
        break
    else:
        subprocess.call(["cmd.exe","/C","cls"])
    







