import funciones as f

char = ''

p_cross = 0.75
p_mut = 0.05

# Menu de inicio del programa
print('+-------------------------+')
print(' Tp 1 Algoritmos Geneticos ')
print('+-------------------------+\n')
print('Probabilidad de crossover: ', p_cross)
print('Probabilidad de mutación: ', p_mut, '\n')
print('a) Ruleta')
print('b) Ruleta c/ elitismo')
print('c) Torneo')
print('d) Cambiar probabilidades')
print('e) Salir\n')
x = input('Elija una opcion: ')


# Bucle del programa
while x != 'e':
    poblacion = []
    poblacion_nro = []
    fit = []
    func_obj = []
    nueva_poblacion = []
    seleccionados = []
    valores = []
    elite = []

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
            for j in range(n):
                # Primera iteracion
                if j == 0:
                    # Generar primera poblacion, en binario y enteros con sus fitness y valores objetivo
                    poblacion, poblacion_nro, fit, func_obj = f.generarPoblacion()
                    # Guardar valores maximos, minimos y promedio
                    valores.append(f.maxMinProm(func_obj))
                    # Imprimir tabla de resultados de la primera poblacion
                    f.imprimirValores(poblacion, poblacion_nro, fit, func_obj, j + 1)
                    # Seleccinar con ruleta
                    seleccionados = f.ruleta(poblacion, fit, 10)
                    # Realizar crossover a los seleccionados
                    nueva_poblacion = f.crossover(p_cross, seleccionados, 5)
                    # Realizar mutacion a la poblacion
                    poblacion = f.mutacion(p_mut, nueva_poblacion)
                    # Convertir la nueva poblacion a numeros
                    poblacion_nro = f.hacerNumero(poblacion)
                    # Calcular fitness y valores objetivos de la nueva poblacion
                    fit, func_obj = f.calcFitObj(poblacion_nro)
                    valores.append(f.maxMinProm(func_obj))
                # Proximas iteraciones
                else:
                    seleccionados = f.ruleta(poblacion, fit, 10)
                    nueva_poblacion = f.crossover(p_cross, seleccionados, 5)
                    poblacion = f.mutacion(p_mut, nueva_poblacion)
                    poblacion_nro = f.hacerNumero(poblacion)
                    fit, func_obj = f.calcFitObj(poblacion_nro)
                    valores.append(f.maxMinProm(func_obj))
            # Imprimir tabla de poblacion
            f.imprimirValores(poblacion, poblacion_nro, fit, func_obj, j + 2)
            f.guardarArchivo(valores, n+1)
            # Realiar graficas de los valores
            f.graficas(valores, n+1)

    # Ruleta con elitismo
    elif x == 'b':
        for i in range(2):
            if i == 0:
                n = 19
            elif i == 1:
                n = 99
            valores = []
            for j in range(n):
                # Primera iteracion
                if j == 0:
                    # Generar primera poblacion, en binario y enteros con sus fitness y valores objetivo
                    poblacion, poblacion_nro, fit, func_obj = f.generarPoblacion()
                    # Guardar valores maximos, minimos y promedio
                    valores.append(f.maxMinProm(func_obj))
                    # Imprimir tabla de resultados de la primera poblacion
                    f.imprimirValores(poblacion, poblacion_nro, fit, func_obj, j + 1)
                    # Elegir la elite
                    elite = (f.elitismo(poblacion, fit))
                    # Seleccinar con ruleta
                    seleccionados = f.ruleta(poblacion, fit, 8)
                    # Realizar crossover a los seleccionados
                    nueva_poblacion = f.crossover(p_cross, seleccionados, 4)
                    # Realizar mutacion a la poblacion
                    poblacion = f.mutacion(p_mut, nueva_poblacion)
                    # Incluir a la elite en la nueva poblacion
                    for i in elite:
                        poblacion.append(i)
                    poblacion_nro = f.hacerNumero(poblacion)
                    fit, func_obj = f.calcFitObj(poblacion_nro)
                    valores.append(f.maxMinProm(func_obj))
                # Proximas iteraciones
                else:
                    elite = (f.elitismo(poblacion, fit))
                    seleccionados = f.ruleta(poblacion, fit, 8)
                    nueva_poblacion = f.crossover(p_cross, seleccionados, 4)
                    poblacion = f.mutacion(p_mut, nueva_poblacion)
                    for i in elite:
                        poblacion.append(i)
                    poblacion_nro = f.hacerNumero(poblacion)
                    fit, func_obj = f.calcFitObj(poblacion_nro)
                    valores.append(f.maxMinProm(func_obj))
            f.imprimirValores(poblacion, poblacion_nro, fit, func_obj, j + 2)
            f.guardarArchivo(valores, n+1)
            f.graficas(valores, n+1)

    # Torneo
    elif x == 'c':
        for i in range(3):
            if i == 0:
                n = 19
            elif i == 1:
                n = 99
            elif i == 2:
                n = 199
            valores = []
            for j in range(n):
                # Primera iteracion
                if j == 0:
                    # Generar primera poblacion, en binario y enteros con sus fitness y valores objetivo
                    poblacion, poblacion_nro, fit, func_obj = f.generarPoblacion()
                    # Guardar valores maximos, minimos y promedio
                    valores.append(f.maxMinProm(func_obj))
                    # Imprimir tabla de resultados de la primera poblacion
                    f.imprimirValores(poblacion, poblacion_nro, fit, func_obj, j + 1)
                    # Seleccinar con ruleta
                    seleccionados = f.torneo(poblacion, fit, 10)
                    # Realizar crossover a los seleccionados
                    nueva_poblacion = f.crossover(p_cross, seleccionados, 5)
                    # Realizar mutacion a la poblacion
                    poblacion = f.mutacion(p_mut, nueva_poblacion)
                    # Convertir la nueva poblacion a numeros
                    poblacion_nro = f.hacerNumero(poblacion)
                    # Calcular fitness y valores objetivos de la nueva poblacion
                    fit, func_obj = f.calcFitObj(poblacion_nro)
                    valores.append(f.maxMinProm(func_obj))
                # Proximas iteraciones
                else:
                    seleccionados = f.torneo(poblacion, fit, 10)
                    nueva_poblacion = f.crossover(p_cross, seleccionados, 5)
                    poblacion = f.mutacion(p_mut, nueva_poblacion)
                    poblacion_nro = f.hacerNumero(poblacion)
                    fit, func_obj = f.calcFitObj(poblacion_nro)
                    valores.append(f.maxMinProm(func_obj))
            # Imprimir tabla de poblacion
            f.imprimirValores(poblacion, poblacion_nro, fit, func_obj, j + 2)
            f.guardarArchivo(valores, n+1)
            # Realiar graficas de los valores
            f.graficas(valores, n+1)

    # Cambiar valores de probabilidad
    elif x == 'd':
        p_cross = int(input('Probabilidad de crossover: '))/100
        p_mut = int(input('Probabilidad de mutacion: '))/100

    print('+-------------------------+')
    print(' Tp 1 Algoritmos Geneticos ')
    print('+-------------------------+\n')
    print('Probabilidad de crossover: ', p_cross)
    print('Probabilidad de mutación: ', p_mut, '\n')
    print('a) Ruleta')
    print('b) Ruleta c/ elitismo')
    print('c) Torneo')
    print('d) Cambiar probabilidades')
    print('e) Salir\n')
    x = input('Elija una opcion: ')
