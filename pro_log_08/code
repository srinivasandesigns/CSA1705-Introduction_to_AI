% Q33: Diet suggestion based on disease
diet(diabetes, 'Low sugar food').
diet(obesity, 'Low calorie food').
diet(anemia, 'Iron rich food').
diet(blood_pressure, 'Low salt food').
diet(heart_disease, 'Low fat food').
diet(weakness, 'Protein rich food').

suggest_diet(Disease, Food) :-
    diet(Disease, Food).

% Queries:
% ?- suggest_diet(diabetes, Food).
% Food = 'Low sugar food'.
% ?- suggest_diet(anemia, Food).
% Food = 'Iron rich food'.
%
% Educational example only; not medical advice.
