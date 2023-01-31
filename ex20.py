# Solicitar os dias de aluguel e km percorrido, sendo que o carro custa R$60 e km R$0,15
dias = int(input('Quantos dias deseja alugar? '))
km = float(input('Quantos quilômetros rodado? '))
pago = ( dias * 60) + (km * 0.15)
print(f'Com o carro alugado por {dias} dias e com {km}km rodados...')
print(f'Total a pagar: R${pago:.2f}.')
