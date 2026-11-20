% Q35: Fruits and colours using backtracking
fruit(apple).
fruit(banana).
fruit(orange).
fruit(grapes).
fruit(mango).

color(apple, red).
color(banana, yellow).
color(orange, orange).
color(grapes, green).
color(mango, yellow).

fruit_color(Fruit, Color) :-
    fruit(Fruit),
    color(Fruit, Color).

% Queries:
% ?- fruit_color(apple, C).       % C = red.
% ?- fruit_color(F, C).           % Press ; for more answers.
% ?- color(F, yellow).            % F = banana ; F = mango.
