# Opção de Sair
print("0 - Sair")
# Entrada de Tipo de Cultura (Cana-de-açúcar e Milho)
print("1 - Tipo de cultura = Cana-de-açúcar: ")
print("2 - Tipo de cultura = Milho: ")
opcao = int(input("Digite opção cultura: "))
if opcao == 1:
# Entrada de Produto (Calcário, Gesso, Fósforo, Potássio, Nitrogênio)
    print("1 - Tipo de produto = Calcário: ")
    print("2 - Tipo de produto = Gesso: ")
    print("3 - Tipo de produto = Fósforo: ")
    print("4 - Tipo de produto = Potássio: ")
    print("5 - Tipo de produto = Nitrogênio: ")
    opcao_produto = int(input("Digite opção produto: "))
    area = float(input("Digite a área em hectares "))
    if opcao_produto == 1:
        resultado = 3000 * area
        print(f"Quantidade de calcário = {resultado:,.2f} kg p/ {area:,.2f} hectares")
    elif opcao_produto == 2:
        resultado = 1000 * area
        print(f"Quantidade de gesso = {resultado:,.2f} kg p/ {area:,.2f} hectares")
    elif opcao_produto == 3:
        resultado = 150 * area
        print(f"Quantidade de fósforo = {resultado:,.2f} kg p/ {area:,.2f} hectares")
# Entrada de Área de Plantio hectare
# Se cana-de-açúcar
# Calcular Produto x Área
# Imprimir resultado
# Senao (milho)
# Calcular Produto x Area
# Imprimir Resultado