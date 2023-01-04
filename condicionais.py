# if / elif ... / else

# entrada = input('Você quer "entrar" ou "sair"? ')

# if entrada == 'entrar':
#     print('Você entrou no sistema !')
# elif entrada == 'sair': 
#     print('Você saiu do sistema !')
# else:
#     print('Você não escolheu nenhuma das opções')

condicao1 = False
condicao2 = False
condicao3 = True
condicao4 = True

if condicao1:
    print('Código para a condição 1')
    print('Código para a condição 1')
elif condicao2:
    print('Código para a condição 2')
elif condicao3:
    print('Código para a condição 3')
elif condicao4:
    print('Código para a condição 4')
else:
    print('Nenhuma condição foi satisfeita.')

if 10 == 10:
    print('Outro if')

print('Fora do if')