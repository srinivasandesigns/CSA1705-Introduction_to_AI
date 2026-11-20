% Q36: Best First Search
% Graph edges
edge(a, b).
edge(a, c).
edge(b, d).
edge(b, e).
edge(c, f).
edge(c, g).
edge(d, h).
edge(e, h).
edge(f, h).
edge(g, h).

% Heuristic values (smaller is considered better)
heuristic(a, 7).
heuristic(b, 6).
heuristic(c, 4).
heuristic(d, 5).
heuristic(e, 3).
heuristic(f, 2).
heuristic(g, 3).
heuristic(h, 0).

best_first(Start, Goal, Path) :-
    heuristic(Start, H),
    best_search([H-[Start]], Goal, [], ReversePath),
    reverse(ReversePath, Path).

best_search([_-[Goal|Rest]|_], Goal, _, [Goal|Rest]).

best_search([_-[Node|Rest]|Open], Goal, Visited, Path) :-
    findall(H-[Next,Node|Rest],
            ( edge(Node, Next),
              \\+ member(Next, [Node|Rest]),
              \\+ member(Next, Visited),
              heuristic(Next, H)
            ),
            Children),
    append(Open, Children, Combined),
    keysort(Combined, Sorted),
    best_search(Sorted, Goal, [Node|Visited], Path).

% Query: ?- best_first(a, h, Path).
% One valid result: Path = [a, c, f, h].
