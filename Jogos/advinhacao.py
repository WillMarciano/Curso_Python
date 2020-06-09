import random

print("********************************")
print("Bem Vindo ao jogo de Adivinhação")
print("********************************")

total_de_tentativas = 0
numero_secreto = round(random.randrange(1,101))
pontos = 1000

print("Informe o Nível de Dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Defina o Nível:"))

if nivel == 1:
    total_de_tentativas = 20
elif nivel == 2:
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

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
        print("você acertou o número secreto e fez {} pontos!".format(pontos))
        break
    else:
        if maior:
            print("Você errou! O Seu chute foi maior do que o número secreto.")
        else:
            print("Você errou! O Seu chute foi menor do que o número secreto.")
        pontos = (pontos - abs(numero_secreto - chute))
print("Fim do Jogo")