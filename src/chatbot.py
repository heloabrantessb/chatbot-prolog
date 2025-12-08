from pyswip import Prolog

prolog = Prolog()
prolog.consult("regras.pl")
prolog.consult("fatos.pl")

def menu_principal():
    print("""
    Olá! Seja bem-vindo ao Chatbot de Harry Potter.
    ====== MENU ======
    1 - Bruxos
    2 - Casas
    3 - Patronos
    4 - Feitiços
    0 - Sair
    """)


def menu_bruxos():
    print("""
    =====MENU DE BRUXOS=====
    1 - Mostrar detalhes do bruxo
    2 - Mostrar a casa do bruxo
    3 - Buscar um bruxo pelo nome
        """)
    
    bruxos_input = input("Escolha uma opção: ")

    # Mostrar detalhes do bruxo
    if bruxos_input == "1":
        nome = input("Digite o nome do bruxo (nome e sobrenome): ").lower().replace(" ", "_")
        result = list(prolog.query(f"detalhes({nome}, Resultado)"))

        if result:
            print(f"Detalhes de {nome.replace('_', ' ').title()}:")
            print(result[0]["Resultado"])
        else:
            print("Bruxo não encontrado")
        return
    
    # Mostrar a casa do bruxo
    elif bruxos_input == "2":
        nome = input("Digite o nome do bruxo (nome e sobrenome): ").lower().replace(" ", "_")
        
        result = list(prolog.query(f"casa_do_personagem({nome}, Casa)"))
        
        if result:
            casa = result[0]["Casa"]
            print(f"O bruxo(a) {nome.replace('_', ' ').title()} pertence à casa {casa.title()}")
        else:
            print(f"Bruxo(a) '{nome.replace('_', ' ').title()}' não encontrado.")    

    # Buscar bruxo pelo nome
    elif bruxos_input == "3":
        busca = input("Digite o nome (ou parte do nome) do bruxo: ").lower().replace(" ", "_")
        
        result = list(prolog.query(f"buscar_personagem({busca}, NomeCompleto)"))
        
        if result:
            print("Bruxos encontrados:")
            for item in result:
                nome_encontrado = item["NomeCompleto"].replace('_', ' ').title()
                print(f"- {nome_encontrado}")
            print(f"Total: {len(result)} bruxos(as) encontrados(as).")
        else:
            print("Nenhum bruxo(a) encontrado.")
    