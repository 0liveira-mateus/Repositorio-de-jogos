import random

def jogar():

    bemvindo()
    palavra_secreta = carregando_palavras()
    letras_acertadas = substitue_letras_certas(palavra_secreta)
    print(letras_acertadas)



    enforcou = False
    acertou = False
    erros = 0


    while not enforcou and not acertou:

        chute = pedirchute()

        if chute in palavra_secreta:
            marca_chute_correto(chute, palavra_secreta, letras_acertadas)
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)


    if(acertou):
        mensagem_vitoria()
    else:
        print("Você perdeu!!")
    print("Fim do jogo")



# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def bemvindo():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")


def carregando_palavras():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def substitue_letras_certas(palavra):
    return ["_" for letra in palavra]


def pedirchute():
    chute = input("Qual letra? ").strip().upper()
    return chute

def marca_chute_correto(chute, palavra_secreta, letras_acertadas):
    for posicao, letra in enumerate(palavra_secreta):
        if chute.upper() == letra.upper():
            letras_acertadas[posicao] = letra


def mensagem_vitoria():
    return print("Você ganhou!!")

if(__name__ == "__main__"):
    jogar()

