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
data_attack.drop('mqtt.topic_len', axis =1, inplace = True)

data_attack.columns = data_attack.columns.str.lower().str.replace('.', '_')
data_attack.to_csv('data_attackv2.csv', index=False, sep =';')


#-- Balanceamento da base
data_attack = pd.read_csv('data_attackv2.csv', sep=';')
c = data_attack.groupby('label')
data_attack = c.apply(lambda x: x.sample(n = c.size().min()).reset_index(drop=True))
data_attack.to_csv('data_attackv3.csv', index=False, sep =';')

'''

data_attack = pd.read_csv('data_attackv3.csv', sep=';')

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
#index = data_attack[(data_attack['mqtt_topic_len'].isnull() == True)].index
#data_attack.loc[index, 'mqtt_topic_len'] = data_attack.loc[index, :].apply(lambda x: 0, axis=1)

# Tratando mqtt
data_attack['mqtt_len_flag'] = data_attack.loc[:,:].apply(lambda x: len(str(x['mqtt_len']).split(",")), axis=1)
data_attack['mqtt_len_null'] = data_attack['mqtt_len'].isna()
data_attack.loc[data_attack[(data_attack['mqtt_len_null']==True)].index,'mqtt_len_flag'] = 0
data_attack.drop('mqtt_len', axis=1, inplace=True)

data_attack.to_csv('data_attackv4.csv', index=False, sep =',')