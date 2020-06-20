# with open('ttids.txt', 'a+') as f:
#     # f.write(','.join(item.house_id));
#     f.write('88'+',')
#

# with open('ids.txt','r') as f:
#     tt = f.read()
#     print(tt)
#     tt = tt[:-1]
#     print(len(tt.split(',')))

import pandas as pd
import numpy as np

csv = pd.read_csv('info.csv',usecols=[14],header=None)

nparr = np.array(csv.stack())

arr = nparr.tolist()[1:]
print(len(arr))

if(str(16937838) in arr):
    print('已经存在')