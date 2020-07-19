\* dual_problem.py *\
Maximize
OBJ: 3 chocolate_cake + cream_cake
Subject To
_C1: 2 chocolate_cake + 3 cream_cake <= 180
_C2: cream_cake <= 40
_C3: chocolate_cake <= 60
_C4: chocolate_cake >= 10
_C5: chocolate_cake + cream_cake >= 20
_C6: cream_cake >= 0
Bounds
0 <= chocolate_cake
0 <= cream_cake
Generals
chocolate_cake
cream_cake
End
