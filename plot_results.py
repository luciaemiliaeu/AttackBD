import pandas as pd 
import matplotlib.pyplot as plt 
'''
results = pd.read_csv('results2.csv', sep =',')
results_by_algorit = pd.DataFrame(columns = ['Algoritmo','Pct_treino', 'Acc', 'Acc_DV', 'Fscore', 'Precision', 'Recall'])

for pct, values in results.groupby(['Pct_treino']):
	for alg, data in values.groupby(['Algoritmo']):
		results_by_algorit.loc[results_by_algorit.shape[0],:] = [alg, pct, data['Acuracia'].mean(), data['Acuracia'].std(), data['Fscore'].mean(), data['Precision'].mean(), data['Recall'].mean()]
results_by_algorit.to_csv('results_by_algorit.csv', sep = ',', index = False)
'''
results = pd.read_csv('results_by_algorit.csv', sep =',')

metrics = ['Accuracy', 'F-score', 'Precision', 'Recall' ]
for metric in metrics:	
	fig = plt.figure()
	plt.title(metric)
	for alg, values in results.groupby(['Algoritmo']):
		if metric == 'Accuracy':
			plt.plot(values['Pct_treino'], values[metric], label = alg)
			plt.fill_between(values['Pct_treino'], values[metric]-2*values['Acc_DV'],values[metric]+2*values['Acc_DV'], alpha=0.2 )
		else:		
			plt.plot(values['Pct_treino'], values[metric], label = alg)
	plt.axis([results['Pct_treino'].min(),results['Pct_treino'].max(), 0, 1.0])
	plt.xlabel('Train size')
	plt.ylabel('Accuracy')
	plt.grid(True)
	plt.legend()

plt.show()