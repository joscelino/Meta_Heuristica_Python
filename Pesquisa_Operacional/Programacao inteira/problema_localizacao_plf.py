from pulp import LpVariable, LpProblem, LpMinimize, LpStatus,  lpSum, value

objective_func = LpProblem('Location', LpMinimize)

terminals = {0: 'Terminal_1', 1: 'Terminal_2', 2: 'Terminal_3', 3: 'Terminal_4'}
manufacture = {0: 800, 1: 1200, 2: 650, 3: 1450}
variable_costs = [[40, 15, 20],
                  [10, 12, 25],
                  [30, 17, 27],
                  [10, 12, 20]]

locations = {0: 'Niteroi', 1: 'Angra', 2: 'Campos'}
fixed_costs = {0: 300000, 1: 400000, 2: 490000}
availabilities = {0: 1500, 1: 2600, 2: 3400}

weeks = 52

# Objective Function

var_1 = LpVariable.dict('Cities', locations, cat='Binary')
var_2 = LpVariable.dict("Location", (terminals, locations), lowBound=0, cat='Integer')

objective_list = []

for i in var_1.keys():
    objective_list.append(var_1[i] * fixed_costs[i])

for x in var_2.keys():
    objective_list.append(weeks * (var_2[x] * variable_costs[x[0]][x[1]]))

objective_func += lpSum(objective_list)
# Constrains

# Technological constrains
objective_func += lpSum(var_2[0, 0] + var_2[0, 1] + var_2[0, 2]) == manufacture[0]
objective_func += lpSum(var_2[1, 0] + var_2[1, 1] + var_2[1, 2]) == manufacture[1]
objective_func += lpSum(var_2[2, 0] + var_2[2, 1] + var_2[2, 2]) == manufacture[2]
objective_func += lpSum(var_2[3, 0] + var_2[3, 1] + var_2[3, 2]) == manufacture[3]

# Availabilities constrains
objective_func += lpSum(var_2[0, 0] + var_2[1, 0] + var_2[2, 0] + var_2[3, 0]) <= availabilities[0]
objective_func += lpSum(var_2[0, 1] + var_2[1, 1] + var_2[2, 1] + var_2[3, 1]) <= availabilities[1]
objective_func += lpSum(var_2[0, 2] + var_2[1, 2] + var_2[2, 2] + var_2[3, 2]) <= availabilities[2]

print(objective_func)
status = objective_func.solve()
print(LpStatus[status])

print(f'Costs = R${value(objective_func.objective)}\n')

for x in var_2.values():
    if value(x) != 0:
        print(f'{x} = {value(x)}')














