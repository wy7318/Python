from numpy import *
from numpy.linalg import *
A = mat([[1.,2.],[4.,5.],[7.,8.]])
Q,R = qr(A)
print ”Q”
print Q
print ”R”
print R
print ”(abs(Q*R-A)>1e-10).all()”
print (abs(Q*R-A)>1e-10).all()
b=mat([3.,6.,10.]).reshape(3,1)
x=solve(R,Q.T*b)
print ”x”
print x
