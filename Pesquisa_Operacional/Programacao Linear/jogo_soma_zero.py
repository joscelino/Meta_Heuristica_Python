from pulp import LpVariable, LpProblem, LpMaximize, lpSum, LpStatus, value

# Dados do Problema

retornos = [[30, -10, -30],
            [0, -40, 10],
            [-50, 60, 0]]

estrategia_a = [0, 1, 2]
estrategia_b = [0, 1, 2]

# Criacao das variaveis de decisao

var = LpVariable.dict("A", (estrategia_a), lowBound=0)
v = LpVariable('v')

# Criacao do modelo

model = LpProblem("Jogo_soma_ZERO", LpMaximize)

# Criacao da funcao Objetivo

model += v

# Criacao das restricoes

lista_rest = []

for j in estrategia_b:
    for i in estrategia_a:
        lista_rest.append(var[i] * retornos[i][j])
    model += v - lpSum(lista_rest) == 0
    lista_rest = []

for x in var.values():
    lista_rest.append(x)

model += lpSum(lista_rest) == 1

# Solucao do modelo
status = model.solve()
print(LpStatus[status])
print(f'O resultado sera {value(model.objective)}')

for x in var.values():
    print(f'{x} = {value(x)}')