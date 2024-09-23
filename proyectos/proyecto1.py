#proyecto1 : Juego de adivinanza
#reglas : no puedo usar chatgpt

import random
def numero():
 aleatorio = random.randrange(1,10)
 return(aleatorio)
 print(numero())
 numero_aleatorio = numero()

adivinanza = int(input("Adivine el numero que piensa la maquina"))

if adivinanza == numero_aleatorio:
     print(f"Adivinaste el numero {numero_aleatorio}")
else:
     print("Vales madre") 


