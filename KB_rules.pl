/* 
these represent the rules to find the facts in the predicate set:

    p -> q
    l AND m -> p
    l AND p -> m
    a AND b -> l
    a AND p -> l

    fact(a)
    fact(b)

q is our goal (conclusion)
*/

is_true(P) :- fact(P).
is_true(P) :- is_true(Condition), is_true(P)
is_true(P1 and P2) :- is_true(P1), is_true(P2).
is_true(P1 or P2) :- is_true(P1); is_true(P2).

/* Defining if, then, and, or which currently do not exist in prolog*/
:- op(800, fx, if).
:- op(700, xfx, then).
:- op(600, xfy, and).
:- op(600, xfy, or).


% Reasoning WHY and HOW
how(P) :-
    fact(P),
    write(P), write(' is a fact '), nl.

how(P) :-
    if Condition then P,
    write(P), write(' because '), write(Condition), nl,
    how(Condition).

why(P) :-
      fact(P),
      write(P), write(' is a known fact'), nl.

  why(P) :-
      if Condition then P,
      write('To prove '), write(P),
      write(' we need '), write(Condition), nl,
      why(Condition).


/* ------- Knowledge Base ----------*/
% Facts
fact(hallway_wet).
fact(bathroom_dry).
fact(window_closed).
% Rules
if hallway_wet and bathroom_dry then leak_bathroom.
if hallway_wet and bathroom_dry then problem_kitchen.
if window_closed or no_rain then no_water_outside.
if problem_kitchen and no_water_outside then leak_in_kitchen.