import pandas as pd 
import matplotlib.pyplot as plt 


results = pd.read_csv('results.csv', sep =',')

figure = plt.figure(figsize=(27, 9))

results_by_algorit = pd.DataFrame(columns = ['Algoritmo','Pct_treino', 'Acc', 'DV'])

for pct, values in results.groupby(['Pct_treino']):
	for alg, data in values.groupby(['Algoritmo']):
		results_by_algorit.loc[results_by_algorit.shape[0],:] = [alg, pct, data['Acuracia'].mean(), data['Acuracia'].std()]
results_by_algorit.to_csv('results_by_algorit.csv', sep = ',', index = False)

results = pd.read_csv('results_by_algorit.csv', sep =',')

for alg, values in results.groupby(['Algoritmo']):
	print(alg)
	plt.plot(values['Pct_treino'], values['Acc'], label = alg)
	plt.fill_between(values['Pct_treino'], values['Acc']-2*values['DV'],values['Acc']+2*values['DV'], alpha=0.2 )

plt.axis([results['Pct_treino'].min(),results['Pct_treino'].max(), 0, 1.0])
plt.xlabel('Train size')
plt.ylabel('Accuracy')
plt.grid(True)

plt.legend()
plt.show()

plt.savefig('resultado')