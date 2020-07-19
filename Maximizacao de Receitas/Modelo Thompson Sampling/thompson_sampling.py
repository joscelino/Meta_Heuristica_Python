# -*- coding: utf-8 -*-
# Estudo de caso - Maximizando a receita de um negocio de varejo on line
import numpy as np
import matplotlib.pyplot as plt 
import random

# Configuracao dos parametros
N = 3250            # usuarios conectados
d = 9               # numero de estrategias
lucro_unit = 19.99

# Criacao da simulacao
convertion_rates = [0.07, 0.13, 0.09, 0.16, 0.11, 0.04, 0.20, 0.08, 0.02]
X = np.array(np.zeros([N, d]))

for i in range(N):
    for j in range(d):
        if np.random.rand() <= convertion_rates[j]:
            X[i,j] = 1

# Implementacao da estrategia randomica e do Thompson Sampling
strategies_selected_rs = [] # Estrategia randomica
strategies_selected_ts = [] # Estrategia Thompson Sampling
total_reward_rs = 0
total_reward_ts = 0
number_of_rewards_1 = [0] * d
number_of_rewards_0 = [0] * d

for n in range(0, N):
    # Estrategia Randomica
    strategy_rs = random.randrange(d)
    strategies_selected_rs.append(strategy_rs)
    reward_rs = X [n, strategy_rs]
    total_reward_rs += reward_rs
    
    # Estrategia Thompson Sampling
    strategy_ts = 0
    max_random = 0
    for i in range(0, d):
        random_beta = random.betavariate(number_of_rewards_1[i] + 1, number_of_rewards_0[i] + 1)
        if random_beta > max_random:
            max_random = random_beta
            strategy_ts = i
    reward_ts = X[n, strategy_ts]
    if reward_ts == 1:
        number_of_rewards_1[strategy_ts]+= 1
    else:
        number_of_rewards_0[strategy_ts] += 1
    strategies_selected_ts.append(strategy_ts)
    total_reward_ts += reward_ts

#print('Estrategias selecionadas: ', strategies_selected_ts)
# Calculo do retorno absoluto e retorno relativo
absolute_return = (total_reward_ts - total_reward_rs)  * lucro_unit
relative_return = (total_reward_ts - total_reward_rs)  / total_reward_rs * 100
print("Absolute return  : R$ {:0f} ".format(absolute_return))   
print("Relative return  : {:0f} %".format(relative_return))       
    
# Grafico com histograma das Selecoes
plt.hist(strategies_selected_rs)
plt.title("Histograma de Selecoes")
plt.xlabel('Strategy')
plt.ylabel('Number of times the strategy was selected.')
plt.show()