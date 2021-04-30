import random
import math
import array
import funciones

poblacion = []
poblacion_nro = []
fit = []
func_obj = []
nueva_poblacion = []
seleccionados = []
p_cross = 0.75
p_mut = 0.05
valores = []
elite = []

char = ''

# Menu de inicio del programa
while x != d:
    print('=-------------------------=')
    print(' Tp 1 Algoritmos Geneticos ')
    print('=-------------------------=\n')
    print('a) Ruleta')
    print('b) Ruleta c/ elitismo')
    print('c) Rango\n')
    print('d) Salir')
    x = input('Elija una opcion: ')

    # Ruleta
    if x == 'a':
        for i in range(3):
            if i == 0:
                n = 19
            elif i == 1:
                n = 99
            elif i == 2:
                n = 199
            valores = []
            path = 'primera_poblacion_%d.txt' % (n + 1)
            for j in range(n):
                # Primera iteracion
                if j == 0:
                    # Generar primera poblacion, en binario y enteros con sus fitness y valores objetivo
                    poblacion, poblacion_nro, fit, func_obj = funciones.generarPoblacion()
                    # Guardar valores maximos, minimos y promedio
                    valores.append(funciones.maxMinProm(poblacion, poblacion_nro))
                    # Guardar archivos
                    funciones.guardarArchivo(poblacion, path)
                    # Imprimir tabla de resultados de la primera poblacion
                    funciones.imprimirValores(poblacion, poblacion_nro, fit, func_obj, j + 1)
                    # Seleccinar con ruleta
                    seleccionados = funciones.ruleta(poblacion, fit, 10)
                    # Realizar crossover a los seleccionados
                    nueva_poblacion = funciones.crossover(
                    p_cross, seleccionados, 5)
                    # Realizar mutacion a la poblacion
                    poblacion = funciones.mutacion(p_mut, nueva_poblacion)
                    # Convertir la nueva poblacion a numeros
                    poblacion_nro = funciones.poblacionNumero(poblacion)
                    # Calcular fitness y valores objetivos de la nueva poblacion
                    fit, func_obj = funciones.calcFitObj(poblacion_nro)
                    valores.append(funciones.maxMinProm(poblacion, poblacion_nro))
                # Proximas iteraciones
                else:
                    seleccionados = funciones.ruleta(poblacion, fit, 10)
                    nueva_poblacion = funciones.crossover(
                        p_cross, seleccionados, 5)
                    poblacion = funciones.mutacion(p_mut, nueva_poblacion)
                    poblacion_nro = funciones.poblacionNumero(poblacion)
                    fit, func_obj = funciones.calcFitObj(poblacion_nro)
                    valores.append(funciones.maxMinProm(poblacion, poblacion_nro))
                funciones.imprimirValores(poblacion, poblacion_nro, fit, func_obj, j + 2)
                path = 'poblacion_%d.txt' % (n + 1)
                funciones.guardarArchivo(poblacion, path)

    # Ruleta con elitismo
    elif x == 'b':
        for i in range(2):
            if i == 0:
                n = 19
            elif i == 1:
                n = 99
            valores = []
            path = 'primera_poblacion_%d.txt' % (n + 1)
            for j in range(n):
                # Primera iteracion
                if j == 0:
                    # Generar primera poblacion, en binario y enteros con sus fitness y valores objetivo
                    poblacion, poblacion_nro, fit, func_obj = funciones.generarPoblacion()
                    # Guardar valores maximos, minimos y promedio
                    valores.append(funciones.maxMinProm(poblacion, poblacion_nro))
                    # Guardar archivos
                    funciones.guardarArchivo(poblacion, path)
                    # Imprimir tabla de resultados de la primera poblacion
                    funciones.imprimirValores(poblacion, poblacion_nro, fit, func_obj, j + 1)
                    # Elegir la elite
                    elite = (funciones.elitismo(poblacion, fit))
                    # Seleccinar con ruleta
                    seleccionados = funciones.ruleta(poblacion, fit, 8)
                    # Realizar crossover a los seleccionados
                    nueva_poblacion = funciones.crossover(p_cross, seleccionados, 4)
                    # Realizar mutacion a la poblacion
                    poblacion = funciones.mutacion(p_mut, nueva_poblacion)
                    # Incluir a la elite en la nueva poblacion
                    for i in elite:
                        poblacion.append(i)
                    poblacion_nro = funciones.poblacionNumero(poblacion)
                    fit, func_obj = funciones.calcFitObj(poblacion_nro)
                    valores.append(funciones.maxMinProm(poblacion, poblacion_nro))
                # Proximas iteraciones
                else:
                    elite = (funciones.elitismo(poblacion, fit))
                    seleccionados = funciones.ruleta(poblacion, fit, 8)
                    nueva_poblacion = funciones.crossover(p_cross, seleccionados, 4)
                    poblacion = funciones.mutacion(p_mut, nueva_poblacion)
                    for i in elite:
                        poblacion.append(i)
                    poblacion_nro = funciones.poblacionNumero(poblacion)
                    fit, func_obj = funciones.calcFitObj(poblacion_nro)
                    valores.append(funciones.maxMinProm(poblacion, poblacion_nro))
            funciones.imprimirValores(poblacion, poblacion_nro, fit, func_obj, j + 2)
            path = 'poblacion_%d.txt' % (n + 1)
            funciones.guardarArchivo(poblacion, path)
# elif x == 'c':

# with open("poblacion.txt", "wb") as fp:  # Pickling
#    pickle.dump(poblacion, fp)
#    fp.close()
# with open("poblacion.txt", "rb") as fp:
#    b = pickle.load(fp)
#    fp.close()
