a = 'A'
b = 'BBBBBB'
c = 1.1

# formatação de strings com .format
string = 'a={nome1} b={nome2} c={nome3:.2f}'
formato = string.format(
    nome1=a, nome2=b, nome3=c
)

print(formato)