import random as rn
final=0
while final==0:
 secreto = ""
 while True:
     n = rn.randint(0,9)
     if str(n) not in secreto:
         secreto += str(n)
     if len(secreto) == 3:
         break
 print(secreto)
 n1=int(secreto[0])
 n2=int(secreto[1])
 n3=int(secreto[2])
 #print('primer dijito: ',n1)
 #print('segundo dijito: ',n2)
 #print('Tercer dijito: ',n3)
 print('                          PICAS Y FIJAS')
 print()
 i=0
 picas=0
 fijas=0
 print("Tienes 10 intentos para poder hallar el número")
 while True:
   print('¡Vamos a Jugar!')
   a=int(input('Ingresa un número entre de tres cifras con la unica condidción de no tener cifras iguales.\n'))
   usuario=str(a)
   a1=int(usuario[0])
   a2=int(usuario[1])
   a3=int(usuario[2])
   long=len(usuario)
   if long<3:
     print("¿Que te Pasa?, Número de tres cifras!!!")
   elif long>3:
     print ("¿Crees que ", a,"Tiene 3 cifras? \n 'Te hace falta primaria'")
   elif a1==a2 and a2==a3:
     print("SIN CIFRAS REPETIDAS DIJE.")
   elif usuario !=secreto:
     i+=1
     if i<10:
       for s in range (len(secreto)):
         for n in range(len(usuario)):
           if secreto[s]==usuario[n]:
             if s== n:
               fijas+=1
             else:
               picas+=1
       print('El número no coincide')
       print('Has realizado', i, 'Intentos')
       print('Te quedan ', 10-i, 'intentos')
       print('Número de picas', picas,'\n Número de fijas',fijas)
     elif i==10:
       print("Perdiste")
       break
   else:
     print ('Son iguales')
     print ('Ganaste con ',i, 'Intentos')
     break
 while True:
   nuevo=input('¿Quieres jugar de nuevo? \n Digite si o no \n')
   if nuevo=='si' or nuevo=='SI' or nuevo=='Si':
     print('Sigamos!!!')
     break 
   elif nuevo=='no' or nuevo=='NO' or nuevo=='No':
     print("Nos veremos en el futuro")
     print ('¡Gran Juego!')
     final=1
     break
   else:
     print("Escribir una opción valida")