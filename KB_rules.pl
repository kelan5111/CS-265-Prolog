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
is_true(P) :- if Condition then P, is_true(Condition).
is_true(P1 and P2) :- is_true(P1), is_true(P2).
is_true(P1 or P2) :- is_true(P1); is_true(P2).


/* ------- Knowledge Base ----------*/


