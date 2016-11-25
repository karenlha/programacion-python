#Laboratorio 1
#Ejercicio 5
#Karen Lizbeth Herrera Avila

numero=input("segundos")
dia=input(numero/86400 "dd")
hora=input((numero-(dia*86400)/3600) "hh")
minuto=input((numero-(hora*3600)/60) "mm")
segundo=input((numero-(minuto*60)/1) "ss")
print (dia, hora, minuto, segundo)
