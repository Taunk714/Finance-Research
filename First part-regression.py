'''
suitable for:
figure 2 panel A
figure 3 panel A
figure 3 panel B 
'''

from sklearn import linear_model
from matplotlib import pyplot as plt
import numpy as np
def regression(dataX,dataY):
	reg = linear_model.LinearRegression()
	reg.fit(dataX,dataY)
	mu=reg.coef_[-1]
	return mu

def circlecoef():
	workbook = xlrd.open_workbook(r'F:\IF.xlsx')
	sheet2_names = workbook.sheet_names()[1]
	sheet2 = workbook.sheet_by_index(1)
	#获取sheet内容【1.根据sheet索引2.根据sheet名称】
	#sheet=workbook.sheet_by_index(1)
	sheet2=workbook.sheet_by_name('TestCase002')
	n=sheet2.nrows-1
	m=sheet2.ncols-1
	for i in [1:240]:
		u[i]=0
		for j in [1:m]: 
			A=np.mat(sheet2.col_values(j)[1:n-i]).T
			B=np.mat(sheet2.col_values(j)[1+i:n]).T
			y[i][j]=regression(a,b)
			u[i]=u[i]+y[i][j]
		u[i]=avg(y[i])
	plt.plot([1:240],u)
	plt.show()
