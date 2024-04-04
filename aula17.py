#   Descrição do Exercicio: Seu objetivo é criar
# um programa que simule um jogo de adivinhação.
# O programa irá gerar um número aleatório entre 1 e 100,
# e o jogador terá que tentar adivinhar qual é esse número.
#   O programa dară dicas ao jogador se o palpite fol
# muito alto, muito baixo ou correto.

#   Requisitos: O programa deve gerar um número aleatório entre 1 = 100;

#   O programa deve solicitar ao jogador que insira um palpite;
#   O programa deve comparar o palpite do jogador com o número aleatório gerado e fornecer dicas se
# o palpite foi muito alto, muito baixo ou correto;
#   O programa deve continuar pedindo palpites até que o jogador adivinhe corretamente o número;
#   O programa deve contar quantas tentativas o jogador fez até adivinhar corretamente;
#   O programa deve fornecer uma mensagem de parabéns ao jogador quando ele adivinhar
# corretamente e informar quantas tentativas foran necessárias.

# Sugestões:
# - Utilize a biblioteca random para gerar o número aleatório;
# - Utilize uma estrutura de repetição como while
# para continuar pedindo palpites até que o
# jogador acerte;
# - Utilize uma estrutura de controle if/elif/else para
# comparar o palpite do jogador com o número aleatório e forcecer as dicas
# - Utilize variaveis para armazenar o número aleatório, o palpite do jogador e o
# número de tentativas: Utilize a função input() para permitir que o jogador insira seus palpites.


#import random

#x = random.randint(1,52)

#print(x)

#x = random.randrange(1,52)

#print(x)

#import random
#import numpy as np

# Criar o array 3 x 3 com números aleatórios entre 1 e 52
#x = np.random.randint(1,52, (3,3))

#print(x)

#import random

# Criar uma lista com números entre 1 e 52
#cartas = list(range(1,53))

#print(cartas)

# Embaralha a lista de números 
#random.shuffle(cartas)

#print(cartas)

'''import random

#Define uma função que cria um peso para ordenar
def peso():
  return random.random()


lista = ["maçã", "banana", "morango"]

random.shuffle(lista,peso)

print(lista)'''

import random as nd
#.randint(1,100) calcular números aleatórios
#numero_aleatorio = nd.randint(1,100)
numero_aleatorio = nd.randrange(1,100)

tentativas = 0

print("Bem-vindo ao jogo de adivinhação! Tente adivinhar o número aleatório de 1 a 100.")

while True:
    palpite=int(input("Insira seu palpite: "))
    tentativas += 1
    if palpite < numero_aleatorio:
        print("Palpite muito baixo. Tente novamente")
    elif palpite > numero_aleatorio:
        print("Palpite muito alto. Tente novamente")
    else:
        print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")
        break



