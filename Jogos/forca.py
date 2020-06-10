def jogar():
    print("********************************")
    print("***Bem Vindo ao jogo da Forca***")
    print("********************************")

    palavra_secreta = "laranja".upper()
    acertou = False
    enforcou = False
    palavra = [" "] * len(palavra_secreta)
    letras_utilizadas = ""
    chances = 5

    while (not acertou and not enforcou):
        print(palavra)
        print()
        print("Chances = {} - Letras Digitadas: {}".format(chances,letras_utilizadas))
        print()
        chute = input("Qual a Letra? ").upper()

        i = 0
        for letra in palavra_secreta:
            if i < len(palavra):
                if chute == letra:
                    palavra[i] = chute

            i = i + 1
        letras_utilizadas = letras_utilizadas + chute + ', '

        print()
        print("Jogando...")
        print()

    print("Fim do Jogo")


if __name__ == "__main__":
    jogar()
