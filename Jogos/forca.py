import random
def jogar():
    mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_utilizadas = ""
    palavra = ["_" for l in palavra_secreta]

    acertou = False
    enforcou = False
    chances = 8

    while (not acertou and not enforcou):
        print("Chances = {} \nLetras Digitadas: {}".format(chances,letras_utilizadas))
        desenha_forca(chances)
        print(palavra)
        chute = input("Qual a Letra? ").strip().upper()

        if chute in palavra_secreta:
            verifica_chute(chute,palavra,palavra_secreta)
        else:
            chances -= 1

        enforcou = chances == 0
        acertou = "_" not in palavra

        letras_utilizadas = letras_utilizadas + chute + ', '
        print("Jogando...\n")

    verifica_resultado(acertou,palavra_secreta)

def mensagem_abertura():
    print("**********************************")
    print("*** Bem Vindo ao jogo da Forca ***")
    print("**********************************\n")

def carrega_palavra_secreta():
    arquivo = open("Arquivos\palavras.txt", "r")
    palavra_secreta = []

    for linha in arquivo:
        linha = linha.strip()
        palavra_secreta.append(linha)

    arquivo.close()

    n = random.randrange(0,len(palavra_secreta))
    palavra_secreta = palavra_secreta[n].upper()
    return palavra_secreta

def verifica_chute(chute,palavra,palavra_secreta):
    i = 0
    for letra in palavra_secreta:
        if chute == letra:
            palavra[i] = chute
        i += 1

def verifica_resultado(acertou,palavra_secreta):
    if acertou:
        print("Parabéns, você ganhou!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")
    else:
        print("Você foi enforcado!")
        print("A palavra era {}".format(palavra_secreta))
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 7):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if (__name__ == "__main__"):
    jogar()