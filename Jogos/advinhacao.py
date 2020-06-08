import random

print("********************************")
print("Bem Vindo ao jogo de Adivinhação")
print("********************************")

numero_secreto = round(random.randrange(1,101))
total_de_tentativas = 3
rodada = 1

while (rodada <= total_de_tentativas):
    print("Tentativa ", rodada , " do total de ", total_de_tentativas)
    chute = int(input("Digite o seu número entre 1 e 100: "))
    print("você digitou ", chute)

    if chute < 1 or chute > 100:
        print("Você deve digitar um número entre 1 e 100!")
        rodada = rodada + 1
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
    rodada = rodada + 1

print("Fim do Jogo")