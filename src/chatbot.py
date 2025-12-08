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
    
def menu_casas():

    print("""
    =====MENU DE CASAS=====
    1 - Listar todas as casas
    2 - Mostrar detalhes da casa
    3 - Mostrar chefe de casa
        """)
    casas_input = input("Escolha uma opção: ")

    # 1. Listar todas as casas
    if casas_input == "1":
        result = list(prolog.query("listar_casas(Casa)"))
        
        if result:
            for item in result:
                casa = item["Casa"].title()
                print(f"- {casa}")
        else:
            print("Nenhuma casa encontrada nos fatos.")
            
    # 2. Mostrar detalhes da casa 
    elif casas_input == "2":
        nome_casa = input("Digite o nome da casa: ").lower().replace(" ", "_")
        result = list(prolog.query(f"detalhes_casa({nome_casa}, Detalhes)"))
        
        if result:
            detalhes = result[0]["Detalhes"].strip()
            print(detalhes)
        else:
            print(f"Casa '{nome_casa.title().replace('_', ' ')}' não encontrada.")

    # 3. Mostrar chefe de casa
    elif casas_input == "3":
        nome_casa = input("Digite o nome da casa: ").lower().replace(" ", "_")
        result = list(prolog.query(f"chefe_da_casa({nome_casa}, Chefe)"))
        
        if result:
            chefe = result[0]["Chefe"].replace('_', ' ').title()
            print(f"O chefe da casa {nome_casa.title().replace('_', ' ')} é: {chefe}.")
        else:
            print(f"Chefe não encontrado para a casa '{nome_casa.title().replace('_', ' ')}'.")        
    else:
        print("Opção inválida.")
    return

def menu_patronos():
    print("""
    =====MENU DE PATRONOS=====
    1 - Mostrar Patrono de um Bruxo
    2 - Listar todos os Patronos e seus donos
    """) 
    patronos_input = input("Escolha uma opção: ")

    # 1. Mostrar Patrono de um Bruxo
    if patronos_input == "1":
        nome = input("Digite o nome do bruxo (nome e sobrenome): ").lower().replace(" ", "_")
        
        result = list(prolog.query(f"patrono_do_bruxo({nome}, Forma)"))
        
        if result:
            forma = result[0]["Forma"].replace('_', ' ').title()
            print(f"O Patrono de {nome.replace('_', ' ').title()} é um(a) {forma}.")
        else:
            print(f"Bruxo(a) '{nome.replace('_', ' ').title()}' não encontrado(a) ou Patrono desconhecido.")
    
    elif patronos_input == "2":
        result = list(prolog.query("listar_patronos(Nome, Forma)"))
        
        if result:
            for item in result:
                nome = item["Nome"].replace('_', ' ').title()
                forma = item["Forma"].replace('_', ' ').title()
                print(f"- {nome}: {forma}")
            print(f"Total: {len(result)} patronos(as) conhecidos(as).")
        else:
            print("Nenhum Patrono encontrado nos fatos.")
            
    else:
        print("Opção inválida.")
        
    return

def menu_feiticos():
    print("""
    =====MENU DE FEITIÇOS=====
    1 - Listar todos os Feitiços
    2 - Mostrar efeito de um Feitiço
    """) 

    feiticos_input = input("Escolha uma opção: ")
    
    # 1. Listar todos os Feitiços
    if feiticos_input == "1":
        result = list(prolog.query("listar_feiticos(Nome)"))
        
        if result:
            for item in result:                
                nome = item["Nome"].title()
                print(f"- {nome}")
            print(f"Total: {len(result)} feitiços encontrados.")
        else:
            print("Nenhum feitiço encontrado nos fatos.")
            
    # 2. Mostrar efeito de um Feitiço
    elif feiticos_input == "2":
        nome_feitico = input("Digite o nome do feitiço: ").lower().replace(" ", "_")
        
        result = list(prolog.query(f"efeito_feitico({nome_feitico}, Efeito)"))
        if result:
            efeito = result[0]["Efeito"].replace('_', ' ').capitalize()
            print(f"O feitiço {nome_feitico.title().replace('_', ' ')} é o feitiço de {efeito}.")
        else:
            print(f"Feitiço '{nome_feitico.title().replace('_', ' ')}' não encontrado.")
            
    else:
        print("Opção inválida.")
        
    return