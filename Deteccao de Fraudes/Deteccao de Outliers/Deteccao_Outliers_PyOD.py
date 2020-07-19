# -*- coding: utf-8 -*-
# Importacao de bibliotecas
import matplotlib.pyplot as plt
from pyod.models.knn import KNN
import seaborn as sns
import pandas as pd

# Pre-processamento de dados
base = pd.read_csv('credit_data.csv')
base = base.dropna()
base.describe()

# Detectando Outliers
detector = KNN()
detector.fit(base.iloc[:, 1:4])

previsoes = detector.labels_
confianca_previsoes = detector.decision_scores_

# Listando os Outliers
outliers = []
for i in range(len(previsoes)):
    if previsoes[i]== 1:
        outliers.append(i)

lista_outliers = base.iloc[outliers, :]

print(lista_outliers)