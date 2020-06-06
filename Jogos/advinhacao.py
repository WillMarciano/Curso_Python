print("********************************")
print("Bem Vindo ao jogo de Adivinhação")
print("********************************")

numero_secreto = 42

chute = int(input("Digite o seu numero: "))

print("você digitou ", chute)

if numero_secreto == chute:
    print("você acertou o numero secreto")
else:
    print("Você errou")