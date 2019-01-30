from numpy import*
from numpy.linalg import *
A = mat([[1.,2.,],[4.,5.],[7.,8.]])
print ”A”
print A
U,s,V = svd(A.T*A)
S = diag(s)
print ”U”
print U
print ”S”
print S
9
print ”V”
print V
print (abs(U*S*V-(A.T*A))
>1e-10).all()
b=mat([3.,6.,10.]).reshape(3,1)
x = (A.T*A)*(A.T*b)
print ”x”
print x
