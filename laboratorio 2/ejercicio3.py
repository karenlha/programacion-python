#Laboratorio2
#Ejercicio3
#Karen Lizbeth Herrera Avila
import math
t=[[1,2,4,1],[1,3,1,1]]
p=[2,2]
salida=[[],[]]
for i in range(11):
    num=math.random(0,3)
    vertice=[t[0][num],[t[1][num]]]
    Pmx=(p[0]-vertice[0])/2
    Pmy=(p[1]-vertice[1])/2
    salida[0].append(Pmx)
    salida[1].append(Pmy)
print salida
plt.plot(salida)