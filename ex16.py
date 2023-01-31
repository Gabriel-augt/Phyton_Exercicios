# Encontrar 'a' primeira e última vez
frase=input('Digite uma frase: ').upper() .strip()
espaços=frase.count(' ')
a=frase.count('A')
a2=frase.rfind('A')+1
q=frase.find('A') +1
print(frase)
print(f'A letra "A" aparece {a} vezes.')
print(f'A letra "A" aparece pela 1° vez na posição {q}.')
print(f'A letra "A" aparece pela última vez na posiçao {a2-espaços}.')
