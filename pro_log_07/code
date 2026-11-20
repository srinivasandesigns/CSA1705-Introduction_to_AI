% Q32: Family tree
% Gender facts
female(pam).
female(liz).
female(ann).

male(tom).
male(bob).
male(jim).

% Example parent relationships (the question gives genders only)
parent(tom, liz).
parent(pam, liz).
parent(tom, bob).
parent(pam, bob).
parent(bob, ann).
parent(liz, jim).

mother(X, Y) :-
    female(X),
    parent(X, Y).

father(X, Y) :-
    male(X),
    parent(X, Y).

grandfather(X, Y) :-
    male(X),
    parent(X, Z),
    parent(Z, Y).

grandmother(X, Y) :-
    female(X),
    parent(X, Z),
    parent(Z, Y).

sister(X, Y) :-
    female(X),
    parent(Z, X),
    parent(Z, Y),
    X \= Y.

brother(X, Y) :-
    male(X),
    parent(Z, X),
    parent(Z, Y),
    X \= Y.

% Queries:
% ?- mother(X, liz).       % X = pam.
% ?- father(X, bob).       % X = tom.
% ?- grandfather(X, ann).  % X = tom.
% ?- grandmother(X, ann). % X = pam.
% ?- sister(X, bob).       % X = liz.
% ?- brother(X, liz).      % X = bob.
