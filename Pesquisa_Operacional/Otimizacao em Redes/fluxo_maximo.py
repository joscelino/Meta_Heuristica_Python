from pulp import LpVariable, LpProblem, LpMaximize, LpStatus,  lpSum, value

# Dados do problema

nos = [0, 1, 2, 3, 4]

no_origem = 0

no_destino = 4

grafo = [[0, 1, 1, 1, 0],
         [0, 0, 1, 0, 1],
         [0, 0, 0, 1, 1],
         [0, 0, 1, 0, 1],
         [0, 0, 0, 0, 0]]

capacidade = [[0, 200, 300, 100, 0],
            [0, 0, 400, 0, 300],
            [0, 0, 0, 100, 200],
            [0, 0, 50, 0, 200],
            [0, 0, 0, 0, 0]]

# Variaveis de decisao

var = {}

for i in nos:
    for j in nos:
        if grafo[i][j] == 1:
            var[(i,j)] = LpVariable(name=f'x{i}{j}', lowBound=0, cat='Integer')
        else:
            continue
    var.update(var)

# Criacao do Modelo

model = LpProblem('Problema_fluxo_maximo', LpMaximize)

# Funcao objetivo
lista_fo = []

for x in var.keys():
    if x[0] == no_origem:
        lista_fo.append(var[x])

model += lpSum(lista_fo)

# Criacao das restricoes
lista_o = []
lista_d = []

for no in nos:
    for x in var.keys():

        if no == x[0]:
            lista_o.append(var[x])

        elif no == x[1]:
            lista_d.append(var[x])

        else:
            continue

    if no == no_origem or no == no_destino:
        None

    else:
        model += lpSum(lista_o) - lpSum(lista_d) == 0

    lista_o = []
    lista_d = []

for x in var.keys():
    model += var[x] <= capacidade[x[0]][x[1]]

#print(model)

# Solucao do Modelo
status = model.solve()
print(LpStatus[status])
print('---------------------------------------------------')
print(f'A quantidade total eh de: {value(model.objective)}')
print('---------------------------------------------------\n')

for x in var.values():
    print(f'{x} = {value(x)}')

