is_a(bird, animal).
is_a(giraffe, animal).
is_a(chicken, bird).
moving_method(bird, fly).


one_fact(Fact) :-
    Fact, !.    % Checks whether Arguament is proovable

all_facts(Fact) :-
    Fact.   

fact(Fact) :-
    Fact =.. [Rel, Arg1, Arg2], % Current node's Fact as a functor
    is_a(Arg1, ParentArg),  % Checks whether current node has a parent
    ParentFact =.. [Rel, ParentArg, Arg2], % Parent node's fact using the child nodes Arg2
    fact(ParentFact).   % Checks whether Parent's functor is a fact




animal(bird).
bird(chicken).
moving_method(bird, fly).




