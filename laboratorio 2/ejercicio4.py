#Laboratorio2
#Ejercicio4
#Karen Lizbeth Herrera Avila

def figura(entero):
    lista=[[],[]]
    tam=10
    P4l=[[2,4,4,1,2],[1,1,3,3,1]]
    if entero==4:
        for i in P4l[0]:
            lista[0].append(i*tam)
        for i in P4l[1]:
            lista[1].append(i*tam)
    return lista
    print lista

def funcion(P4l):
    lista=[[],[]]
    for i in P4l[0]:
        lista[0].append(i*tam)
    for i in P4l[1]:
        lista[1].append(i*tam)
    return lista
    if entero==4:
        lista=funcion(P4l)
    return lista
    
        