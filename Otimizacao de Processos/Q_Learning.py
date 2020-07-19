# -*- coding: utf-8 -*-
# Otimizando fluxos do armazem com Q-Learning
import numpy as np

# Configuracao dos parametros gamma e alpha para o Q-Learning (Equacao de Bellman)
gamma = 0.75
alpha = 0.90
n_iteracoes = 1500

# DEFINICAO DO AMBIENTE
location_to_state = {'A': 0,
                     'B': 1,
                     'C': 2,
                     'D': 3,
                     'E': 4,
                     'F': 5,
                     'G': 6,
                     'H': 7,
                     'I': 8,
                     'J': 9,
                     'K': 10,
                     'L': 11}

actions = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# matriz de recompensas
R = np.array([[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
              [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
              [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
              [0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0],
              [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1],
              [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
              [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0]])

# CONSTRUCAO DA SOLUCAO DE IA COM Q-LEARNING
# inicializacao dos valores Q do algoritmo

state_to_location = {state: location for location, state in location_to_state.items()}


def route(starting_location, ending_location):
    R_new = np.copy(R)
    ending_state = location_to_state[ending_location]
    R_new[ending_state, ending_state] = n_iteracoes  # Define prioridade 0 da rota
    Q = np.array(np.zeros([len(actions), len(actions)]))

    for i in range(n_iteracoes):
        current_state = np.random.randint(0, len(actions))
        playable_actions = []
        for j in range(len(actions)):
            if R_new[current_state, j] > 0:
                playable_actions.append(j)
        next_state = np.random.choice(playable_actions)

        # Calculando a diferenca temporal (TD)
        TD = R_new[current_state, next_state] + gamma * Q[next_state, np.argmax(Q[next_state,])] - Q[
            current_state, next_state]

        # Atualizando o valor de Q utilizando a equacao de Bellman
        Q[current_state, next_state] = Q[current_state, next_state] + alpha * TD

    route = [starting_location]
    next_location = starting_location
    while (next_location != ending_location):
        starting_state = location_to_state[starting_location]
        next_state = np.argmax(Q[starting_state])
        next_location = state_to_location[next_state]
        route.append(next_location)
        starting_location = next_location
    return route


# IMPRESSAO DA ROTA FINAL
print('Rota: ')
print(route('E', 'H'))


# Adicionando rota intermediaria
def best_route(starting_location, intermediary_location, ending_location):
    return route(starting_location, intermediary_location) + route(intermediary_location, ending_location)


best_route('A', 'L', 'D')
