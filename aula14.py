# DUAS FUNÇÕES:
  # CADASTRO / LOGIN
  #CADASTRO: NOME, CPF E SENHA
  #LOGIN: CPF E SENHA
      # SE O LOGIN ESTIVER CORRETO: PRINT ("PARABÉNS")
      # SE O LOGIN ESTIVER ERRADO: PRINT ("TENTE NOVAMENTE")

def cadastrar_usuario():
  while True:
    try:
      nome = str(input("Digite seu nome: "))
      cpf = int(input("Digite seu CPF: "))
      senha = int(input("Digite sua Senha: "))
      break
    except ValueError:
      print("tente novamente.")

  cadastro = []
  cadastro.append(nome)
  cadastro.append(cpf)
  cadastro.append(senha)

  print("Meu nome é: {}, Meu CPF é: {}, Minha Senha é: {}".format(cadastro[0], cadastro[1], cadastro[2]))

#cadastrar_usuario()

def cadastrar_login():
  while True:
    try:
      login = str(input("Digite seu Login: "))
      cpfL = int(input("Digite seu CPF: "))
      senhaL = int(input("Digite sua Senha: "))
      break
    except ValueError:
      print("tente novamente.")

  cadSenha = []
  cadSenha.append(login)
  cadSenha.append(cpfL)
  cadSenha.append(senhaL)
 
  print("Meu login é: {}, Meu CPF é: {}, Minha Senha é: {}".format(cadSenha[0], cadSenha[1], cadSenha[2]))

#cadastrar_login()

opcao=1

while opcao:
    print("0. Sair")
    print("1. Cadastro")
    print("2. Login")
   
    opcao = int(input("Opção: "))

    if(opcao==1):
        cadastrar_usuario()
    if(opcao==2):
        cadastrar_login()