def main():
    monedas = [1, 2, 5]
    monedas_usadas = [0, 0, 0]
    #print("monedas_usadas 2 vale: " + str(monedas_usadas[2]))
    cantidad = int(input("introduce una cantidad: \n"))

    monedas_usadas[2] = int((cantidad / monedas[2]))
    #cantidad = cantidad % monedas[2]
    cantidad %= monedas[2]

    monedas_usadas[1] = int((cantidad / monedas[1]))
    #cantidad = cantidad % monedas[2]
    cantidad %= monedas[1]

    monedas_usadas[0] = cantidad
    cantidad -= cantidad

    print("las monedas usadas son: \n" + "5 euros: "+ str(monedas_usadas[2])
        + "\n2 euros: "+ str(monedas_usadas[1])
        + "\n1 euros: "+ str(monedas_usadas[0]) +
        ".\n La cantidad restante es: " + str(cantidad))
            
        
        
    


if __name__ == "__main__":
    main()