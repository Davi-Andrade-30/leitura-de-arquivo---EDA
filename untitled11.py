def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for d in range(0, n-i-1):
            if lista[d] > lista[d+1]:
                lista[d], lista[d+1] = lista[d+1], lista[d]
    return lista

def main():
    nome_arquivo = input("Digite o nome do arquivo com os números (ex: numeros.txt): ")

    with open(nome_arquivo, 'r') as file:
        lista = [int(line.strip()) for line in file]

    print("Lista original:", lista)
    lista_ordenada = bubble_sort(lista)
    print("Lista ordenada:", lista_ordenada)

if __name__ == "__main__":
    main()
