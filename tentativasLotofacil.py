from random import sample

                  #jogo a ser utilizado para conferência

jogo = [1, 2, 3, 4, 7, 9, 11, 13, 14, 15, 18, 21, 22, 23, 25]

b = 0
z = 0

while b < 15:
  sorteio = sample(range(1,26),15)
  sorteio.sort()
  a = set(jogo).intersection(sorteio)
  b = len(a)
  z=z+1

print("O número de tentativas para que acertasse",b,"números, foi de",z,"vezes")
print("Os números que acertou foram:",a)
print("Os números sorteados foram:",sorteio)
