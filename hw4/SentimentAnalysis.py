import json
DTcount =0
BScount = 0
DT = []
BS = []
from textblob import TextBlob
for i in range(0,999):
    with open('DT/data_'+str(i)+'.txt','r') as json_file:
        data = json.load(json_file)
        DT.append(data['full_text'])
for i in range(0,999):
    with open('BS/data_' + str(i) + '.txt', 'r') as json_file:
        data = json.load(json_file)
        BS.append(data['full_text'])
p = []
n = []
m = []
x = []
id = 0
tc = 0
for i in DT:
    blob = TextBlob(i)
    temp = 0
    tc = 0
    for sentence in blob.sentences:
        temp = temp+ sentence.sentiment.polarity
        tc+=1
    tr = temp/tc
    if tr<0:
        n.append(tr)
    elif tr ==0:
        m.append(tr)
    else:
        p.append(tr)
DTT = []
DTT.append(len(n))
n.clear()
DTT.append(len(m))
m.clear()
DTT.append(len(p))
p.clear()
for i in BS:
    blob = TextBlob(i)
    temp = 0
    tc = 0
    for sentence in blob.sentences:
        temp = temp+ sentence.sentiment.polarity
        tc+=1
    tr = temp/tc
    if tr<0:
        n.append(tr)
    elif tr == 0:
        m.append(tr)
    else:
        p.append(tr)
import matplotlib.pyplot as plt
import numpy as np
BST = []
BST.append(len(n))
BST.append(len(m))
BST.append(len(p))
fig = plt.figure()
ax = fig.add_subplot(111)

xTickMarks = ['Negative','Neutral','Positive']
N = 3


ind = np.arange(N)    # the x locations for the groups
width = 0.35             # the width of the bars

p1 = ax.bar(ind, DTT, width, color='r', bottom=0)
p2 = ax.bar(ind + width, BST, width,color='y', bottom=0)

ax.set_xticks(ind + width / 2)

ax.set_xticklabels(xTickMarks)

ax.legend((p1[0], p2[0]), ('Donald Trump', 'Bernie Sanders'))
ax.autoscale_view()

plt.savefig('Trending.png')