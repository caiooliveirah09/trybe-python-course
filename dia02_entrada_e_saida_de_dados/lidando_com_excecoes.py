"""while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
"""
"""try:
    arquivo = open("arquivo.txt", "r")
except OSError:
    # será executado caso haja uma exceção
    print("arquivo inexistente")
else:
    # será executado se tudo ocorrer bem no try
    print("arquivo manipulado e fechado com sucesso")
    arquivo.close()
finally:
    # será sempre executado, independentemente de erro
    print("Tentativa de abrir arquivo")
"""
pessoas_aprovadas = []
pessoas_reprovadas = []
pessoas_com_notas = {}
pessoas = open("notas.txt", mode="r")
conteudo = pessoas.read()
conteudo = conteudo.split()

for i in range(0, len(conteudo), 2):
    key = conteudo[i]
    value = conteudo[i+1]
    pessoas_com_notas[key] = value


for pessoa in pessoas_com_notas:
    print(pessoa)
    if int(pessoas_com_notas[pessoa]) < 6:
        pessoas_reprovadas.append(pessoa)
    else:
        pessoas_aprovadas.append(pessoa)

print(pessoas_reprovadas)
print(pessoas_aprovadas)
pessoas.close()