:- dynamic prerequisite/2.

career(software_engineer) :-
    prerequisite(programming, high),
    prerequisite(interest, coding).