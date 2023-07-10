import random
import os
import time

def realizar_sorteio(lista_nomes):

    # Sorteia o primeiro ganhador
    primeiro_ganhador = random.choice(lista_nomes)
    
    # Remove o primeiro ganhador da lista
    lista_nomes.remove(primeiro_ganhador)
    
    # Exibe o primeiro ganhador
    print("Checando se todas as pessoas curtiram o post oficial...........")
    time.sleep(3)
    limpa_tela()
    print("Checando se todas as pessoas curtiram o post oficial...........OK")
    
    print("Checando se todas as pessoas estão seguindo o perfil...........")
    time.sleep(3)
    limpa_tela()
    print("Checando se todas as pessoas curtiram o post oficial...........OK")
    print("Checando se todas as pessoas estão seguindo o perfil...........OK!\n\n\n")
    print("Fazendo o primeiro sorteio\n")
    time.sleep(5)

    print(primeiro_ganhador, "ganhou o livro: Estatística - O que é!\n\n")
    
    # Exibe a mensagem de pausa
    print("Iniciando próximo sorteio com a nova lista:", lista_nomes,"\n\n")
    time.sleep(3)

    # Sorteia o segundo ganhador
    segundo_ganhador = random.choice(lista_nomes)

    print("Quem levou o livro 'Como Mentir com Estatística' para casa foi a(o) ", segundo_ganhador,"\n\n\n")
    
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


os.system('cls' if os.name == 'nt' else 'clear')
lista_pessoas = []
print("\n\n================= O  SORTEIO  DO  ANO =================\n\n")
while True:
   
    nome = input("Digite o nome da pessoa ou <enter> para fazer o sorteio: ")
    if not nome:
        break
    elif nome.upper() in lista_pessoas:
        print("Nome já existe na lista. Tente novamente.")
    else:
        lista_pessoas.append(nome.upper())
        limpa_tela()
        print("\n\n================= O  SORTEIO  DO  ANO =================\n\n")
        print("Lista de nomes atualizada:", lista_pessoas,"\n\n")  # Exibe a lista
        chance_sorteio_1, chance_sorteio_2 = calcular_probabilidade(lista_pessoas)
        print(f"Cada pessoa tem {chance_sorteio_1:.2f}% de chance de levar um livro para casa no primeiro sorteio e {chance_sorteio_2:.2f}% no segundo sorteio.\n\n")

# Limpa a tela
limpa_tela()

# Realiza o sorteio
ganhador1, ganhador2 = realizar_sorteio(lista_pessoas)

# Exibe os ganhadores
print("Parabéns: {} e {}!".format(ganhador1, ganhador2), "Os livros serão enviados para vocês gratuitamente, somente as *** taxas de manuseio de R$ 257,89 *** ficam por conta de vocês.\n\n\n")