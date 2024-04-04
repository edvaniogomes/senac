# PROFESSOR

import random as nd
#.randint(1,100) calcular números aleatórios
def jogo_advinhar():
    numero_aleatorio = nd.randint(1,100)
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
jogo_advinhar()       