from pulp import LpVariable, LpProblem, LpMinimize, LpStatus,  lpSum, value

# Dados do problema

maquinas = [0, 1, 2]

custo_fixo = {0: 25, 1: 45, 2: 60}

custo_variavel = {0: 4, 1: 7, 2: 12}

capacidade = {0: 30, 1: 60, 2: 78}

# Variaveis de decisao

var = LpVariable.dict("x", (maquinas), cat="Integer", lowBound=0)
var2 = LpVariable.dict("y", (maquinas), cat="Binary")

# Criacao do Modelo

model = LpProblem("Problema_carga_fixa", LpMinimize)

# Criacao da funcao objetivo

lista_fo = []

for m in maquinas:
    lista_fo.append(var[m] * custo_variavel[m] + var2[m] * custo_fixo[m])

model += lpSum(lista_fo)
print(model)

# Criacao das restricoes

for m in maquinas:
    model += var[m] <= capacidade[m] * var2[m]

lista_rest = []

for x in var.values():
    lista_rest.append(x)

model += lpSum(lista_rest) == 75

print(model)

# Solucao do Modelo

status = model.solve()
analise = LpStatus[status]
print()
print(f'O custo {analise} eh de: R$ {value(model.objective)}.')

print()
print("Quantidades a serem produzidas)
for m in maquinas:
    print(f'{var[m]}: {value(var[m])}')
    print(f'{var2[m]}: {value(var2[m])}')