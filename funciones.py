import random
import pickle
import matplotlib.pyplot as plt

# Generar primera poblacion en binario y en numeros enteros y calcular su fitness y valor en la funcion objetivo
def generarPoblacion():
    poblacion = []
    poblacion_nro = []
    fitness = []
    func_obj = []
    cromosoma = []
    cromosoma_txt = ''
    for i in range(10):
        # Generar cromosomas binarios en formato texto
        for j in range(30):
            cromosoma.append(str(random.randint(0, 1)))
        cromosoma_txt = ''.join(cromosoma)
        # Agregar cromosoma a la poblacion
        poblacion.append(cromosoma_txt)
        cromosoma = []
    # Transformar los cromosomas de texto a numeros enteros
    poblacion_nro = hacerNumero(poblacion)
    # Calcular el fitness y el valor objetivo de cada cromosoma
    fitness, func_obj = calcFitObj(poblacion_nro)
    return poblacion, poblacion_nro, fitness, func_obj

# Transformar la poblacion de texto a numeros enteros
def hacerNumero(l):
    a = []
    for i in l:
        a.append(int('0b' + i, base=2))
    return a

# Calcular fitness y valor en funcion objetivo
def calcFitObj(nro):
    f = []
    o = []
    for i in nro:
        # Funcion objetivo
        o.append((i / (2**30 - 1))**2)
    for i in o:
        # Fitness
        f.append(i / sum(o))
    return f, o

# Calcular maximos, minimos y promedios
def maxMinProm(l):
    a = []
    # Maximos
    a.append(max(l))
    # Minimos
    a.append(min(l))
    # Promedios
    a.append(sum(l)/len(l))
    return a

# Metodo de ruleta
def ruleta(p, f, n):
    pares = []
    seleccionados = []
    for j in range(n):
        r = random.uniform(0, 1)
        fit = 0
        for i in f:
            fit += i
            if fit > r:
                pares.append(p[f.index(i)])
                break
        if len(pares) == 2:
            seleccionados.append(pares)
            pares = []
    return seleccionados

def torneo(l, f, n):
    a = [[], []]
    seleccionados = []
    pares = []
    for j in range(n):
        for i in range(2):
            m = random.randint(0, 9)
            a[i].append(l[m])
            a[i].append(f[m])
        if a[0][1] > a[1][1]:
            pares.append(a[0][0])
        else:
            pares.append(a[1][0])
        a = [[], []]
        if len(pares) == 2:
            seleccionados.append(pares)
            pares = []
    return seleccionados


# Metodo de crossover
def crossover(p, l, m):
     s = []
     for i in range(m):
         # Elegir padre y madre de entre los seleccionados
         padre = l[i][0]
         madre = l[i][1]
         # Calculo de probabilidad
         n = random.random()
         if n < p:
             # Realizar corte en lugar aleatorio y engendrar hijos
             r = random.randint(0, 29)
             hijo = padre[:r] + madre[r:]
             hija = madre[:r] + padre[r:]
             # Agregar hijos a la poblacion
             s.append(hijo)
             s.append(hija)
         else:
             # Crossover negativo, mantener padre y madre en la proxima generacion
             s.append(padre)
             s.append(madre)
     return s

# Metodo de mutacion
def mutacion(p, l):
    a = []
    for i in l:
        # Calculo de probabilidad
        n = random.random()
        if n < p:
            s = list(i)
            # Seleccionar gen aleatorio
            r = random.randint(0, 29)
            # Cambiar de 0 a 1
            if s[r] == '0':
                s[r] = '1'
                j = ''.join(s)
                a.append(j)
            # Cambiar de 1 a 0
            elif s[r] == '1':
                s[r] = '0'
                j = ''.join(s)
                a.append(j)
        else:
            # Mutacion negativa, mantener cromosoma en la proxima generacion
            a.append(i)
    return a

# Metodo de elitismo
def elitismo(l, p):
    a = []
    b = []
    # Crear array auxiliar de fitness
    for i in p:
        b.append(i)
    # Ordenar fitness de mayor a menor
    p.sort()
    # Elegir los cromosomas de mayor fitness
    a.append(l[b.index(p[9])])
    a.append(l[b.index(p[8])])
    return a

# Impresion de tablas
def imprimirValores(pob, pob_nro, fit, obj, n):
    print("+-----------------------------------------------------------------------------------+")
    print('Generacion ', n)
    print("+-----------------------------------------------------------------------------------+")
    print("Cromosoma                      Número     Fitness            Func. objetivo")
    # Impresion de cromosomas, valor numerico, fitness y valor objetivo
    for i in pob:
        print(i, pob_nro[pob.index(i)], fit[pob.index(i)], obj[pob.index(i)])
    print("+-----------------------------------------------------------------------------------+")
    # Impresion de suma de fitness y de funcion objetivo
    print('Suma:                                    ', round(sum(fit)), '                 ',sum(obj))
    # Impresion del promedio de los cromosomas, el fitness y la funcion objetivo
    print('Promedio:                    ', sum(pob_nro)/len(pob_nro), '                  ', sum(obj)/len(obj))
    # Impresion de cromosoma minimo, su valor numerico, su fitness y su valor objetivo
    print('Mínimo: ', pob[pob_nro.index(min(pob_nro))], min(pob_nro), fit[pob_nro.index(min(pob_nro))], obj[pob_nro.index(min(pob_nro))])
    # Impresion de cromosoma maximo, su valor numerico, su fitness y su valor objetivo
    print('Máximo: ', pob[pob_nro.index(max(pob_nro))], max(pob_nro), fit[pob_nro.index(max(pob_nro))], obj[pob_nro.index(max(pob_nro))], '\n')

# Realizar graficas de valores maximos, minimos y promedios
def graficas(l, n):
    max = []
    min = []
    prom = []
    title = 'Poblacion %d'%n
    for i in l:
        max.append(i[0])
        min.append(i[1])
        prom.append(i[2])
    plt.plot(range(n), max, linewidth = 3, c = 'FireBrick')
    plt.plot(range(n), min, linewidth = 3, c = 'Gold')
    plt.plot(range(n), prom, linewidth = 3, c = 'ForestGreen')
    plt.grid()
    plt.xlim(0, n)
    plt.ylim(0, 1)
    plt.autoscale(False)
    plt.xlabel('Rojo: Maximos, Amarillo: Minimos, Verde: Promedios')
    plt.title(title)
    plt.savefig('valores%d.svg'%n, bbox_inches='tight')
    plt.show()
    plt.clf()

def guardarArchivo(v, n):
    a = []
    b = []
    for i in v:
        for j in i:
            b.append(str(j))
        b.insert(0, '[')
        b.append(']')
        a.append(','.join(b))
        b = []
    c = '\n'.join(a)
    path = "valores%d.txt"%n
    with open(path, "wb") as fp:
        pickle.dump(c, fp)
    a = []
