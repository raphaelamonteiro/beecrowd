# -*- coding: utf-8 -*-

# Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. 
# Após, calcule e mostre o valor a ser pago.

codigo1, quantidade1, valor1 = map(float, input().split(" "))

codigo2, quantidade2, valor2 = map(float, input().split(" "))

total = ((quantidade1) * (valor1)) + ((quantidade2) * (valor2))

print("VALOR A PAGAR: R$ %0.2f" %total)
