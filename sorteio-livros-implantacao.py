import random
import os
import time

def realizar_sorteio(lista_nomes):

    # Sorteia o primeiro ganhador
    primeiro_ganhador = random.choice(lista_nomes)
    
    # Remove o primeiro ganhador da lista
    lista_nomes.remove(primeiro_ganhador)
    
    # Exibe o primeiro ganhador
    print(primeiro_ganhador, " - Ganhou o primeiro sorteio!\n\n")
    
    # Exibe a mensagem de pausa
    print("Iniciando próximo sorteio com a nova lista:", lista_nomes,"\n\n")
    time.sleep(5)

    # Sorteia o segundo ganhador
    segundo_ganhador = random.choice(lista_nomes)

    print(segundo_ganhador, " - Ganhou o segundo sorteio!\n\n")
    
    # Retorna os nomes dos ganhadores
    return primeiro_ganhador, segundo_ganhador

def calcular_probabilidade(lista):
    tamanho = len(lista)
    if tamanho == 1:
        probabilidade_sorteio_1 = 100.0
        probabilidade_sorteio_2 = 100.0
    else:
        probabilidade_sorteio_1 = 1 / tamanho * 100
        probabilidade_sorteio_2 = 1 / (tamanho-1) * 100

    return probabilidade_sorteio_1, probabilidade_sorteio_2

def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear') 


limpa_tela()
lista_pessoas = []

while True:
    nome = input("Digite o nome da pessoa ou <enter> para iniciar o sorteio: ")
    if not nome:
        break
    elif nome.upper() in lista_pessoas:
        print("Nome já incluído na lista.")
    else:
        lista_pessoas.append(nome.upper())
        limpa_tela()
        print("Lista de nomes atualizada:", lista_pessoas,"\n\n")  # Exibe a lista
        chance_sorteio_1, chance_sorteio_2 = calcular_probabilidade(lista_pessoas)
        print(f"Cada uma das {len(lista_pessoas)} pessoa(s) participante(s) tem {chance_sorteio_1:.2f}% de chance de levar um livro para casa no primeiro sorteio e {chance_sorteio_2:.2f}% no segundo sorteio.\n\n")

# Limpa a tela
limpa_tela()

# Realiza o sorteio
ganhador1, ganhador2 = realizar_sorteio(lista_pessoas)

# Exibe os ganhadores
print("Parabéns: {} e {}!".format(ganhador1, ganhador2), "<mensagem_aos_ganhadores>")