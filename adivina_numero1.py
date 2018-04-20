import random
from VALID import ns, OKI
import subprocess
import pickle

def rango(n1,n2):
    while True:
        n=input("Introduce un número entre "+str(n1)+" y "+str(n2)+": ")#("("+str(int(timer/7)),"semanas y",timer%7,"dias)")
        try:
            n=int(n)
        except:
            pass
        else:
            if n>=n1 and n<=n2:
                break
    return n

def rango_valido(nu):
    while True:
         try:
             R=(nu).split(",")
             Rango=[int(R[0]),int(R[1])]
             Rango.sort()
         except:
             nu=input("Establece el rango (escribir ambos números separados por una coma): ")
             pass
         else:
            break
    return Rango
        
        
        

def aprox(difer,n1,n2,vis):
    grado_desvia=round(difer*100/((abs(n2-n1))+1),5)
    if n1==n2:
        pass
    else:
        if grado_desvia<25:
            if vis==("s"):
                print("GRADO DE DESVIACION:",grado_desvia)
            contes=("UN POCO MAS: YA CASI LO TIENES")
        if grado_desvia>=25 and grado_desvia<50:
            if vis==("s"):
                print("GRADO DE DESVIACION:",grado_desvia)
            contes=("NO ESTA MAL: SIGUE PROBANDO")
        if grado_desvia>=50 and grado_desvia<100:
            if vis==("s"):
                print("GRADO DE DESVIACION",grado_desvia)
            contes=("DEMASIADO LEJOS")
    return contes
    

def intent(n):
    if n>1:
        n=("intentos")
    else:
        n=("intento")
    return n

while True:
    print("ADIVINA EL NÚMERO")
    nu=rango_valido(input("Establece el rango (escribir ambos números separados por una coma): "))#SE NECESITA ESTABLECER LA EXCEPCION PARA EVITAR VALORES NO ENTEROS
    vis=ns(input("¿Desea visualizar el grado de desviacion?: "))
    n1=nu[0];n2=nu[1]
    num_elect=random.randint(n1,n2)
    intentos=0
    while True:
        tu_numero=rango(n1,n2)
        if tu_numero!=num_elect:
            intentos+=1
            difer=abs(tu_numero-num_elect)
            aproxi=aprox(difer,n1,n2,vis)
            print(aproxi)
        else:
            print("¡BINGO!")
            intentos+=1
            if intentos==1:
                P=100
            else:
                no_inte=((n2-n1)+1)-intentos
                P=(round(no_inte*100/((n2-n1)+1)))/10
            ntents=intent(intentos)
            print("Lo conseguiste en",intentos,ntents)
            print("TU PUNTUACIÓN:",P,"sobre 10")
            break
    puntuacion=pickle.load(open("mejor_marca","rb"))
    if P>puntuacion[4]:
        puntuacion[4]=P
        print("")
        print("¡NUEVO RECORD!")
    print("MEJOR PUNTUACION PARA ESTE NIVEL: ",puntuacion[4])
    pickle.dump(puntuacion,open("mejor_marca","wb"))
    preg=ns(input("¿Jugar otra vez?: "))
    if preg==("n"):
        break
    else:
        subprocess.call(["cmd.exe","/C","cls"])

