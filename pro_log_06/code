% Q30: Towers of Hanoi
hanoi(1, Source, Destination, _) :-
    format('Move disk from ~w to ~w~n', [Source, Destination]).
hanoi(N, Source, Destination, Auxiliary) :-
    N > 1,
    N1 is N - 1,
    hanoi(N1, Source, Auxiliary, Destination),
    format('Move disk from ~w to ~w~n', [Source, Destination]),
    hanoi(N1, Auxiliary, Destination, Source).

% Query: ?- hanoi(3, a, c, b).
% Output: 7 moves, ending with Move disk from a to c.
