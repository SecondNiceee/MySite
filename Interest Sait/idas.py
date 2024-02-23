
import math
#a
x = float(input())
y = float(input())
z = float(input())
a = (  ( math.sqrt(abs(x-1)) - abs(y)**(1/3)  ) ) /  (1 + (x**2/2) + (y**2 / 4)) 
b =    x * (   math.atan(z) + math.exp(-(x+3))       )
print(a,b)
#b
a = (3 + math.exp(y-1)) / (1 + x**2 * abs(y - math.tan(z)))
b = 1 + abs(y-x) + (( (y-x)**2) / 2) + ((abs(y-x)**3) / 3)
print(a,b)

#в
a = (1+y)* (  (x + (y / (x**2 + 4)))  / (math.exp(-x-2) + (1/(x**2+4))))
b = (1+math.cos(y-2)) / ((x**4 / 2) + math.sin(z)**2)
print(a,b)
#г
a = y + (x) / (y**2 + abs((x**2) / (y + (x**3 / 3))))
b = (1+ math.tan(z/2)**2)
print(a,b)
#д
a = (2*math.cos(x - (math.pi/6))) / ( 1/2 + math.sin(y)**2)
b = 1 + (z**2) / (3 + (z**2 / 5))
print(a,b)
#e
a = ( (1+math.sin(x+y)**2) / (2 + abs(x - (2*x) / (1+x**2*y**2))) ) + x
b = math.cos(math.atan(1/z))**2
print(a,b)
#ж
a = math.log(abs((y - math.sqrt(abs(x)))*(x - (y/(z + (x**2 / 4))))))
b = x - ((x**2) / (math.factorial(3))) + (x**5/(math.factorial(5)))
print(a,b)

print('Второе задани: ')
x1 , x2 , x3,  y1, y2, y3= map(float, input().split())
S = 1/2* abs(( (x2-x1)*(y3-y1) - (x3 - x1)*(y2 - y1) ) )
print(S)
print()
print()
print('Третье задание')
a = float(input(a))
S = a**2
h = (a*math.sqrt(3) / 2)
S = (a**2 * math.sqrt(3)) / (4)
r = (a*math.sqrt(3)) / 6
R = (a*math.sqrt(3) / 3)
print(S , h, r , R)
print()
print()
print('Четвертое задание')
firstElement = float(input('первый элемент: '))
col = int(input('Количество элементов: '))
znam = float(input('знаменатель: '))
Summ = ( (2*firstElement + znam*(col - 1)) / 2 ) * col
print(Summ)
print()
print()
print('Пятое  задание')
a, b ,c = map(float, input().split())
polP = (a + b + c) / 2
fiveH = (2* math.sqrt( polP* (polP - a) * (polP - b) * (polP - c) )) / c

print()
print()
print('Шестое  задание')
n1,n2 = map(float, input().split())
print(   (n1**3 + n2**3) / 2, (abs(n1) * abs(n2) / 2    ))

print()
print()
print('Седьмое  задание')
a = float(input())
print( a**2,  a**2*6, a**3)
print()


