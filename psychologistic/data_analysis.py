import pandas as pd 
from matplotlib import pyplot as plt
df = pd.read_excel('psychologistic/data.xlsx',index_col=0)
print('样本池目前共有%s个样本'%(df.shape[0]))

fig = plt.figure()
