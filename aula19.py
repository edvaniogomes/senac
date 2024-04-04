
import math
def areatriangungulo():
    altura = float(input('Digite a altura do triângulo : '))
    base = float(input('Digite a base do triãngulo: '))
    areat = round(((base * altura) / 2),2)
    print('A área do triângulo  é de  ', areat)
def areaquadradro():
    lado = float(input('Digite a altura do quadrado: '))
    areaq = lado**2
    print('A área do quadrado é de ', areaq)
def arearetangulo():
    alturaret = float(input('Digite a altura do retângulo: '))
    baseret = float(input('Digite a altura do retângulo: '))
    arearet = round((alturaret*baseret),2)
    print('A área do retângulo é de ', arearet)
def areacirculo ():
    #area do círculo  π . r2
    raio = float(input('Digite o raio do circulo: '))
    areac = round((math.pi * raio**2),2)
    print('A área do círculo  é de ', areac)
escolha=True
while escolha:
    print("\n")
    print("Calculadora de áreas")
    print("""
    1.Calcular área do triângulo
    2.Calcular área do quadrado
    3.Calcular área do retângulo
    4.Calcular área do círculo
    5.Exit/Quit/Saída
    """)
    escolha= input("Escolha uma opção:  ")
    if escolha=="1":
        print('\n')
        areatriangungulo()

    elif escolha=="2":
      print('\n')
      areaquadradro()

    elif escolha=="3":
        print('\n')
        arearetangulo()
    elif escolha == "4":
        print('\n')
        areacirculo()
    elif escolha=="5":
      print("\n Adeus")
      escolha = None
    else:
       print("\n Escolha não válida.\n Tente outra vez.")


