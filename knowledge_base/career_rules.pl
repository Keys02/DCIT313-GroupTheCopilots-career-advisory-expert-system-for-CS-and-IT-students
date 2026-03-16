:- dynamic prerequisite/2.

% --------------------------
% Career scoring rules
% --------------------------
career_score(software_engineer, Score) :-
    score_programming(ProgScore),
    score_mathematics(MathScore),
    score_interest_coding(InterestScore),
    Score is ProgScore + MathScore + InterestScore.

career_score(data_analyst, Score) :-
    score_statistics(StatsScore),
    score_mathematics(MathScore),
    score_interest_data(InterestScore),
    Score is StatsScore + MathScore + InterestScore.

career_score(ui_ux_designer, Score) :-
    score_design(DesignScore),
    score_creativity(CreativeScore),
    score_interest_design(InterestScore),
    Score is DesignScore + CreativeScore + InterestScore.

career_score(digital_marketer, Score) :-
    score_communication(CommScore),
    score_creativity(CreativeScore),
    score_interest_marketing(InterestScore),
    Score is CommScore + CreativeScore + InterestScore.

% -------------------------------
% Scoring components for skills
% -------------------------------
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

% -----------------------------------
% Scoring components for interests
% -----------------------------------
score_interest_coding(30) :- prerequisite(interest, coding), !.
score_interest_coding(0).

score_interest_data(30) :- prerequisite(interest, data), !.
score_interest_data(0).

score_interest_design(30) :- prerequisite(interest, design), !.
score_interest_design(0).

score_interest_marketing(30) :- prerequisite(interest, marketing), !.
score_interest_marketing(0).

% --------------------------
% Reason rules
% --------------------------
reason(software_engineer,
"Recommended because you have programming skills, some mathematical ability, and an interest in coding and software development.").

reason(data_analyst,
"Recommended because you have statistics and mathematical skills along with an interest in analyzing and interpreting data.").

reason(ui_ux_designer,
"Recommended because you show design ability, creativity, and an interest in creating visually appealing and user-friendly digital experiences.").

reason(digital_marketer,
"Recommended because you have communication skills, creativity, and an interest in marketing and promoting products through digital platforms.").