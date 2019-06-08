def main():
    palabra = input("introduce una palabra: ")
    #print(palabra[2])
    contador_fallos = 0
    while (1):
        letra = input("introduce una letra: ")
        if letra in palabra:
                palabra = palabra.replace(letra, '', 1)
                print("acierto")
        else:
                print("fallo")
                contador_fallos+=1


        if (contador_fallos == 5):
                print("Perdiste")
                return

        if len(palabra) == 0:
                print("Ganaste")
                return



    #print(contador_fallos)


            
        
        
    


if __name__ == "__main__":
    main()
