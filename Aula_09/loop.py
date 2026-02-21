#i = 0
#while i <=999:
#    print((i), end=" ")
#    i += 1
#    if i % 10 == 0:
#        print(i)

nomes = []
contador = 0

while contador < 10:
    nome = input(f"Digite o nome da {contador + 1}ª pessoa: ")
    nomes.append(nome)
    contador += 1

print("\nLista de nomes cadastrados:")
contador = 0

while contador < len(nomes):
    print(f"{contador + 1} - {nomes[contador]}")
    contador += 1