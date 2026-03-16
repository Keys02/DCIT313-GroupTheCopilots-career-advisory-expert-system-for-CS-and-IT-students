:- dynamic prerequisite/2.

% --------------------------
% Career scoring rules
% --------------------------

career_score(software_engineer, Score) :-
    score_programming(P),
    score_mathematics(M),
    score_interest_coding(I),
    Score is P + M + I.

career_score(data_analyst, Score) :-
    score_statistics(S),
    score_mathematics(M),
    score_interest_data(I),
    Score is S + M + I.

career_score(ui_ux_designer, Score) :-
    score_design(D),
    score_creativity(C),
    score_interest_design(I),
    Score is D + C + I.

career_score(digital_marketer, Score) :-
    score_communication(C),
    score_creativity(CR),
    score_interest_marketing(I),
    Score is C + CR + I.

career_score(machine_learning_engineer, Score) :-
    score_programming(P),
    score_mathematics(M),
    score_statistics(S),
    score_interest_data(I),
    Score is P + M + S + I.

career_score(cybersecurity_analyst, Score) :-
    score_networking(N),
    score_programming(P),
    score_interest_security(I),
    Score is N + P + I.

career_score(network_engineer, Score) :-
    score_networking(N),
    score_mathematics(M),
    score_interest_networks(I),
    Score is N + M + I.

career_score(game_developer, Score) :-
    score_programming(P),
    score_creativity(C),
    score_mathematics(M),
    score_interest_coding(I),
    Score is P + C + M + I.

career_score(product_designer, Score) :-
    score_design(D),
    score_creativity(C),
    score_communication(COM),
    score_interest_design(I),
    Score is D + C + COM + I.

career_score(technical_writer, Score) :-
    score_communication(C),
    score_creativity(CR),
    Score is C + CR.

% --------------------------
% Skill scoring
% --------------------------

score_programming(40) :- prerequisite(programming, high), !.
score_programming(25) :- prerequisite(programming, medium), !.
score_programming(10) :- prerequisite(programming, low), !.
score_programming(0).

score_mathematics(30) :- prerequisite(mathematics, high), !.
score_mathematics(20) :- prerequisite(mathematics, medium), !.
score_mathematics(10) :- prerequisite(mathematics, low), !.
score_mathematics(0).

score_statistics(40) :- prerequisite(statistics, high), !.
score_statistics(25) :- prerequisite(statistics, medium), !.
score_statistics(10) :- prerequisite(statistics, low), !.
score_statistics(0).

score_design(30) :- prerequisite(design, high), !.
score_design(20) :- prerequisite(design, medium), !.
score_design(10) :- prerequisite(design, low), !.
score_design(0).

score_creativity(30) :- prerequisite(creativity, high), !.
score_creativity(20) :- prerequisite(creativity, medium), !.
score_creativity(10) :- prerequisite(creativity, low), !.
score_creativity(0).

score_communication(30) :- prerequisite(communication, high), !.
score_communication(20) :- prerequisite(communication, medium), !.
score_communication(10) :- prerequisite(communication, low), !.
score_communication(0).

score_networking(40) :- prerequisite(networking, high), !.
score_networking(25) :- prerequisite(networking, medium), !.
score_networking(10) :- prerequisite(networking, low), !.
score_networking(0).

% --------------------------
% Interest scoring
% --------------------------

score_interest_coding(30) :- prerequisite(interest, coding), !.
score_interest_coding(0).

score_interest_data(30) :- prerequisite(interest, data), !.
score_interest_data(0).

score_interest_design(30) :- prerequisite(interest, design), !.
score_interest_design(0).

score_interest_marketing(30) :- prerequisite(interest, marketing), !.
score_interest_marketing(0).

score_interest_security(30) :- prerequisite(interest, security), !.
score_interest_security(0).

score_interest_networks(30) :- prerequisite(interest, networks), !.
score_interest_networks(0).

% --------------------------
% Reasons
% --------------------------

reason(software_engineer,
"Recommended because you have programming skills and mathematical ability with an interest in software development.").

reason(data_analyst,
"Recommended because you demonstrate strong statistics and mathematics skills with interest in analyzing data.").

reason(ui_ux_designer,
"Recommended because you show design ability, creativity and interest in building user-friendly interfaces.").

reason(digital_marketer,
"Recommended because you demonstrate communication skills, creativity and interest in digital marketing.").

reason(cybersecurity_analyst,
"Recommended because you show networking and programming ability with interest in protecting systems and information.").

reason(game_developer,
"Recommended because you combine programming, creativity and mathematics with interest in game development.").

reason(product_designer,
"Recommended because you demonstrate design, creativity and communication skills suited for designing digital products.").

reason(technical_writer,
"Recommended because you have strong communication and creativity skills useful for explaining technical concepts clearly.").