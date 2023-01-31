# Valor do produto sem desconto e com 5% de desconto
preco=float (input('Digite o preço do produto: '))
desconto=preco-(preco*5/100)
print(f'Preço sem desconto R${preco:.2f}.',f'\nPreço com desconto de 5%: R${desconto:.2f}.')
