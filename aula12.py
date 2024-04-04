'''print("oi")

import numpy as np

a = np.array([1,2,3,4,5])


a=a.max()

print(a)'''

def cadastrar_login():
  while True:
    try:
      login = str(input("Digite seu Login: "))
      cpf = int(input("Digite seu CPF: "))
      senha = int(input("Digite sua Senha: "))
      break
    except ValueError:
      print("Valor inválido.")

  cadSenha = [login, cpf, senha]
  print("Meu nome é: {}, Meu CPF é: {}, Minha Senha é: {}".format(login, cpf, senha))

cadastrar_login()

'''def cadastrar_usuario():
  while True:
    try:
      nome = str(input("Digite seu nome: "))
      cpf = int(input("Digite seu CPF: "))
      senha = int(input("Digite sua Senha: "))
      break
    except ValueError:
      print("Valor inválido.")

  cadastro = [nome, cpf, senha]

  print("Meu nome é: {}, Meu CPF é: {}, Minha Senha é: {}".format(nome, cpf, senha))

cadastrar_usuario()'''

