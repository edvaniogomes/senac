# PROFESSOR
# DUAS FUNÇÕES:
  # CADASTRO / LOGIN
  #CADASTRO: NOME, CPF E SENHA
  #LOGIN: CPF E SENHA
      # SE O LOGIN ESTIVER CORRETO: PRINT ("PARABÉNS")
      # SE O LOGIN ESTIVER ERRADO: PRINT ("TENTE NOVAMENTE")

def cadastrar_usuario():
      nome = input("Digite seu nome: ")
      cpf = input("Digite seu CPF: ")
      senha = input("Digite sua Senha: ")
      return nome, cpf, senha
      
def fazer_login(usuarios):
      cpf_l = input("Digite seu CPF: ")
      senha_l = input("Digite sua Senha: ")
      
      for usuario in usuarios:
           if cpf_l == usuario[1] and senha_l == usuario[2]:
                print("Login feito com sucesso!")
                return True
      print("CPF ou senha incorretos. Tente novamente.")
      return False

def main():
     usuarios = []
     while True:
          print("")

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