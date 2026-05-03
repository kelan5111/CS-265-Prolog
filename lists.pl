a2b([], []).
a2b([a | Ta], [b | Tb]) :- a2b(Ta, Tb).

combine([], [], []).
combine([A | Ta], [B | Tb], [A, B | T]) :-
    combine(Ta, Tb, T).