from pulp import LpVariable, LpProblem, LpMinimize, LpStatus,  lpSum, value

# Variaveis do Problema
times = [0, 1, 2, 3, 4]
obras = [0, 1, 2, 3, 4]

custos = [[33, 22, 40, 21, 43],
          [33, 40, 26, 17, 36],
          [34, 38, 42, 29, 39],
          [36, 30, 21, 36, 40],
          [28, 45, 31, 42, 19]]

# Variaveis de Decisao
var = LpVariable.dict("x", (times, obras), cat='Binary')

# criar problema
model =  LpProblem('Problema_designacao', LpMinimize)

# Criar funcao objetivo
lista_fo = []

for x in var.keys():
    lista_fo.append(var[x] * custos[x[0]][x[1]])

model += lpSum(lista_fo)
print(model)

# Restricoes

lista_rest = []

for time in times:
    for obra in obras:
        lista_rest.append(var[(time, obra)])
    model += lpSum(lista_rest) == 1
    lista_rest = []

for obra in obras:
    for time in times:
        lista_rest.append(var[(time, obra)])
    model += lpSum(lista_rest) == 1
    lista_rest = []


# Solucao do Modelo
status = model.solve()
print(LpStatus[status])
print(f'O valor da funcao objetivo eh R$: {value(model.objective)}')

for x in var.values():
    if value(x) == 1:
        print(f'{x} = {value(x)}')
    else:
        continue