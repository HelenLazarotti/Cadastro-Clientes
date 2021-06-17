print('='*50)
print('Luiz Piscinas \n"A empresa que sempre busca qualidade e inovação"')
print('='*50)

atendimento = int(input('[1] - Presencial \n[2] - Online \nDigite a forma de atendimento: '))
presencial = 1
if atendimento == 1:
    print('Agora você precisa informar os dados abaixo')
    cidade = input('Digite a cidade: ')
    bairro = input('Bairro: ')
    num = int(input('Número: '))
    ponto = input('Ponto de referência: ')
    fora = input('É fora de Arroio do Sal? \n[A] - Sim \n[B] - Não \n[]: ')
    a = 'sim'
    b = 'não'
    if fora == a:
        print('Ok! Vamos continuar!!!')
    else:
        print('Terá custos adicionais conforme a localidade')
else:
    hora = str(input('Digite o horário que deseja o atendimento: '))
    dia = input('Dia da semana: ')
    regiao = input('De qual estado você é: ')
    local = input('Cidade: ')

    confirma = int(input('Você marcou às {} horas, na {}. \nNo estado de {} na cidade de {}. \nTe esperamos na {}!'
                         ''.format(hora, dia, regiao, local, dia)))
