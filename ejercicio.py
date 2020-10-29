# -*- coding: utf-8 -*-
import os
def cargar(archivo):
  f = open(archivo)
  lineas = [x.strip("\n") for x in f.readlines()]
  f.close()
  return lineas

def leer_alumnos(archivo):
    a=open(archivo,'r')
    lista=a.readlines()
    a.close()
    lista=[x.strip('\n') for x in lista]
    return lista
def leer_porcentajes(archivo):
    a=open(archivo,'r')
    lista=a.readlines()
    a.close()
    lista=[x.strip('\n') for x in lista]
    matriz=[x.split(",")for x in lista]
    return matriz
def leer_materias(archivo):
    a=open(archivo,'r')
    lista=a.readlines()
    a.close()
    lista=[x.strip('\n') for x in lista]
    return lista
alumnos=cargar('alumnos.txt')
porcentajes=cargar('porcentaje.txt')
materias=cargar('materias.txt')
print(alumnos)
print(porcentajes)
print(materias)
def recoger_notas():
  f=open('notas.txt','w')
  alumno=cargar('alumnos.txt')
  materia=cargar('materias.txt')
  porcentajes=cargar('porcentaje.txt')
  for a in alumno:
    for m in materia:
      f.write(a + ", " + m)
      for p in porcentajes:
        n = input("ingrese la nota : " + p[0] + " para la materia de " + m + " del " + a+": ")
        f.write(", " + n)
      f.write("\n")
  f.close()
  
def cacular_definitiva():
    n=open('notas.txt', "r")
    lista=n.readlines()
    n.close()
    o=open('definitivas.txt', "w")
    porcentajes=leer_porcentajes('porcentaje.txt')
    lista=[x.strip('\n') for x in lista]
    matriz=[x.split(",")for x in lista]
    for k in matriz:
      a = k[0]
      mat = k[1]
      valores = [int(x) for x in k[2:]]
      s = 0
      for m  in range(len(porcentajes)):
        s+=(int(porcentajes[m][1])/100)*valores[m]
      o.write(a + ", " + mat + ", " + str(s) + "\n")

if not os.path.exists("notas.txt"):    
  recoger_notas()
cacular_definitiva()

