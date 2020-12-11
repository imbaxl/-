import numpy as np
'''
a = np.array([[1,2,3],[4,5,6]])
b = np.array([[2,2,3],[4,4,2]])
c = a*b

print(c)
'''
#matrix是array的分支，
a = np.array([[1,2,3],[1/2,1/4,1/6],[1/3,1/6,1/9]])
b = np.array([[0,1,1],[1,0,-1],[1,1,1]])
#c = a.dot(b)
c = np.dot(a, a) #matrix可以用*符号相乘，但array类型要用dot()方法相乘
print(c)

#转置 https://www.runoob.com/numpy/numpy-matrix.html
print('转置结果：',c.T)
