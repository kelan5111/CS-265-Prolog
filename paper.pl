country(X) :- usa(X).
country(X) :- italy(X).
country(X) :- vietnam(X).
country(X) :- kenya(X).
usa(a).
italy(b).
vietnam(c).
kenya(d).

plansToVisit(jane, X) :- country(X), \+ usa(X).
drives(vincent, X) :- \+ usa(X), country(X).



