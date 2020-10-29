import cmath
a=float(input("Enter the value  of a:"))
b=float(input("Enter the value  of b:"))
c=float(input("Enter the value  of c:"))
p=(-b+cmath.sqrt(b**2-4*a*c))/(2*a)
q=(-b-cmath.sqrt(b**2-4*a*c))/(2*a)
print('The solution are {0} and {1}'.format(p,q))