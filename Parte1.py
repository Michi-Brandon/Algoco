def generar_rotaciones(cajas):
    from itertools import permutations
    return [tuple(rotacion) for caja in cajas for rotacion in permutations(caja)]

def fuerza_bruta_recursiva(cajas_permutadas, construccion_actual=None, indice_rotacion=0):
    if construccion_actual is None:
        construccion_actual = []

    # Comprobamos si hemos alcanzado el final de las rotaciones
    if indice_rotacion == len(cajas_permutadas):
        # Si construccion_actual es None, retornamos 0; de lo contrario, retornamos la suma de alturas
        return 0 if not construccion_actual else sum(caja[0] for caja in construccion_actual)

    caja_rotada = cajas_permutadas[indice_rotacion]

    # Comprobamos si la caja_rotada cumple con las restricciones
    if not construccion_actual or (
        caja_rotada[1] < construccion_actual[-1][1] and
        caja_rotada[2] < construccion_actual[-1][2]
    ):
        # Agregamos la caja_rotada a la construcción actual
        nueva_construccion = construccion_actual + [caja_rotada]

        # Llamada recursiva y retorno directo sin necesidad de condición
        return max(
            fuerza_bruta_recursiva(cajas_permutadas, nueva_construccion, indice_rotacion + 1),
            fuerza_bruta_recursiva(cajas_permutadas, construccion_actual, indice_rotacion + 1)
        )

    # Si la caja_rotada no cumple las restricciones, pasamos a la siguiente rotación
    return fuerza_bruta_recursiva(cajas_permutadas, construccion_actual, indice_rotacion + 1)


# Programa
with open("input.txt", "r") as f:
    lines = f.readlines()

line_iterator = iter(lines)

while True:
    try:
        n_line = next(line_iterator).strip()

        if not n_line:
            break  # Fin del archivo

        n = int(n_line)

        if n == 0:
            break

        # Resto del código para procesar las cajas
        cajas = []

        for _ in range(n):
            dimensiones = list(map(int, next(line_iterator).strip().split()))
            cajas.append(dimensiones)

        cajas_permutadas = generar_rotaciones(cajas)
        resultado = fuerza_bruta_recursiva(cajas_permutadas)
        print(resultado)

    except StopIteration:
        break  # Fin del archivo
