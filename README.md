# sorteio-implantacao
sorteios em python a partir de uma lista de nomes. finalidade "didático-recreativa" 😆.

## Funcionalidades

- Adicione nomes à lista de participantes, verificando se o nome já foi inserido anteriormente.
- Acompanhe a atualização da lista de nomes a cada inclusão.
- Calcule e exiba a probabilidade de cada pessoa ganhar em cada sorteio, considerando o número de participantes.
- Realize o sorteio e exiba os nomes dos dois ganhadores.

## Pré-requisitos

- Python 3.x

## Como usar

1. Clone o repositório para o seu computador:

```shell
git clone https://github.com/helbertm/sorteio-implantacao.git
```

2. Navegue até o diretório do projeto
```shell
cd sorteio-implantacao
```

3. Execute o programa com Python
```shell
python sorteio-livros-implantacao.py
```

## Contribuição
Se encontrar algum problema ou quiser trabalhar no [TO-DO](#to-do), sinta-se à vontade para abrir uma "issue" ou enviar um "pull request".

## Licença

Este projeto está licenciado sob a licença [MIT](LICENSE).

---

## Detalhes de Implementação

O programa foi implementado em Python e utiliza a biblioteca padrão do Python para realizar o sorteio aleatório e realizar a interface com o usuário no terminal.

### Funções

- `realizar_sorteio(lista_nomes)`: Realiza o sorteio dos ganhadores com base na lista de nomes fornecida.
- `calcular_probabilidade(lista)`: Calcula a probabilidade de cada pessoa ganhar em cada sorteio, considerando o número de participantes.
- `limpa_tela()`: Limpa a tela do terminal.

### Arquivo `sorteio.py`

O arquivo `sorteio-livros-implantacao.py` contém o código-fonte principal do programa. Ele solicita ao usuário que digite os nomes das pessoas, atualiza a lista de nomes, exibe a probabilidade de cada pessoa ganhar em cada sorteio e realiza o sorteio dos ganhadores.

---


## TO-DO
- [x] retirar firulas da brincadeira inicial
- [ ] permitir mais de um sorteio dinamicamente
- [ ] parametrizar se exclui ou não o ganhador da lista dos próximos sorteios
- [ ] recuperar a lista de participantes de um google spreadsheet, csv ou json
- [ ] parametrizar mensagem final aos ganhadores
- [ ] parametrizar prêmios em cada um dos sorteios
