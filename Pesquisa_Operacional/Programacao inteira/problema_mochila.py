from pulp import LpVariable, LpProblem, LpMaximize, LpStatus,  lpSum, value

itens = ['A', 'B', 'C', 'D', 'E', 'F']

capacidade = 20000
peso = {'A': 7000, 'B': 4500, 'C': 8700, 'D': 8000, 'E': 4900, 'F': 7500}
valor = {'A': 36, 'B': 64, 'C': 40, 'D': 45, 'E': 60, 'F': 40}

# Variaveis de Decisao
var = LpVariable.dict("", itens, cat="Binary")

# Criar o Problema
model = LpProblem("Problema_Mochila01", LpMaximize)

# Funcao Objetivo
lista_fo = []

for item in itens:
    lista_fo.append(var[item] * valor[item])

model += lpSum(lista_fo)

# Restricoes
lista_rest = []

for item in itens:
    lista_rest.append(var[item] * peso[item])

model += lpSum(lista_rest) <= capacidade
print(model)

# Solucao do Modelo

status = model.solve()
print(LpStatus[status])
print(f'Valor da funcao objetivo: {value(model.objective)}')
print()


for x in var.values():
    print(f' X = {value(x)}')
