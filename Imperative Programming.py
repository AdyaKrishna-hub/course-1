#HW1
#1. Arithmetic addition, Comparing two values or applying boolean logic ar examples of fundamental computer operations. Computing n!, repeated multiplications are examples of compound computer operations.
#2.
#a=15
#b=22
#print(a)
#print(b)
#print(a-b)
#print(f'ratio of a and b is {a/b}')
#print((3*a) % (2*b))

#print(sum(range(5, 16)))

#HW2
#a=int(input("Enter a number: "))
#b= int(input("Enter a number: "))
#if a==b:
    #print(f'{a**2 + b**2 + 2*a*b}')
#else:
    #print(f'{a+b}')

#HW3

#for i in range(10,38,3):
    #print(i)

#for c in range(998,898,-2):
    #print(c)

#numbers = [1, -1] * 10
#print(", ".join(map(str,numbers)))

#numbers= [7,7,9]*20
#print(", ".join(map(str,numbers)))

#HW4

#h= int(input("card total: "))
#if h < 17:
 #   print("hit")
#elif h in range(17,22):
 #   print("stay")
#else:
 #   print("bust")

#HW5

#a = int(input("integer: "))
#b = int(input("integer: "))

#if a>100 or a==100 and b<50 or b==50:
 #   print("1")
#else:
 #   print("0")


#if a>=100 and b<= 50:
 #   print("1")
#elif a<=50 and b>=100:
 #   print("1")
#else:
 #   print("0")


#HW6

#y= int(input("give weight: "))

#if y <= 2:
 #   print("3")
#elif y<=5 and y>2:
 #   g= 2*y+3
  #  print(g)
#else:
 #   h= 3 + 5*y
  #  print(h)


 #EXAMPLE 2
#mark = int(input('Please give marks: '))
#if mark >= 90:
#    grade=10
#elif mark >= 70:
 #   grade = 9
#else:
 #   grade =8

#print('grade is', grade)

#EXAMPLE3

#n =int(input('please give a positive integer: '))
#if n>0:
#    p = 1 
#    for n in range (1,n+1): 
#        p*= n
#    print(p)
#else:
#    print("given integer is not positive: ")

#EXAMPLE5

#for i in range (9,66,4):
#    print(i, end=' ')
#OR
#v=9
#while v <= 65:
#    print(v,end=' ')
#    v += 4

#k = 3
#for x in range(13):
#    print(k, end= ' ')
#    k *= 2

#for y in range(1,41):
#    m = y
#    if y % 4 == 0:
#        m = -1
#        print (m,end = ' ')

# EXAMPLE 5
#smallest =0
#largest= 0
#for n in range(51):
#    value = n*(n-30)*(n-50)
#    if value < smallest:
#        smallest = value
#    if value > largest:
#        largest = value
#print(smallest,largest)

#for g in range(0,101):
#    n=g
#    hey= n**3-16
#    if g%47 == 0:
#        j = [g]
#        print(j, end= ' ')

#EXAMPLE7

#s = int(input('Please give the value of s: '))

#n = 1
#found =False 

#while found == False:
#    if n*(n+1)/2 > s:
#        found = True
#    else:
#        n += 1
#print(n)

#HOMEWORK7

#n = 1
#found =False

#while found == False:
#    if (n**3-16) % 47 != 0:
#        n += 1
#    else:
#        found = True
#print(n)

#HW8
#wtv comment 
#a = int(input('enter a nonnegative integer: '))

#num = 1

#for i in range(a):
#    num *= 3 # Every time the loop runs, it multiplies num by 3

#print(num)

#a = int(input('give a nonnegative integer: '))
#b = int(input('give an integer: '))

#num = 1

#for i in range(a):
#    num *= b
#print(num)

#HW9
h =1

for i in range(0,101):
    bacteria= h*(h-20)(h-100)+120000
    h += 1
    

