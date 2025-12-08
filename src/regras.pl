:- consult('fatos.pl').

detalhes(Nome, Resultado) :-
    personagem(Nome, Casa, Patrono, Sangue),
    swritef(Resultado, 
            'Nome: %w\nCasa: %w\nPatrono: %w\nTipo de sangue: %w', 
            [Nome, Casa, Patrono, Sangue]).

casa_do_personagem(Nome, Casa) :-
    personagem(Nome, Casa, _, _).

buscar_personagem(Busca, Nome) :-
    personagem(Nome, _, _, _),
    sub_atom(Nome, _, _, _, Busca).


listar_casas(Casa) :-
    casa(Casa, _).

detalhes_casa(Casa, Detalhes) :-
    casa(Casa, Atributos),
    swritef(Detalhes, 
            'Atributos principais: %w', 
            [Atributos]).

chefe_da_casa(Casa, Chefe) :-
    chefe_de_casa(Casa, Chefe).


patrono_do_bruxo(Nome, Forma) :-
    patrono(Nome, Forma).

listar_patronos(Nome, Forma) :-
    patrono(Nome, Forma),
    Forma \= desconhecido.


listar_feiticos(Nome) :-
    feitico(Nome, _).

efeito_feitico(Nome, Efeito) :-
    feitico(Nome, Efeito).