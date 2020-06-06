print("********************************")
print("Bem Vindo ao jogo de Adivinhação")
print("********************************")

total_de_tentativas = 3
numero_secreto = 42

for rodada in range(1,total_de_tentativas + 1):

    print("Tentativa {} de {}".format(rodada,total_de_tentativas))
    chute = int(input("Digite um número entre 1 e 100: "))
    print("você digitou ", chute)

    if chute < 0 or chute > 100:
        print("Você deve digitar um número entre 1 e 100!")
        continue

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto

    if acertou:
        print("você acertou o número secreto")
        break
    else:
        if maior:
            print("Você errou! O Seu chute foi maior do que o número secreto.")
        else:
            print("Você errou! O Seu chute foi menor do que o número secreto.")

print("Fim do Jogo")