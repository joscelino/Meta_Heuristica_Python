from pulp import LpVariable, LpProblem, LpMaximize, LpStatus, value

prob = LpProblem("dual_problem.py", LpMaximize)

x1 = LpVariable("Prod_1", 0, cat='Integer')
x2 = LpVariable("Prod_2", 0, cat='Integer')
profit_x1 = 5
profit_x2 = 6
products = [x1, x2]
resources = [0, 1, 2]
capabilities = [14, 9, 56]
costs = [[1, 1, 7],
         [2, 1, 4]]

# Objective Function
prob += profit_x1 * x1 + profit_x2 * x2

# Constrains
prob += costs[0][0] * x1 + costs[1][0] * x2 <= capabilities[0]
prob += costs[0][1] * x1 + costs[1][1] * x2 <= capabilities[1]
prob += costs[0][2] * x1 + costs[1][2] * x2 <= capabilities[2]
prob += capabilities[0] + capabilities[1] + capabilities[2] <= sum(capabilities)
prob += costs[0][0] * capabilities[0] + costs[0][1] * capabilities[1] + costs[0][2] * capabilities[2] >= profit_x1
prob += costs[1][0] * capabilities[0] + costs[1][1] * capabilities[1] + costs[1][2] * capabilities[2] >= profit_x2

prob.writeLP('dual_problem.py')

print(prob)
print('Solution')
print("----------------------------------------")

# Solution
prob.solve()

status = LpStatus[prob.status]

# Variable solutions
for variable in prob.variables():
    print(f'{variable.name} = {variable.varValue}')

# Optimized goal
print(f'Total production margin - R$: {value(prob.objective)}')
