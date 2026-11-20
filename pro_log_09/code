% Q34: Monkey and Banana problem (simple state-space solution)
% state(MonkeyPosition, BoxPosition, MonkeyStatus, HasBanana)
initial_state(state(door, middle, floor, no)).

% The monkey pushes the box from the middle to the window.
action(state(door, middle, floor, no),
       push_box,
       state(window, window, floor, no)).

% The monkey climbs onto the box.
action(state(window, window, floor, no),
       climb,
       state(window, window, on_box, no)).

% The monkey grabs the banana.
action(state(window, window, on_box, no),
       grab_banana,
       state(window, window, on_box, yes)).

solve_monkey :-
    initial_state(S0),
    action(S0, A1, S1),
    action(S1, A2, S2),
    action(S2, A3, S3),
    write('Actions: '), nl,
    write(A1), nl,
    write(A2), nl,
    write(A3), nl,
    S3 = state(_, _, _, yes),
    write('Monkey gets the banana.').

% Query: ?- solve_monkey.
