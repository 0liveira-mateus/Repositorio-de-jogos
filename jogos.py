import adivinhacao
import forca

print("*********************************")
print("   Bem vindo a sala de jogo      ")
print("*********************************")

print("Escolha um jogo para se divertir!!")
print("(1) = Forca | (2) = Adivinhação")

opcao = int(input("Digite:"))

if (opcao == 1):
    print("Jogando Forca")
    forca.jogar()
elif (opcao == 2):
    print("Jogando Adivinhação")
    adivinhacao.jogar()