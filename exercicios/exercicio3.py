primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

input_primeiro_valor = int(primeiro_valor)
input_segundo_valor = int(segundo_valor)

if input_primeiro_valor > input_segundo_valor:
    print('O {input_primeiro_valor} é maior que {input_segundo_valor}')
elif input_primeiro_valor < input_segundo_valor:
    print('O{input_segundo_valor} é maior que {input_primeiro_valor}')
else:
    print('O{input_segundo_valor} é igual ao {input_primeiro_valor}')
