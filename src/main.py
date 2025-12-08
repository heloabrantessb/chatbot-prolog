from chatbot import menu_principal, menu_bruxos, menu_casas, menu_patronos, menu_feiticos

while True:
    menu_principal()
    menu_input = input("Escolha uma opção: ")

    match menu_input:
        case "0":
            print("Saindo do chat...")
            break
        case "1":
            menu_bruxos()
        case "2":
            menu_casas()
        case "3":
            menu_patronos()
        case "4":
            menu_feiticos()
        case _:
            print("Opção Inválida")
    print()
