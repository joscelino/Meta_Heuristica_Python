"""
Lucro bolo chocolate = 3 u.m.
Lucro bolo creme = 1 u.m.
Contratos = 10 bolos de chocolate/dia
Producao >= 20 bolos/dia
Demanda creme = 40 bolos creme/dia e 60 bolos chocolate dia
Capacidade mquinas = 180 horas
Horas-maquina creme = 3
Horas-maquina chocoloate = 2
"""
from pulp import LpVariable, LpProblem, LpMaximize, LpStatus, value

prob = LpProblem("dual_problem.py", LpMaximize)

x1 = LpVariable("cream_cake", lowBound=0, cat='Integer')
x2 = LpVariable("chocolate_cake", lowBound=0, cat='Integer')
profit_x1 = 1
profit_x2 = 3
chocolate_deal = 10
production_min = 20
demand = [40, 60]
capabilities = 180
costs = [3, 2]

# Objective Function
prob += profit_x1 * x1 + profit_x2 * x2

# Constrains
prob += costs[0] * x1 + costs[1] * x2 <= capabilities
prob += x1 <= demand[0]
prob += x2 <= demand[1]
prob += x2 >= chocolate_deal
prob += x1 + x2 >= production_min
prob += x1 >= 0

prob.writeLP('dual_problem.py')

print(prob)

# Solution
prob.solve()

status = LpStatus[prob.status]
print(f'Solution')
print("----------------------------------------")

# Variable solutions
for variable in prob.variables():
    print(f'{variable.name} = {variable.varValue}')

# Optimized goal
print(f'Profit {status} - R$: {value(prob.objective)}')