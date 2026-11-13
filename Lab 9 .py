# Задание 1
def divisors(n):
    for i in range(1,n+1):
        if n%i==0:
            print(i,end=' ')

n=int(input())
divisors(n)


# Задание 2
def coordinate(m1,m2,m3,x1,x2,x3):
    return (m1*x1+m2*x2+m3*x3)/(m1+m2+m3)

m1=float(input())
m2=float(input())
m3=float(input())
x1=float(input())
y1=float(input())
x2=float(input())
y2=float(input())
x3=float(input())
y3=float(input())

xc=coordinate(m1,m2,m3,x1,x2,x3)
yc=coordinate(m1,m2,m3,y1,y2,y3)

print(xc,yc)


# Задание 3
def count_negative(a):
    k=0
    for i in range(len(a)):
        if a[i]<0:
            k+=1
    return k

a=list(map(int,input().split()))
b=list(map(int,input().split()))

print(count_negative(a))
print(count_negative(b))


# Задание 4
def factorial(n):
    p=1
    for i in range(1,n+1):
        p*=i
    return p

n=int(input())
print(factorial(n))


# Задание 5
def sumD(n):
    s=0
    while n!=0:
        s+=n%10
        n=n//10
    return s

n=int(input())
print(sumD(n))


# Задание 6
def area(r):
    return 3.14*r*r

r=float(input())
print(area(r))


# Задание 7
def a_r(a,b):
    return a*b

a=float(input())
b=float(input())
print(a_r(a,b))


# Задание 8
def f(c):
    return c*9/5+32

c=float(input())
print(f(c))


# Задание 9
def average(a,b,c):
    return (a+b+c)/3

a=float(input())
b=float(input())
c=float(input())

print(average(a,b,c))


# Задание 10
def triangle(a,b,c):
    if a<b+c and b<a+c and c<a+b:
        return True
    else:
        return False

a=float(input())
b=float(input())
c=float(input())

print(triangle(a,b,c))


# Задание 11
def sum_a(*nums):
    s=0
    for i in nums:
        s+=i
    return s

print(sum_a(1,2,3,4,5))


# Задание 12
def norm(text):
    text=' '.join(text.split())
    if text!='':
        text=text[0].upper()+text[1:]
    return text

s=input()
print(norm(s))


# Задание 13
def primes(limit):
    a=[]
    for n in range(2,limit+1):
        simple=True
        for i in range(2,n):
            if n%i==0:
                simple=False
        if simple:
            a.append(n)
    return a

limit=int(input())
print(primes(limit))
