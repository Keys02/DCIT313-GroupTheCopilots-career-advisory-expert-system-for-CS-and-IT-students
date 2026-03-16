:- dynamic prerequisite/2.

career(software_engineer) :-
    prerequisite(programming, high),
    (prerequisite(mathematics, medium); prerequisite(mathematics, high)),
    prerequisite(interest, coding).

career(data_analyst) :-
    prerequisite(statistics, high),
    prerequisite(mathematics, high),
    prerequisite(interest, data).

career(ui_ux_designer) :-
    (prerequisite(design, high); prerequisite(design, medium)),
    (prerequisite(creativity, high); prerequisite(creativity, medium)),
    prerequisite(interest, design).

career(digital_marketer) :-
    (prerequisite(communication, high); prerequisite(communication, medium)),
    (prerequisite(creativity, high); prerequisite(creativity, medium)),
    prerequisite(interest, marketing).


/* Explanation rules */

reason(software_engineer,
"Recommended because you have strong programming skills, sufficient mathematical ability, and a strong interest in coding and software development.").

reason(data_analyst,
"Recommended because you demonstrate strong statistics and mathematical skills along with an interest in analyzing and interpreting data.").

reason(ui_ux_designer,
"Recommended because you show good design ability, creativity, and an interest in creating visually appealing and user-friendly digital experiences.").

reason(digital_marketer,
"Recommended because you possess communication skills, creativity, and an interest in marketing and promoting products or services through digital platforms.").