print("********************************")
print("Bem Vindo ao jogo de Adivinhação")
print("********************************")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while (rodada <= total_de_tentativas):
    print("Tentativa ", rodada , " do total de ", total_de_tentativas)
    chute = int(input("Digite o seu numero: "))
    print("você digitou ", chute)

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto

    if acertou:
        print("você acertou o número secreto")
    else:
        if maior:
            print("Você errou! O Seu chute foi maior do que o número secreto.")
        else:
            print("Você errou! O Seu chute foi menor do que o número secreto.")
    rodada = rodada + 1
print("Fim do Jogo")