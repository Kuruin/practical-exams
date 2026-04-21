% Facts

flower(rose).
thorny(rose).
color(rose, red).

flower(sunflower).
color(sunflower, yellow).

flower(lotus).
habitat(lotus, water).

fruit(mango).
leaf(mango, green).

thorny(cactus).
habitat(cactus, desert).


% Rules

plant(X) :-
    flower(X),
    thorny(X),
    color(X, red).

plant(X) :-
    flower(X),
    color(X, yellow).

plant(X) :-
    flower(X),
    habitat(X, water).

plant(X) :-
    fruit(X),
    leaf(X, green).

plant(X) :-
    thorny(X),
    habitat(X, desert).
