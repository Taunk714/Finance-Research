'''
figure2 panel B
'''
from sklearn import linear_model
import numpy as np
from matplotlib import pyplot as plt
from reg_corf import nmreg as ng

def circlecoef():
	workbook = xlrd.open_workbook(r'F:\IF.xlsx')
	sheet2_names = workbook.sheet_names()[1]
	sheet2 = workbook.sheet_by_index(1)
	n=sheet2.nrows-1
	m=sheet2.ncols-1
	for j in [6:m]:
		for i in [1:n]:
			ReS(i)[j]=sum(sheet2.col_values(j)[i-5:i+5])  #直接excel处理也很快
	for i in [1:240]:
		u[i]=0
		for j in [1:m]: 
			A=np.mat(ReS(j)[1:n-i]).T
			B=np.mat(ReS(j)[1+i:n]).T
			y[i][j]=regression(a,b)
			u[i]=u[i]+y[i][j]
		u[i]=avg(y[i])
	plt.plot([1:240],u)
	plt.show()
