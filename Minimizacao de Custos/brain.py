# -*- coding: utf-8 -*-
from keras.layers import Input, Dense
from keras.models import Model
from keras.optimizers import Adam

# CONSTRUCAO DA REDE NEURAL
class Brain(object):
    
    # CONSTRUCAO DA ARQUITETURA DA REDE NEURAL DENSA DENTRO DO METODO INIT
    def __init__(self, learning_rate = 0.001, number_actions = 5):
        self.learning_rate = learning_rate
        
        # CRIACAO DA CAMADA DE ENTRADA COMPOSTA PELO INPUT STATE
        states = Input(shape = (3, ))
        
        # CRIACAO DAS CAMADAS OCULTAS DA REDE NEURAL DENSA
        x = Dense(units = 64, activation =  'sigmoid')(states)
        y = Dense(units = 32, activation = 'sigmoid')(x)
        
        # CRIACAO DA CAMADA DE SAIDA, CONECTADA COM A ULTIMA CAMADA OCULTA
        q_values = Dense(units = number_actions, activation = 'softmax')(y)
        
        # AGREGAR TODAS AS CAMDAS EM UM MODELO (OBJETO MODEL)
        self.model = Model(inputs = states, outputs = q_values)
        
        # COMPILACAO DO MODELO, UTILIZANDO A FUNCAO DE ERRO E OTIMIZADOR
        self.model.compile(loss = 'mse', optimizer = Adam(lr = self.learning_rate))
        