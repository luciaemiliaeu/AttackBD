import pandas as pd 
import numpy as np
'''
#-- Redução de atributos irrelevantes
data_attack = pd.read_csv('attacks.csv', sep=';')

data_attack.drop('frame.time_delta', axis =1, inplace = True)
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

data_attack.to_csv('data_attackv2.csv', index=False, sep =';')

#-- Balanceamento da base
data_attack = pd.read_csv('data_attackv2.csv', sep=';')
attack = data_attack[~(data_attack['label']=='normal')]
normal = data_attack[(data_attack['label']=='normal')].sample(n = attack.shape[0], random_state=1)
notselected = data_attack.drop(attack.index)
notselected = notselected.drop(normal.index)
data_attack = data_attack.drop(notselected.index)

data_attack.to_csv('data_attackv3.csv', index=False, sep =';')
'''


data_attack = pd.read_csv('data_attackv3.csv', sep=';')
#data_attack['na'] = pd.isna(data_attack['ipv6_src'])
#data_attack['virgula'] = data_attack['mqtt_len'].str.contains(',')
#print(data_attack[(data_attack['virgula'] == True)&(data_attack['na'] == False)])
#print(data_attack[(data_attack['ipv6_nxt']==58) & (data_attack['label'] != 'normal')])
#print(data_attack[(data_attack['label'] == 'mitm')])
print(data_attack['label'].unique())
#print(data_attack[(data_attack['na'] == True)])
'''
data_attack[(data_attack['virgula'] == True)]['mqtt_len'] = 
'''