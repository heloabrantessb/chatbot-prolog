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