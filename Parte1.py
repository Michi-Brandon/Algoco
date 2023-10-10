# Abre el archivo .txt
f = open("input.txt", "r")


def fuerza_bruta_recursiva(cajas):
    # Caso base: si no hay cajas, la altura es 0
    if not cajas:
        return 0
    
    # Inicializar la altura máxima
    altura_maxima = 0
    
    # Recorre todas las cajas y considera todas las rotaciones posibles
    for i in range(len(cajas)):
        for j in range(3):  # Considera las 3 rotaciones posibles
            # Filtra las cajas que cumplen con las restricciones
            cajas_validas = [caja for caja in cajas if cumple_restricciones(cajas[i], caja)]
            
            # Llamada recursiva para encontrar la altura máxima con las cajas restantes
            altura_actual = cajas[i][j] + fuerza_bruta_recursiva(cajas_validas)
            
            # Actualiza la altura máxima si es necesario
            altura_maxima = max(altura_maxima, altura_actual)
    
    return altura_maxima

def cumple_restricciones(caja_base, caja_superior):
    # Verifica que las dimensiones de la base sean estrictamente mayores que las de la caja superior
    return caja_base[1] > caja_superior[1] and caja_base[2] > caja_superior[2]

# Programa
while True:
    n = f.readline().strip()

    # Asegurarse que no sea linea vacia
    if not n:
      break
    n = int(n)
    if n == 0:
        break  
    print(n)

    # Creamos un arreglo de las cajas
    cajas = []

    # Leemos N lineas
    for _ in range(n):
        # Metemos las dimensiones de la caja i en el arreglo
        dimensiones = list(map(int, f.readline().strip().split()))
        cajas.append(dimensiones)
    resultado = fuerza_bruta_recursiva(cajas)
    print(resultado)
