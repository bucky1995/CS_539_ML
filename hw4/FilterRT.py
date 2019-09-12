import json
import matplotlib.pyplot as plt
import numpy as np
DTcount =0
BScount = 0
DT = []
BS = []
res = []
countD = 0
countB = 0
for i in range(0,999):
    with open('DT/data_'+str(i)+'.txt','r') as json_file:
        data = json.load(json_file)
        # if 'RT' not in data['full_text']:
        #     with open('DT/Non-RT/data_' + str(countD) + '.txt', 'w') as outfile:
        #         json.dump(data, outfile)
        #     countD += 1
        print(data['full_text'])
        print("================")
    with open('BS/data_'+str(i)+'.txt','r') as json_file:
        data = json.load(json_file)
        if 'RT' not in data['full_text']:
            with open('BS/Non-RT/data_' + str(countB) + '.txt', 'w') as outfile:
                json.dump(data, outfile)
            countB+=1