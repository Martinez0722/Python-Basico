nome = 'Gonzalo'
altura = 1.95
peso = 100
# imc = ... # IMC = peso / (altura x altura)

imc = peso / altura ** 2

print("%s tem %s de altura, pesa %s kg e seu imc é igual a %s "%(nome, altura, peso, imc))

# f string
print(f"{nome}, tem {altura:.2f} de altura, pesa {peso} kg e seu imc é igual a {imc}")