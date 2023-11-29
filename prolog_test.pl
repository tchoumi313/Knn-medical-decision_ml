% Facts for Symptomes
symptome('DIARRHEE').
symptome('CRAMPES ABDOMINALES ET DOULEURS MUSCULAIRES').
symptome('NAUSEES et VOMISSEMENTS').
symptome('FIEVRES LEGERE MAL DE TETE').
symptome('PERTE D''APPETIT et Fatigue').
symptome('Douleurs abdominales').
symptome('Toux').
symptome('Vomissements').
symptome('Éruptions cutanées').
symptome('Une toux persistante (pouvant durer plus de 2 semaines, accompagnée parfois de sang ou de mucosité)').
symptome('Douleurs thoraciques').
symptome('Faiblesses ou fatigue').
symptome('Perte de poids').
symptome('Perte d’appétit').
symptome('Des frissons').
symptome('fièvre').
symptome('Sueurs nocturnes').
symptome('Perte de poids involontaire').
symptome('Fièvre persistante').
symptome('Fatigue extrême').
symptome('Infections opportunistes fréquentes').
symptome('Essoufflement').
symptome('Toux persistante').
symptome('Ulcères buccaux').
symptome('Éruptions cutanées persistantes').
symptome('Maux de tête persistants').
symptome('La Cécité').
symptome('Dermatite Chronique').
symptome('Atteintes articulaire').
symptome('lésions cutanéesNodule cutanées').

% Facts for Maladies
maladie('PALUDISME').
maladie('VARICELLE').
maladie('TYPHOIDE').
maladie('TUBERCULOSE').
maladie('SIDA').
maladie('onchocercose').
maladie('GONORRHEE').

% Facts for Correspondance
correspondance('DIARRHEE', 'PALUDISME').
correspondance('CRAMPES ABDOMINALES ET DOULEURS MUSCULAIRES', 'VARICELLE').
correspondance('NAUSEES et VOMISSEMENTS', 'TYPHOIDE').
correspondance('FIEVRES LEGERE MAL DE TETE', 'TUBERCULOSE').
correspondance('PERTE D''APPETIT et Fatigue', 'SIDA').
correspondance('Douleurs abdominales', 'onchocercose').
correspondance('Toux', 'GONORRHEE').
correspondance('Vomissements', 'PALUDISME').
% ... (add other correspondences)

% Query method
proposer_diagnostic(Symptomes, Diagnostic) :-
    member(Symptome, Symptomes),
    correspondance(Symptome, Diagnostic).

% Rules for proposing a diagnostic
proposer_diagnostic2(Symptomes, DiagnosticPropose) :-
    findall(Maladie, (member(Symptome, Symptomes), correspondance(Symptome, Maladie)), MaladiesPossibles),
    list_to_set(MaladiesPossibles, MaladiesUniques),
    length(MaladiesUniques, NumMaladies),
    NumMaladies = 1, % Ensure there is a unique potential disease
    member(DiagnosticPropose, MaladiesUniques),
    print(5).

% Rules for proposinMaladieg potential diseases
% Rules for proposing potential diseases
proposer_diagnostic3(Symptomes) :-
    findall(Maladie, (member(Symptome, Symptomes), correspondance(Symptome, Maladie)), MaladiesPossibles),
    list_to_set(MaladiesPossibles, MaladiesUniques),
    length(MaladiesUniques, NumMaladies),
    NumMaladies > 0, % Ensure there is at least one potential disease
    writeln('Potential Diseases:'),
    print_potential_diseases(MaladiesUniques).

% Helper predicate to print potential diseases
print_potential_diseases([]).
print_potential_diseases([Disease | Rest]) :-
    write(Disease), nl,
    print_potential_diseases(Rest).
