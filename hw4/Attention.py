import json
import matplotlib.pyplot as plt
import numpy as np
DTcount =0
BScount = 0
DT = []
BS = []
res = []
for i in range(0,999):
    with open('DT/data_'+str(i)+'.txt','r') as json_file:
        data = json.load(json_file)
        if(data['user']['followers_count']>10000):
            DTcount += 1

    with open('BS/data_'+str(i)+'.txt','r') as json_file:
        data = json.load(json_file)
        if(data['user']['followers_count']>10000):
            BScount += 1

res.append(DTcount)
res.append(BScount)
names = ['Donald Trump', 'Bernie Sanders']
niuxinboda
fig, axs = plt.subplots(1, 1, figsize=(6, 10))
axs.bar(names, res)
plt.savefig('Attention.png')