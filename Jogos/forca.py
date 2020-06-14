def jogar():
    print("********************************")
    print("***Bem Vindo ao jogo da Forca***")
    print("********************************")

    palavra_secreta = "laranja".upper()
    palavra = ["_"] * len(palavra_secreta)

    acertou = False
    enforcou = False

    letras_utilizadas = ""
    chances = 6
    tentativa = 0

    while (not acertou and not enforcou):
        print(palavra)
        print("Chances = {} - Letras Digitadas: {}".format(chances,letras_utilizadas))
        chute = input("Qual a Letra? ").strip().upper()

        i = 0
        if chute in palavra_secreta:
            for letra in palavra_secreta:
                if chute == letra:
                    palavra[i] = chute
                i += 1
                tentativa += 1
        else:
            chances -= 1

        enforcou = chances == 0
        acertou = "_" not in palavra

        letras_utilizadas = letras_utilizadas + chute + ', '
        print("Jogando...")
        print("")

    if acertou:
        print("Você Venceu")
    else:
        print("Você Perdeu")
    print("Fim do Jogo")


if __name__ == "__main__":
    jogar()
