% Q37: Simple rule-based medical diagnosis example
symptom(john, fever).
symptom(john, cough).
symptom(alex, headache).
symptom(alex, fever).
symptom(peter, sneezing).
symptom(peter, runny_nose).
symptom(mary, fever).
symptom(mary, body_pain).

disease(Person, flu) :-
    symptom(Person, fever),
    symptom(Person, cough).

disease(Person, common_cold) :-
    symptom(Person, sneezing),
    symptom(Person, runny_nose).

disease(Person, viral_fever) :-
    symptom(Person, fever),
    symptom(Person, body_pain).

diagnose(Person) :-
    disease(Person, Disease),
    format('Patient: ~w~nPossible condition: ~w~n', [Person, Disease]).

% Queries:
% ?- diagnose(john).
% ?- disease(peter, Disease).
% Educational example only; not a real diagnosis.
