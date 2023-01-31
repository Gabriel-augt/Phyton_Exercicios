# Solicitar duas notas e verificar se a nota é superior ou inferior que 7
n1=float(input('Digite sua 1° nota:'))
n2=float(input('Digite sua 2° nota:'))
m=(n1 + n2) / 2
print(f'Sua media foi {m:.1f}.')
if m >=7 :
    print('Ótima nota, parabéns! :) ')
else:
    print('Tente melhorar...')
