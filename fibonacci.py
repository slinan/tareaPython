# coding=utf-8
#Correr en Python 2!
#Santiago Liñán - s.linan10@uniandes.edu.co
try:
    x=int(raw_input('Número:'))
except ValueError:
    print "No es un número"

fibo = []

def fib(n):
	if n==0 or n ==1:
		return n
	return fib(n-1)+fib(n-2)
i = 0;
n = fib(i);
while n < x:
	fibo.append(n)
	i+=1
	n=fib(i)
	
print 'Serie de Fibonacci menor que %d:' %(x)
print fibo
