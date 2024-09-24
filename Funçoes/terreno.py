comprimento = int(input("Digitr o comprimento: "))
largura     = int(input("Digitr a Largura: "))
preco_m2    = int(input("Digitr o Valor do M2: "))

area = comprimento * largura #m2
preco_total = area * preco_m2

print(f"O terreno possui {area}m2 e custa R${preco_total:,.2f}")
