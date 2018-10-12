#q.no.1
def area_sphere(radius):
    return (4*(3.14*radius**2))
r=float(input("enter the radius of sphere:"))
print(area_sphere(r))


#q.no.2
def perf_num(n):
    l=[]
    for i in range(1,n):
        if n%i==0:
            l.append(i)
    if sum(l)==n:
        return True
for i in range(1,78):
    if perf_num(i):
        print(i,"is perfect number")

#q.no.3
def multi_table(n):
    for i in range(1,11):
        print(n,'*',i,"=",n*i)
n=int(input("enter the number for which you want to generate a table:"))
multi_table(n)

#q.no.4
def pow_num(base,exp):
    if(exp==1):
        return base
    if(exp!=1):
        return (base*pow_num(base,exp-1))
base=int(input('enter the base:'))
exp=int(input('enter the exponent:'))
print(pow_num(base,exp))
