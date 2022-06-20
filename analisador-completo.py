soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_velho = ''
totmulher20 = 0
for p in range(1, 5):
    print('----- {}ª PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    soma_idade += idade
    if p == 1 and sexo in 'Mm':  # se a pessoa for a primeira pessoa, e se sexo for M ou m
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
media_idade = soma_idade/4
print('A média de idade do grupo, é de {} anos.'.format(media_idade))
print('O homem mais velho tem {} anos e se chama {}'.format(maior_idade_homem, nome_velho))
print('O total de mulheres com menos de 20 anos é igual a {}'.format(totmulher20))
