# -*- coding: utf-8 -*-
"""
Otimizacao de Carteiras de Investimentos por Pesquisa Operacional Metodo Simplex
Restricoes :
    - Nao se pode ter investimento superior a 35% em um unico ativo
    - Nao se pode ter valor menor que zero para ativos
    - Retorno esperado deve ser maior ou igual ao estipulado
"""
# Importacao das bibliotecas
import numpy as np
from scipy.optimize import linprog

retornos = [0.0037, 0.0024, 0.0014, 0.0030, 0.0024, 0.0019, 0.0028, 0.0018, 0.0025, 0.0024]
volatidades = [0.0248, 0.0216, 0.0195, 0.0293, 0.024, 0.0200, 0.0263, 0.0214, 0.0273, 0.0247]
retorno_medio = np.array([retornos]).mean()
risco_medio = np.array([volatidades]).mean()
risco_tolerado = risco_medio*0.95
risco_maximo = [risco_tolerado]
n_ativos = len(retornos)
invest_max_individual = 0.35

# Retornos dos ativos
c = retornos
c = np.multiply(-1.0, c)

A_eq = np.ones((1, n_ativos)) # condicao de igualdade
b_eq = np.array([1.0]) # condicao de desigualdade

# Para as inequacoes
A_ub = np.append(np.eye(n_ativos), -1*np.eye(n_ativos), axis=0) 
b_ub = np.append(invest_max_individual*np.ones((n_ativos,)), np.zeros((n_ativos,)), axis=0) 

# Verificando
A_ub

# Riscos unitarios da carteira
A_ub = np.append(A_ub, [volatidades], axis=0)
b_ub = np.append(b_ub, risco_maximo)

# Nova verificacao
A_ub

# Otimizacao da carteira
res = linprog(c, A_eq=A_eq, b_eq=b_eq, A_ub=A_ub, b_ub=b_ub, method='simplex', options={'disp': True, 'maxiter': 1000})
retorno_otimo = -res.fun

print("Valor Otimo: ",-res.fun)
print("X: ")

# Listando 
for k, xk in enumerate(res.x):
    print("x_{", str(k+1), "} =", xk)
