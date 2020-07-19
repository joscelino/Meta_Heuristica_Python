from pulp import LpVariable, LpProblem, LpMinimize, LpStatus,  lpSum, value

# Dados do problema

n_nos = [0, 1, 2, 3, 4]

no_origem = 0

no_destino = 1

grafo = [[0, 1, 1, 0, 0],
         [0, 0, 1, 0, 0],
         [0, 0, 0, 1, 1],
         [0, 1, 0, 0, 1],
         [0, 0, 0, 0, 0]]

custos = [[0, 300, 90, 0, 0],
         [0, 0, 60, 0, 0],
         [0, 0, 0, 30, 180],
         [0, 45, 0, 0, 150],
         [0, 0, 0, 0, 0]]

# Variaveis de decisao

var = {}
for i in n_nos:
    for j in n_nos:
        if grafo[i][j] == 1:
            var[(i, j)] = LpVariable(name=f'x{i}{j}', cat='Binary')
        else:
            continue
    var.update(var)

print(var)

# Criacao do Modelo

model = LpProblem('Problema_menor_caminho', LpMinimize)

# Funcao objetivo
lista_fo = []

for x in var.keys():
    lista_fo.append(var[x]*custos[x[0]][x[1]])

model += lpSum(lista_fo)

# Criacao das restricoes
lista_o = []
lista_f = []

for no in n_nos:
    for aresta in var.keys():

        if aresta[0] == no:
            lista_o.append(var[aresta])

        elif aresta[1] == no:
            lista_f.append(var[aresta])

    if no == no_origem:
        model += lpSum(lista_o) == 1

    elif no == no_destino:
        model += - lpSum(lista_f) == - 1

    else:
        model += lpSum(lista_o) - lpSum(lista_f) == 0

    lista_f = []
    lista_o = []

#print(model)

# Solucao do Modelo
status = model.solve()
print(LpStatus[status])
print(f'O custo minino eh de R$: {value(model.objective)}')
print('---------------------------------------------------')

for x in var.values():
    if value(x) != 0:
        print(f'{x} = {value(x)}')
    else:
        continue
