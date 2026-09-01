#EXAMPLE1
#a = int(input('please give a: '))
#b = int(input('please give b: '))
#c = int(input('please give c: '))
#ab = a -b
#ac = a-c
#bc = b-c

#if ab*bc>0:
#    result =b
#elif ab*ac < 0:
#    result = a
#else:
#    result = c

#print(result)
#result = 1
#x = int(input('x: '))
#y = int(input('y: '))

#while y > 0:
#    if y % 2 == 0:
#        y /= 2
#        x = x**2
#    else:
#        y -=1
#        result *= x

#print(result)


#HW1

#a = int(input('give a: '))
#b = int(input('give b: '))
#c = int(input('give c: '))
#result = a
#if b > result:
#    result = b
#if c > result:
#    result = c

#print(result)

#HW2
#def fun(x):
#    flag = True
#    i = 2
#    while flag and i < len(x):
#        y=x[i]-x[i-1] 
#        z= x[i-1]-x[i-2]
#        print(f'{i}= i, current difference = {y}, previous difference = {z}')

#        if y != z:
#            flag = False
#        else:
#            i += 1
#    print("Final flag: ",flag)
#    return flag

#k = [7,3,-1,-5,-8,-12]
#fun(k)