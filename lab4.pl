p(1).
p(2) :- !.
p(3).

class(Number, positive):- Number > 0, !.
class(0, zero):- !.
class(Number, negative):- Number < 0.

split([], [], []).

split([H|T], [H|PT], NL):-
    class(H, positive),
    split(T, PT, NL).

split([H|T], [H|PT], NL):-
    class(H, zero),
    split(T, PT, NL).

split([H|T], PL, [H|NT]):-
    class(H, negative),
    split(T, PL, NT).