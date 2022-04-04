def main():

    def encontrar(array, inicio, final, elemento):
        meio = inicio + (final-inicio)//2

        if meio == final and array[final] < elemento:
            return final + 1
        elif meio == final and array[final] > elemento:
            return final
        else:
            if array[meio] < elemento < array[meio+1]:
                return meio+1
            elif array[meio] > elemento:
                return encontrar(array, inicio, meio, elemento)
            elif array[meio+1] < elemento:
                return encontrar(array, meio+1, final, elemento)


    entrada = input().split(" ")
    consultas = int(entrada[1])
    array = input().split(" ")
    array.pop()
    array = list(map(int, array))
    while consultas > 0:
        consultar = int(input())
        local = encontrar(array, 0, len(array)-1, consultar) + 1
        print(local)
        consultas -= 1


if __name__ == "__main__":
    main()
