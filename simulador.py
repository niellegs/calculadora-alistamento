import datetime
anoNasc = int(input('Ano de nascimento: '))
sexo = str(input('''Qual o seu sexo?
Digite [f] para feminino
Digite [m] para masculino
Sua resposta: '''))
ano = datetime.date.today()
data = ano.year
idade = data - anoNasc
if idade < 18 and sexo == 'm':
    excesso = (18-idade) + data
    print('''    Quem nasceu em {} tem {} anos em {}. 
    Ainda faltam {} anos para o alistamento.
    Seu alistamento será em {}.''' .format(anoNasc, idade, data,18 - idade, excesso))
elif idade > 18 and sexo == 'm':
    excesso = idade - 18
    anoIdeal = data - excesso
    print('''    Quem nasceu em {} tem {} anos em {}.
    Você já deveria ter se alistado há {} anos. 
    Seu alistamento foi em {}.''' .format(anoNasc, idade, data, excesso, anoIdeal))
elif idade == 18 and sexo == 'm':
    print('''    Quem nasceu em {} tem {} anos em {},
    Você tem que se alistar IMEDIATAMENTE!'''.format(anoNasc, idade, data))
else:
    print('O alistamento é apenas obrigatório para pessoas do sexo masculino.')
