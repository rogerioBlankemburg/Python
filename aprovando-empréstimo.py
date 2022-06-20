print('-=' * 20)
print('{:^40}'.format('SIMULADOR DE EMPRÉSTIMO BANCÁRIO'))
print('-=' * 20)

valor = float(input('Qual o valor do imóvel? '))
salario = float(input('Qual o seu salário? '))
anos = int(input('Em quantos anos irá pagar o imóvel? '))
prestacao = valor/(anos * 12)

# prestacao = valor/meses
if prestacao > (salario * 30/100):
    print('Infelizmente seu empréstimo foi negado.')
else:
    print('Boas! Empréstimo aprovado! :)')