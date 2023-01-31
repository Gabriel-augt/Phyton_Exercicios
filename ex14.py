# Encontrar o primeiro e o último nome
nome=str (input('Digite seu nome: ')) .strip().title()
n1=nome.split()
print(f'Nome: {nome}.')
print(f'Primeiro nome: {n1[0]}.')
print(f'Último nome: {n1[-1]}.')
