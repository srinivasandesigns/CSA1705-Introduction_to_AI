% Q29: Planets database
planet(mercury, 1).
planet(venus, 2).
planet(earth, 3).
planet(mars, 4).
planet(jupiter, 5).
planet(saturn, 6).
planet(uranus, 7).
planet(neptune, 8).

planet_position(Name, Position) :-
    planet(Name, Position).

is_planet(Name) :-
    planet(Name, _).

% Queries:
% ?- planet_position(earth, P).  % P = 3.
% ?- is_planet(mars).            % true.
% ?- planet(Name, Position).    % Press ; for next planet.
