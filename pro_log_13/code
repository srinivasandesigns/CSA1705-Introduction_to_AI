% Q38: Forward chaining
:- dynamic known/1.

% Rules: if the first item is known, the second can be derived.
rule(a, b).
rule(b, c).
rule(c, d).

% Initial fact
known(a).

% Derive facts repeatedly until no new fact can be added.
forward :-
    rule(X, Y),
    known(X),
    \\+ known(Y),
    !,
    assertz(known(Y)),
    forward.
forward.

% Queries:
% ?- forward.
% true.
% ?- known(X).  % a ; b ; c ; d
%
% To reset before running again:
% ?- retractall(known(_)), assertz(known(a)), forward.
