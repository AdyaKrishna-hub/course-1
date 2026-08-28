#EXAMPLE 2
#for part 1
#h = int(input("give a year: "))

#leap = False

#if h % 4 == 0:
#    leap = True

#if h % 100 == 0:
#    leap= False

#if h % 400 == 0:
#    leap = True

#print(leap)

#for part 2
#print((h%400==0) or (h % 4 == 0 and not h% 100 == 0))

#EXAMPLE 3
#while not (1<= (v := int(input("what is the day of the week(1-7)"))) <= 7):
#    print('please provide a valid day of week')

#while (vacation := input('is James on vacation (yes/no): ')) != 'yes' and vacation != 'no':
#    pass

#print(vacation == 'yes' or v > 5)

#HW1

#n = input('is the sun shining: ')
#b = int(input('current time (0-23)'))
#value = False
#if n:='yes' and b in range(10,17):
#    value = True

#print(value)

#HW2

#z = int(input('give integer: '))
#x = int(input('give integer again: '))

#while (x % 10 == z % 10):
#    print(True)
#    break
#else: 
#   print(False)

#HW3
#rhs= int(input('enter a positive integer: '))
#n = 0
#while rhs > 0 and n**3 - 10*n**2 < rhs:
#    n += 1
#print(f'{n}')
#print(f'{n**3-10*n**2}')

#HW4
#a = int(input('give positive integer: '))
#b = int(input('give another positive integer: '))

#n = 1

#while not (n % a == 0) and not(n % b == 0):
#   n += 1

#print(n)

#HW6

#y = int(input('give a positive integer: '))

#v = 2

#while y % v != 0:
#    v += 1
#    if v == y:
#        v = y

#rint(v)

#HW8
#for y in range(2,100):
 #   for v in range(2,y):
 #       if y % v == 0:
 #           break
 #   else:
 #
 #        print(y, end=' ')

new = []
for y in range(2,100):
        for v in range(2,y):
            if len(new) <= 100 and y % v == 0:
                     new.append(y)
                     
        else:
            print(new, end=' ')





    




