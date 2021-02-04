import numpy as np
import matplotlib.pyplot as plt

# número de iterações
n = 9000

# Matrizes da transformação
A1 = np.array([[0, 0], [0, 0.16]])
A2 = np.array([[0.85, 0.04], [-0.04, 0.85]])
A3 = np.array([[0.2, -0.26], [0.23, 0.22]])
A4 = np.array([[-0.15, 0.28], [0.26, 0.24]])
t1 = np.array([[0], [0]])
t2 = np.array([[0], [1.6]])
t3 = np.array([[0], [1.6]])
t4 = np.array([[0], [0.44]])

# Probabilidades das transformações lineares serem aplicadas
p1 = 0.01
p2 = 0.85
p3 = 0.07
p4 = 0.07

# Pontos iniciais
x = []
y = []
x.append(0)
y.append(0)

# Escrevendo (x,y) como vetores

v = np.array([[x[0]], [y[0]]])

for i in range(n):
    k = np.random.rand()
    if k < p1:
        v = A1.dot(v) + t1
    elif k < p1 + p2:
        v = A2.dot(v) + t2
    elif k < p1 + p2 + p3:
        v = A3.dot(v) + t3
    else:
        v = A4.dot(v) + t4

    x.append(float(v[0]))
    y.append(float(v[1]))

plt.plot(x, y, '.r')
plt.show()