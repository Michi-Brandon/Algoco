# Abre el archivo .txt
f = open("input.txt", "r")

# Program
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
    for i in cajas:
      print(i)