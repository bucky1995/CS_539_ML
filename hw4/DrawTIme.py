import json
from collections import Counter
import matplotlib.pyplot as plt
Date = []
for i in range(0,999):
    with open('DT/data_'+str(i)+'.txt','r') as json_file:
        data = json.load(json_file)
        temp = data['created_at']
        Ra = temp.split()
        Date.append(Ra[1]+Ra[2])
        # print(Ra[1]+Ra[2])
    with open('BS/data_'+str(i)+'.txt','r') as json_file:
        data = json.load(json_file)
        temp = data['created_at']
        Ra = temp.split()
        Date.append(Ra[1] + Ra[2])
DTc = Counter(Date)
print(DTc)
x =[]
y = []
for i in DTc:
    x.append(i)
    y.append(DTc[i])
    print(i)
    print(DTc[i])

plt.plot(x,y)
plt.savefig('TimeSeries.png')