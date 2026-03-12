:- dynamic prerequisite/2.

career(software_engineer) :-
    prerequisite(programming, high),
    prerequisite(interest, coding).

career(data_analyst) :-
    prerequisite(statistics, high),
    prerequisite(mathematics, high),
    prerequisite(interest, data).

career(ui_ux_designer) :-
    (prerequisite(design, high); prerequisite(design, medium)),
    (prerequisite(creativity, high); prerequisite(creativity, medium)),
    prerequisite(interest, design).