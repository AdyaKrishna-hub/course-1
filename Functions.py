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








