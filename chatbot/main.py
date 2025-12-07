from pyswip import Prolog

prolog = Prolog()
prolog.consult("prolog/fatos.pl")

def chatbot_hp():
    print("Olá!")
    print("Bem-vindo ao chat de Harry Potter!")
    print("====== MENU ======")
    print("1 - Bruxos")
    print("2 - Casas")
    print("3 - Patronos")
    print("4 - Feitiços")
    print("0 - Sair")

while True:
    chatbot_hp()
    menu_input = input("Escolha uma opção: ")

    if menu_input == "1":
        print("\nMENU DE BRUXOS")
        print("1 - Listar todos os bruxos")
        print("2 - Buscar um bruxo pelo nome")
        print("3 - Buscar um bruxo pela casa")
        print("4 - Buscar bruxo pelo seu patrono")

        bruxos_input = input("Escolha uma opção: ")

        if bruxos_input == "1":
            print("\nLista de bruxos:")
            for r in prolog.query("personagem(Nome, Casa)"):
                nome = r["Nome"].replace("_", " ").title()
                casa = r["Casa"].title()
                print(f"- {nome} ({casa})")

        elif bruxos_input == "2":
            nome = input("\nDigite o nome do bruxo: ").lower().replace(" ", "_")
            query = f"personagem({nome}, _)"
            resultados = list(prolog.query(query))

            if resultados:
                print(f"Bruxo encontrado: {nome.replace('_', ' ').title()}")
            else:
                print("Bruxo não encontrado!")

        elif bruxos_input == "3":
            print("\nVocê quer consultar os bruxos de qual casa?")
            print("1 - Grifinória")
            print("2 - Sonserina")
            print("3 - Lufa-Lufa")
            print("4 - Corvinal")

            casa = input("Escolha a casa: ")
            casas_map = {
                "1": "grifinoria",
                "2": "sonserina",
                "3": "lufalufa",
                "4": "corvinal"
            }

            if casa in casas_map:
                casa_escolhida = casas_map[casa]
                print(f"\nBruxos da casa {casa_escolhida.title()}:")
                query = f"personagem(Nome, {casa_escolhida})"
                for r in prolog.query(query):
                    nome = r["Nome"].replace("_", " ").title()
                    print(f"- {nome}")
            else:
                print("Casa inválida!")

        elif bruxos_input == "4":
            print("\nDigite o nome do bruxo para consultar seu patrono:")
            
            bruxo_escolhido = input("Nome do bruxo: ").lower().replace(" ", "_")
            query = f"patrono({bruxo_escolhido}, Patrono)"
            resultados = list(prolog.query(query))

            if resultados:
                patrono = resultados[0]["Patrono"].replace("_", " ").title()
                print(f"O patrono de {bruxo_escolhido.replace('_', ' ').title()} é {patrono}")
            else:
                print("Bruxo não encontrado")

        else:
            print("Opção inválida!")

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
