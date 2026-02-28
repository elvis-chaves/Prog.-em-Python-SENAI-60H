# 7
# DESENVOLVA UM SISTEMA DE RESTAURANTE, ONDE O CLIENTE TEM OPÇÃO DE ESCOLHER ENTRE SALADA, MACARRONADA, SANDUICHE, SORVETE.
cardapio = ['SALADA', 'MACARRONADA', 'SANDUICHE', 'SORVETE']
# 1 - Função - cumprimentar o cliente
def comprimentar():
    print('Seja bem vindo ao restaurante X')
    print('****'* 10)
    print('Cardapio')
    print()
    print('Escolha um preto da sua preferencia:')
    print(cardapio)
# 2 - Função - restaurante
def restaurante():
    pedido = []
    
    while True:
        print("📋 Cardápio:")
        
        # Exibe o cardápio usando loop
        for i in range(len(cardapio)):
            print(f"{i + 1} - {cardapio[i]}")
        
        print("0 - Finalizar pedido")
        
        escolha = input("\nDigite o número da opção desejada: ")
        
        if escolha == "0":
            break
        
        if escolha.isdigit():
            escolha = int(escolha)
            
            if 1 <= escolha <= len(cardapio):
                item = cardapio[escolha - 1]
                pedido.append(item)
                print(f"✅ {item} adicionado ao pedido!\n")
            else:
                print("❌ Opção inválida!\n")
        else:
            print("❌ Digite apenas números!\n")
    
    print("\n🧾 Seu pedido foi:")
    for item in pedido:
        print("-", item)
    
    print("🙏 Obrigado por escolher nosso restaurante!")

# Executando o sistema
comprimentar()
restaurante()
# 3 - Sugestão utilize listas e loops 