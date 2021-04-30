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
print('+-------------------------+')
print(' Tp 1 Algoritmos Geneticos ')
print('+-------------------------+\n')
print('a) Ruleta')
print('b) Ruleta c/ elitismo')
print('c) Rango')
print('d) Cambiar probabilidades')
print('e) Salir\n')
x = input('Elija una opcion: ')

# Bucle del programa
while x != 'e':
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
                    poblacion, poblacion_nro, fit, func_obj = funciones.generarPoblacion()
                    # Guardar valores maximos, minimos y promedio
                    valores.append(funciones.maxMinProm(func_obj))
                    # Imprimir tabla de resultados de la primera poblacion
                    funciones.imprimirValores(poblacion, poblacion_nro, fit, func_obj, j + 1)
                    # Seleccinar con ruleta
                    seleccionados = funciones.ruleta(poblacion, fit, 10)
                    # Realizar crossover a los seleccionados
                    nueva_poblacion = funciones.crossover(p_cross, seleccionados, 5)
                    # Realizar mutacion a la poblacion
                    poblacion = funciones.mutacion(p_mut, nueva_poblacion)
                    # Convertir la nueva poblacion a numeros
                    poblacion_nro = funciones.hacerNumero(poblacion)
                    # Calcular fitness y valores objetivos de la nueva poblacion
                    fit, func_obj = funciones.calcFitObj(poblacion_nro)
                    valores.append(funciones.maxMinProm(func_obj))
                # Proximas iteraciones
                else:
                    seleccionados = funciones.ruleta(poblacion, fit, 10)
                    nueva_poblacion = funciones.crossover(p_cross, seleccionados, 5)
                    poblacion = funciones.mutacion(p_mut, nueva_poblacion)
                    poblacion_nro = funciones.hacerNumero(poblacion)
                    fit, func_obj = funciones.calcFitObj(poblacion_nro)
                    valores.append(funciones.maxMinProm(func_obj))
            # Imprimir tabla de poblacion
            funciones.imprimirValores(poblacion, poblacion_nro, fit, func_obj, j + 2)
            # Realiar graficas de los valores
            funciones.graficas(valores, n+1)

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
                    poblacion, poblacion_nro, fit, func_obj = funciones.generarPoblacion()
                    # Guardar valores maximos, minimos y promedio
                    valores.append(funciones.maxMinProm(func_obj))
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
                    poblacion_nro = funciones.hacerNumero(poblacion)
                    fit, func_obj = funciones.calcFitObj(poblacion_nro)
                    valores.append(funciones.maxMinProm(func_obj))
                # Proximas iteraciones
                else:
                    elite = (funciones.elitismo(poblacion, fit))
                    seleccionados = funciones.ruleta(poblacion, fit, 8)
                    nueva_poblacion = funciones.crossover(p_cross, seleccionados, 4)
                    poblacion = funciones.mutacion(p_mut, nueva_poblacion)
                    for i in elite:
                        poblacion.append(i)
                    poblacion_nro = funciones.hacerNumero(poblacion)
                    fit, func_obj = funciones.calcFitObj(poblacion_nro)
                    valores.append(funciones.maxMinProm(func_obj))
            funciones.imprimirValores(poblacion, poblacion_nro, fit, func_obj, j + 2)
            funciones.graficas(valores, n+1)
    #elif x == 'c':
    elif x == 'd':
        p_cross = int(input('Probabilidad de crossover: '))/100
        p_mut = int(input('Probabilidad de crossover: '))/100
    print('+-------------------------+')
    print(' Tp 1 Algoritmos Geneticos ')
    print('+-------------------------+\n')
    print('a) Ruleta')
    print('b) Ruleta c/ elitismo')
    print('c) Rango')
    print('d) Cambiar probabilidades')
    print('e) Salir\n')
    x = input('Elija una opcion: ')
