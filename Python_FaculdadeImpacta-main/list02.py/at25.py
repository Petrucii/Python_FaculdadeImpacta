# Programa que lê as respostas de cinco perguntas e classifique a pessoa de acordo com o número de respostas positivas. Se a pessoa responder positivamente a 5 perguntas, ela é classificada como "Assassino". Se responder positivamente a 4 perguntas, ela é classificada como "Cúmplice". Se responder positivamente a 3 perguntas, ela é classificada como "Suspeito". Caso contrário, ela é classificada como "Inocente".

p1 = input('Telefonou para a vítima? (s/n) ').lower()
p2 = input('Esteve no local do crime? (s/n) ').lower()
p3 = input('Mora perto da vítima? (s/n) ').lower()
p4 = input('Devia algo para a vítima? (s/n) ').lower()
p5 = input('Já trabalhou com a vítima? (s/n) ').lower()

respostas = [p1, p2, p3, p4, p5]

if respostas == ['s', 's', 's', 's', 's']:
    print('Assassino')
elif respostas == ['s', 's', 's', 's', 'n'] or respostas == ['s', 's', 's', 'n', 'n']:
    print('Cúmplice')
elif respostas == ['s', 's', 'n', 'n', 'n']:
    print('Suspeito')