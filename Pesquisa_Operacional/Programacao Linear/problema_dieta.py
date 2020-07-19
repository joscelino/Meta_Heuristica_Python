from pulp import LpVariable, LpProblem, LpStatus, LpMinimize, lpSum, value

# Dados do problema
racoes = [0, 1, 2, 3, 4, 5]

custo = {0: 0.74,
         1: 0.70,
         2: 0.83,
         3: 0.81,
         4: 0.73,
         5: 0.75}

minimo = {0: 200, 1: 180, 2: 150}

inf_nutri = [[50, 60, 30, 40, 20, 45],
             [27, 30, 40, 5, 20, 30, 50],
             [50, 80, 60, 30, 20, 40]]

# Criar as variaveis de decisao
var = LpVariable.dict("R", (racoes), lowBound=0)

# Criando Modelo
model = LpProblem("Problema_da_Dieta", LpMinimize)

# Criar a funcao Objetivo
lista_fo = []

for x in var.keys():
    lista_fo.append(var[x] * custo[x])

model += lpSum(lista_fo)

# Criando as restricoes
lista_rest = []


for i in minimo.keys():
    for j in racoes:
        lista_rest.append(var[j] * inf_nutri[i][j])
    model += lpSum(lista_rest) >= minimo[i]
    lista_rest = []


# Solucao do Modelo

status = model.solve()

print(LpStatus[status])
print("")
print(f"O menor custo fica em {value(model.objective)}")

for x in var.values():
    if value(x) > 0:
        print(f'{x} = {value(x)}')
    else:
        continue




