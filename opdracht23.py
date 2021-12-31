from math import sqrt


# testing

x = 8

for n in range(2,10):

    m1 = (-n**2+sqrt(n**4+6*x*n+x**2))/(2*n)
    m2 = (-n**2-sqrt(n**4+6*x*n+x**2))/(2*n)

    print(m1)
    print(m2)

    if m1%1==0 and m1>1:
        print(f"n:{n}, m1:{m1}")
    
    if m2%1==0 and m2>1:
        print(f"n:{n}, m2:{m2}")