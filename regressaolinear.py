import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

#Universidade de Brasilia - Metodos Computacionais A
#Professor: Luiz A. Ribeiro Junior - Instituto de Fisica
#Aluno: Alexandry Moreira Alves Pinto - 17/0078761
#Problema 4 - Regressao Linear por Minimos Quadrados.
#Github url: 



n=200

#Lendo os dados do arquivo 
X, Y = [], []
for line in open('vxt.dat', 'r'):
  values = [float(s) for s in line.split()]
  X.append(values[0])
  Y.append(values[1])

#Calculando a somatoria dos valores de x_i * y_i onde i=(1,n) e salvando em uma matriz xy[0][n]
xy = np.zeros((1, n))
for i in range(n):
    xy[0][i] = X[i]*Y[i]

#Calculando a somatoria dos valores de x_i * x_i onde i=(1,n) e salvando em uma matriz xx[0][n]
xx = np.zeros((1, n))
for i in range(n):
    xx[0][i] = X[i]*X[i]

#Calculando a somatoria dos valores x_i onde i=(1,n) e salvando na variavel Sx
Sx = sum(X)
#Calculando a somatoria dos valores y_i onde i=(1,n) e salvando na variavel Sy
Sy = sum(Y)
#Calculando a somatoria dos valores da matriz xy[0][i] onde i=(1,n) e salvando na variavel Sxy
Sxy = sum(xy[0])
#Calculando a somatoria dos valores da matriz xx[0][i] onde i=(1,n) e salvando na variavel Sxx
Sxx = sum(xx[0])

#Calculando o a_1:
aum = (n*Sxy - Sx * Sy)/(n*Sxx - (Sx)**2)

#Calculando o a_2:
azero = (Sxx*Sy - Sxy * Sx)/(n*Sxx - (Sx)**2)

#Plotando o grafico dos valores de vxt.dat
fig, ax = plt.subplots()
blue_patch = mpatches.Patch(color='blue', label='vxt.dat')
plt.legend(handles=[blue_patch])
ax.plot(X, Y, color='tab:blue')
ax.set(xlabel='tempo (s)', ylabel='velocidade (m/s)',
       title='Grafico VxT.', )

fig.savefig("dados.png")
plt.show()

#Imprimindo os valores obtidos e a funcao encontrada.
print
print
print('a_0 = %g' % (azero))
print('a_1 = %g' % (aum))
print('y = %g + %g * x' % (azero,aum))
print
print


#Plotando o grafico da funcao encontrada.
t = np.arange(0.0, 200.0, 0.01)
s = azero + aum*t
fig, ax = plt.subplots()
red_patch = mpatches.Patch(color='red', label=r'$regress\tilde{a}o$ $linear$')
plt.legend(handles=[red_patch])
ax.plot(t,s, color='tab:red')
ax.set(xlabel='tempo (s)', ylabel='velocidade (m/s)',
       title=r'Regressao Linear - $y = %g + %g x$' % (azero,aum))
fig.savefig("regressao.png")
plt.show()

#Plotando os dois graficos juntos para uma melhor analise.
fig, ax = plt.subplots()
plt.plot([1, 2, 3], label="vxt.dat", color='blue')
plt.plot([3, 2, 1], label=r'$regress\tilde{a}o$ $linear$', color='red')
plt.legend(ncol=2)
ax.plot(X, Y, color='tab:blue')
ax.plot(t,s, color='tab:red')
ax.set(xlabel='tempo (s)', ylabel='velocidade (m/s)',
       title=r'Comparacao dos dados com a $regress\tilde{a}o$ $linear$.')
fig.savefig("comparacao.png")
plt.show()


