from chatbot import menu_principal, menu_bruxos

while True:
    menu_principal()
    menu_input = input("Escolha uma opção: ")

    if menu_input == "1":
        menu_bruxos()
    elif menu_input == "2":
        print("\nMENU DE CASAS")
        print("1 - Listar todas as casas")
        casas_input = input("Escolha uma opção: ")

        if casas_input == "1":
            print("\nLista de Casas:")
            for r in prolog.query("casa(Casa, Descricao)"):
                casa = r["Casa"].replace("_", " ").title()
                descricao = r["Descricao"].replace("_", " ").title()
                print(f"- {casa} ({descricao})")

    elif menu_input == "3":
        print("Patronos")  

    elif menu_input == "4":
        print("Feitiços")  

    elif menu_input == "0":
        print("Saindo do chat... até mais!")
        break

    else:
        print("Opção inválida!")

    print()
