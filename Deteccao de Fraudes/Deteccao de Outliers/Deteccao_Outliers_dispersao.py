# -*- coding: utf-8 -*-
# Importacao de bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Pre-processamento de dados da base credit data
base = pd.read_csv('credit_data.csv')
base = base.dropna()
base.describe()

# Grafico income x age
plt.scatter(base.iloc[:, 1], base.iloc[:, 2])

# Grafico income x loan
plt.scatter(base.iloc[:, 1], base.iloc[:, 3])

# Grafico age x loan
plt.scatter(base.iloc[:, 2], base.iloc[:, 3])

# Pre-processamento de dados da base census
base_census = pd.read_csv('census.csv')
base_census = base_census.dropna()
base_census.describe()

# Grafico age x final weight
plt.scatter(base_census.iloc[:, 0], base_census.iloc[:, 2])