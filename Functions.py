#EXAMPLE 1
#def abs_value(x):
#    if x < 0:
#        return -x
#    else:
#        return x

#for x in [-5.6,2,-6,0,3]:
#    print(x,abs_value(x))

#def distance(a,b):
#    return abs_value(a-b)

#print(distance(-5,16))

#EXAMPLE 2

#def interleave(a,b):
#    flattened = []
#    for (x,y) in zip(a,b):
#        flattened.append(x)
#        flattened.append(y)
#    return flattened
#print(interleave([1,2,3],[4,5,6]))

#EXAMPLE 3
#def swap(lst,ind1,ind2):
#    (lst[ind1], lst[ind2]) = (lst[ind2],lst[ind1])

#lst = list(range(5))
#swap(lst,0,2)
#print(lst)

#EXAMPLE4

#def read_floats(n):
#    return [float(input(f'input value {x+1} out of {n}: '))for x in range(n)]

#print(read_floats(2))

#HW2
#def sum_upto(n):
#    for val in n:
#        val = len(n)*(len(n)+1)/2
#        return val
#c = [f for f in range(1,21)]
#print(sum_upto(c))

#HW3
#lst = []
#def read_ints():
#    while True:
#        y = input('give integers: ')
#        if y == '':
#            break
#        else:
#            lst.append(int(y))
#    return lst

#print(read_ints())

#HW4
#def share(a,b):
#    for c in a:
#        if c in b:
#            return True
#    return False

#d = [3,5,7]
#e = [8,7,9,2,1]
#print(share(d,e))

#HW5
#def remove(orig,x,out):
#    for y in orig:
#        if x == y:
#            orig.pop(y)
#        while len(orig)<10:
#            b = 0
#            orig.append(b)
#    orig = out
#    return out

#orig_try= [1,2,3,4,5,5,4,3,2,1]
#x_try= 4
#out_try = [1,2,3,5,5,3,2,1,0,0]
#print(remove(orig_try,x_try,out_try))

#HW6
#def alternate(lst):
#    cool =[]
#    n =len(lst)
#    for i in range(n//2): #tells the number of pairs we need
#        cool.append(lst[i])
#       cool.append(lst[n-1-i]) #len numbers the list 1 more than it is so we must subtract i from it
#   if n % 2 == 1:
#           cool.append(lst[n // 2]) #finds the central value
#    return cool

#y = [1,2,3,4,5,6,7]
#print(alternate(y))

#HW7
#PART1
#def func(x):
#    y = 0.5*(x+2/x)
#    return y

#def iterate(f,x,n):
#   lst =[]
#    for i in range(n):
#        x = f(x)
#        lst.append(x)
#   return lst

#result = iterate(func,1,6)
#print(result)

#PART2
#def apply_functions(fs,x):
#    j = reversed(fs)
#    for i in j:
#        x = i(x)
#    return x
#b =['     '.join,str.split, str.lower]
#m= 'WHAT IS THIS?'
#print(apply_functions(b,m))


        


        


    









