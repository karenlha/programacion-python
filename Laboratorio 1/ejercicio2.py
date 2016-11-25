#Laboratorio 1
#Ejercicio 2
#Karen Lizbeth Herrera Avila

interes_por_año=0.04
saldo_inicial= input("cantidad a depositar")
nvo_saldo=0
for i in range(4):
    saldo=saldo_inicial*1.04
  nvo_saldo=nvo_saldo+saldo
  print nvo_saldo