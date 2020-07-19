from pulp import LpVariable, LpProblem, LpMaximize, LpStatus, value, lpSum

"""
Operational Research for allocation of Nexoos investments
"""

available_capital = 3000
investment = ['C2', 'C3', 'B6', 'B4']
min_invest = 1000
max_invest = 2000

interest = {'C2': 0.02235,
            'C3': 0.02360,
            'B6': 0.01808,
            'B4': 0.01642}

risk = {'C2': 0.04,
        'C3': 0.03,
        'B6': 0.02,
        'B4': 0.017}

# Decision variables
var = LpVariable.dict('Investment',  investment, lowBound=min_invest, upBound=max_invest)
#print(var)

model = LpProblem("Loan_allocation", LpMaximize)

# Objective Function
lista_fo = []

for x in var.keys():
    lista_fo.append(interest[x] * (1 - risk[x]) * var[x])

model += lpSum(lista_fo)    

# Constrains
lista_rest = []

for x in var.values():
    lista_rest.append(x)

model += lpSum(lista_rest) <= available_capital
print(model)

# Model Solution
status = model.solve()
print(LpStatus[status])

print(f'Estimated profit - R$  {value(model.objective)}')
print(" ")

for x in var.values():
    print(f'{x} = {value(x)} ')
