# Opção de Sair
print("0 - Sair")
# Entrada de Tipo de Cultura (Cana-de-açúcar e Milho)
print("1 - Tipo de cultura = Cana-de-açúcar: ")
print("2 - Tipo de cultura = Milho: ")
opcao = int(input("Digite opção cultura: "))
# Se cana-de-açúcar
if opcao == 1:
# Entrada de Produto (Calcário, Gesso, Fósforo, Potássio, Nitrogênio)
    print("1 - Tipo de produto = Calcário: ")
    print("2 - Tipo de produto = Gesso: ")
    print("3 - Tipo de produto = Fósforo: ")
    print("4 - Tipo de produto = Potássio: ")
    print("5 - Tipo de produto = Nitrogênio: ")
    opcao_produto = int(input("Digite opção produto: "))
# Entrada de Área de Plantio hectare
    area = float(input("Digite a área em hectares "))
    if opcao_produto == 1:
        resultado = 3000 * area
        print(f"Quantidade de calcário = {resultado:.2f} kg p/ {area:.2f} hectares")
    elif opcao_produto == 2:
        resultado = 1000 * area
        print(f"Quantidade de gesso = {resultado:.2f} kg p/ {area:.2f} hectares")
    elif opcao_produto == 3:
        resultado = 150 * area
        print(f"Quantidade de fósforo = {resultado:.2f} kg p/ {area:.2f} hectares")
    elif opcao_produto == 4:
        resultado = 80 * area
        print(f"Quantidade de potássio = {resultado:.2f} kg p/ {area:.2f} hectares")
    elif opcao_produto == 5:
        resultado = 50 * area
        print(f"Quantidade de nitrogênio = {resultado:.2f} kg p/ {area:.2f} hectares")
    else:
        print("Opção inválida")
# Se milho
elif opcao == 2:
# Entrada de Produto (Calcário, Gesso, Fósforo, Potássio, Nitrogênio)
    print("1 - Tipo de produto = Calcário: ")
    print("2 - Tipo de produto = Gesso: ")
    print("3 - Tipo de produto = Fósforo: ")
    print("4 - Tipo de produto = Potássio: ")
    print("5 - Tipo de produto = Nitrogênio: ")
    opcao_produto = int(input("Digite opção produto: "))
# Entrada de Área de Plantio hectare
    area = float(input("Digite a área em hectares "))
    if opcao_produto == 1:
        resultado = 2000 * area
        print(f"Quantidade de calcário = {resultado:.2f} kg p/ {area:.2f} hectares")
    elif opcao_produto == 2:
        resultado = 500 * area
        print(f"Quantidade de gesso = {resultado:.2f} kg p/ {area:.2f} hectares")
    elif opcao_produto == 3:
        resultado = 90 * area
        print(f"Quantidade de fósforo = {resultado:.2f} kg p/ {area:.2f} hectares")
    elif opcao_produto == 4:
        resultado = 60 * area
        print(f"Quantidade de potássio = {resultado:.2f} kg p/ {area:.2f} hectares")
    elif opcao_produto == 5:
        resultado = 120 * area
        print(f"Quantidade de nitrogênio = {resultado:.2f} kg p/ {area:.2f} hectares")
    else:
        print("Opção inválida")
# Opção Sair
elif opcao == 0:
    print("Obrigado por utilizar o nosso programa!")
else:
    print("Opcao inválida")
# Entrada de Área de Plantio hectare
# Se cana-de-açúcar
# Calcular Produto x Área
# Imprimir resultado
# Senao (milho)
# Calcular Produto x Area
# Imprimir Resultado