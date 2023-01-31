# Nome em letras maiúsculas, letras minúsculas, quantas letras tem no nome e no primeiro nome
nome=input('Digite seu nome completo: ') .strip()
contar= nome.count(' ')
primeiro_nome = nome.split()
print(f'Seu nome em letras maiúsculas: {nome.upper()}.',f'\nSeu nome em letras minúsculas: {nome.lower()}.')
print(f'Seu 1° nome é {primeiro_nome[0].title()} e ele tem {len(primeiro_nome[0])} letras.')
print(f'Seu nome completo tem {len(nome) - contar} letras.')
