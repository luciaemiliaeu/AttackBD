import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
'''
#-- Redução de atributos irrelevantes
data_attack = pd.read_csv('attacks.csv', sep=';')

#data_attack.drop('frame.time_delta', axis =1, inplace = True)
data_attack.drop('frame.time_epoch', axis =1, inplace = True)
data_attack.drop('frame.time_relative', axis =1, inplace = True)
data_attack.drop('tcp.srcport', axis =1, inplace = True)
data_attack.drop('tcp.dstport', axis =1, inplace = True)
data_attack.drop('eth.src', axis =1, inplace = True)
data_attack.drop('eth.dst', axis =1, inplace = True)
data_attack.drop('frame.number', axis =1, inplace = True)
data_attack.drop('mqtt.clientid', axis =1, inplace = True)
data_attack.drop('mqtt.msg', axis =1, inplace = True)
data_attack.drop('mqtt.passwd', axis =1, inplace = True)
data_attack.drop('mqtt.qos', axis =1, inplace = True)
data_attack.drop('mqtt.topic', axis =1, inplace = True)
data_attack.drop('mqtt.username', axis =1, inplace = True)
data_attack.drop('mqtt.willmsg', axis =1, inplace = True)
data_attack.drop('mqtt.willtopic', axis =1, inplace = True)
data_attack.drop('mqtt.topic_len', axis =1, inplace = True)

data_attack.columns = data_attack.columns.str.lower().str.replace('.', '_')
data_attack.to_csv('data_attackv2.csv', index=False, sep =';')

#-- Tratamento de atributos - Parte I
data_attack = pd.read_csv('data_attackv2.csv', sep=';')

# Substituindo o endereço ipv6 pela primeira parte
data_attack['ipv6_src'] = data_attack.apply(lambda x: x['ipv6_src'].split(":")[0], axis=1)
data_attack['ipv6_dst'] = data_attack.apply(lambda x: x['ipv6_dst'].split(":")[0], axis=1)

# Substituindo campos pelo número de flags
index = data_attack[(data_attack['mqtt_dupflag'].isnull() == False)].index
data_attack.loc[index, 'mqtt_dupflag'] = data_attack.loc[index, :].apply(lambda x: len(str(x['mqtt_dupflag']).split(",")), axis=1)
index = data_attack[(data_attack['mqtt_hdrflags'].isnull() == False)].index
data_attack.loc[index, 'mqtt_hdrflags'] = data_attack.loc[index, :].apply(lambda x: len(str(x['mqtt_hdrflags']).split(",")), axis=1)
index = data_attack[(data_attack['mqtt_msgid'].isnull() == False)].index
data_attack.loc[index, 'mqtt_msgid'] = data_attack.loc[index, :].apply(lambda x: len(str(x['mqtt_msgid']).split(",")), axis=1)
index = data_attack[(data_attack['mqtt_msgtype'].isnull() == False)].index
data_attack.loc[index, 'mqtt_msgtype'] = data_attack.loc[index, :].apply(lambda x: len(str(x['mqtt_msgtype']).split(",")), axis=1)
index = data_attack[(data_attack['mqtt_retain'].isnull() == False)].index
data_attack.loc[index, 'mqtt_retain'] = data_attack.loc[index, :].apply(lambda x: len(str(x['mqtt_retain']).split(",")), axis=1)

# Substituindo missin values por 0 - ausência de flags nos campos
index = data_attack[(data_attack['mqtt_dupflag'].isnull() == True)].index
data_attack.loc[index, 'mqtt_dupflag'] = data_attack.loc[index, :].apply(lambda x: 0, axis=1)
index = data_attack[(data_attack['mqtt_hdrflags'].isnull() == True)].index
data_attack.loc[index, 'mqtt_hdrflags'] = data_attack.loc[index, :].apply(lambda x: 0, axis=1)
index = data_attack[(data_attack['mqtt_msgid'].isnull() == True)].index
data_attack.loc[index, 'mqtt_msgid'] = data_attack.loc[index, :].apply(lambda x: 0, axis=1)
index = data_attack[(data_attack['mqtt_msgtype'].isnull() == True)].index
data_attack.loc[index, 'mqtt_msgtype'] = data_attack.loc[index, :].apply(lambda x: 0, axis=1)
index = data_attack[(data_attack['mqtt_retain'].isnull() == True)].index
data_attack.loc[index, 'mqtt_retain'] = data_attack.loc[index, :].apply(lambda x: 0, axis=1)
index = data_attack[(data_attack['mqtt_kalive'].isnull() == True)].index
data_attack.loc[index, 'mqtt_kalive'] = data_attack.loc[index, :].apply(lambda x: 0, axis=1)

# Tratando mqtt
data_attack['mqtt_len_flag'] = data_attack.loc[:,:].apply(lambda x: len(str(x['mqtt_len']).split(",")), axis=1)
data_attack['mqtt_len_null'] = data_attack['mqtt_len'].isna()
data_attack.loc[data_attack[(data_attack['mqtt_len_null']==True)].index,'mqtt_len_flag'] = 0
data_attack.drop('mqtt_len', axis=1, inplace=True)

data_attack.to_csv('data_attackv3.csv', index=False, sep =',')


#-- Tratamento de atributos - Parte II

data_attack = pd.read_csv('data_attackv3.csv', sep =',')

# Tratando nominais 
selec = data_attack[(data_attack['ipv6_src']=='fd9e')].index
not_selec = data_attack[(data_attack['ipv6_src']!='fd9e')].index
data_attack.loc[selec, 'ipv6_src_fd'] = data_attack.loc[selec,:].apply(lambda x: 1, axis=1)
data_attack.loc[not_selec, 'ipv6_src_fd'] = data_attack.loc[not_selec,:].apply(lambda x: 0, axis=1)

selec = data_attack[(data_attack['ipv6_src']=='fe80')].index
not_selec = data_attack[(data_attack['ipv6_src']!='fe80')].index
data_attack.loc[selec, 'ipv6_src_fe'] = data_attack.loc[selec,:].apply(lambda x: 1, axis=1)
data_attack.loc[not_selec, 'ipv6_src_fe'] = data_attack.loc[not_selec,:].apply(lambda x: 0, axis=1)
data_attack.drop('ipv6_src', axis =1, inplace=True)

selec = data_attack[(data_attack['ipv6_dst']=='fd9e')].index
not_selec = data_attack[(data_attack['ipv6_dst']!='fd9e')].index
data_attack.loc[selec, 'ipv6_dst_fd'] = data_attack.loc[selec,:].apply(lambda x: 1, axis=1)
data_attack.loc[not_selec, 'ipv6_dst_fd'] = data_attack.loc[not_selec,:].apply(lambda x: 0, axis=1)

selec = data_attack[(data_attack['ipv6_dst']=='fe80')].index
not_selec = data_attack[(data_attack['ipv6_dst']!='fe80')].index
data_attack.loc[selec, 'ipv6_dst_fe'] = data_attack.loc[selec,:].apply(lambda x: 1, axis=1)
data_attack.loc[not_selec, 'ipv6_dst_fe'] = data_attack.loc[not_selec,:].apply(lambda x: 0, axis=1)

selec = data_attack[(data_attack['ipv6_dst']=='ff02')].index
not_selec = data_attack[(data_attack['ipv6_dst']!='ff02')].index
data_attack.loc[selec, 'ipv6_dst_ff'] = data_attack.loc[selec,:].apply(lambda x: 1, axis=1)
data_attack.loc[not_selec, 'ipv6_dst_ff'] = data_attack.loc[not_selec,:].apply(lambda x: 0, axis=1)
data_attack.drop('ipv6_dst', axis =1, inplace=True)

selec = (data_attack['mqtt_len_null']==True)
data_attack.loc[data_attack[selec].index,'mqtt_len_null'] = 1
data_attack.loc[data_attack[~selec].index,'mqtt_len_null'] = 0

normal = data_attack[(data_attack['label']=='normal')].index
bruteforce = data_attack[(data_attack['label']=='bruteforce')].index
enumeration = data_attack[(data_attack['label']=='enumeration')].index
mitm = data_attack[(data_attack['label']=='mitm')].index
DoS = data_attack[(data_attack['label']=='DoS')].index
data_attack.loc[normal,'label'] = 0
data_attack.loc[bruteforce,'label'] = 1
data_attack.loc[enumeration,'label'] = 2
data_attack.loc[mitm,'label'] = 3
data_attack.loc[DoS,'label'] = 4

data_attack.to_csv('data_attackv4.csv', index=False, sep =',')

# -- Limpando duplicatas e balanceando a base 
data_attack = pd.read_csv('data_attackv4.csv', sep =',')

#Excluindo instâncias repetidas
data_attack.drop_duplicates(inplace= True)

#-- Balanceamento da base
c = data_attack.groupby('label')
data_attack = c.apply(lambda x: x.sample(n = c.size().min()).reset_index(drop=True))

data_attack.to_csv('data_attackv5.csv', index=False, sep =',')
'''
# Descrevendo os resultados
data_attack = pd.read_csv('data_attackv5.csv', sep =',')
print('Número de elementos por classe')
print(data_attack['label'].value_counts())
print('\n Informações dos atributos: número de instâncias não nulas e tipo')
print(data_attack.info())
print('\n Valores possíveis de cada atributo')
for i in data_attack.columns:
	print(i,':', data_attack[i].sort_values().unique())

bx = data_attack.boxplot(column=['frame_time_delta'])
print(bx)
plt.show()