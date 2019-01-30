import numpy as np
#Creating matrix from list and difining dimensions 3,2
A=np.matrix([1,2,3,4,5,6]).reshape(3,2)
#printing A
print ”Matrix A is”
print(A)
#a)
B=np.dot(A,A.T)
print ”a) B=A∧TA”
print(B)
#b)
sumofA=np.sum(np.square(A))
print ”b) The sum of the squares of the coefficients of A”
print(sumofA)
#c)
rowVectorColumn=np.mean(A,axis=0)
print ”c) The row vector of column means”
