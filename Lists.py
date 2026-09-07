#EXAMPLE 1
#lst = [5,11,7]
#for e in lst: 
#    print(e)
#print(lst[0], lst[1], lst[2])
#lst[2] *= 5 
#print(len(lst))
#print(lst[4]) #indexing error

#lst = [] # useful for reading data types from a user
#for x in range(10):
#    lst.append(x**2)
#    print(lst)

#lst = [x%2 for x in range(8)]
#for l in lst:
#    print(lst)

#lst = [c for c in 'thingamabob']
#for i in range(len(lst)):
#    if i% 2== 0:
#        print(lst[i], end =' ')

#lst = [10-abs(x-3) for x in range(7)]
#print(lst)
#val = 8
#print(lst.count(val))
#print(lst.index(val))

#lst = list(range(10))
#print(list(reversed(lst)))
#print(lst)

#EX1 part 1
#lst =[]
#while (v:= int(input('please give next int: '))) >=0:
#    lst.append(v)

#print(lst)

#lst =[]
#while (v:= int(input('please give next int: '))) >=0:
#   i = 0 # index into list
#    while i < len(lst) and lst[i]<v:
#        i += 1
#    lst.insert(i,v)
#print(lst)

#EX3
#lst = ['what','a','wonderful','morning']
#new = []
#for i in lst:
#    if len(i)> 4:
#        new.append(i)
#lst = new
#print(lst)

#lst = [i for i in lst if len(i)>4]
#print(lst)

#EX4
#import random
#n=12
#lst =random.sample(list(range(n)),n)
#print(lst[1:])#dropping the first value, print statement not needed in actual code
#diffs = [b -a for (a,b) in zip(lst, lst[1:])]
#print(lst)

#HW1
#h =[]
#h.append(1)
#print(h)
#h.append(6)
#print(h)
#h.insert(0,1)
#print(h)
#h.pop(1)
#print(h)
#h.pop(0)
#print(h)

#HW2
#neg =[]
#positive=[]
#while True:
#    y = int(input('give integer: '))
#    if y < 0:
#        neg.append(y)
#    elif y>0:
#        positive.append(y)
#    else:
#        break

#print(neg)
#print(positive)

#HW3
#part1
#import math
#lst =[]
#for i in range(0,8):
#    if i**2 in range(0,50):
#        lst.append(i**2)
#print(lst)

#part2

#lst =[]
#for i in range (0,4):
#    y = (f'2**{i} is {2**i}')
#    lst.append(y)

#print(lst)

#part3
#y = [i for i in range(0,6)]
#x = [x for x in range(5,11)]

#lst =[]
#for p in zip(y,x):
#    lst.append(p)

#print(lst)

#HW4

#cool =[]
#while True:
#    c = input('give a word: ')
#    if c == '!':
#        break
#    else:
#        cool.append(c)

#    pass
#while True:
#    b = input('give more integers: ')
#    if b == '!':
#        break
#    elif b in cool:
#        print('hit')
#    else:
#        cool.append(b)

#HW5
#part1 
#lst=[]
#while True:
#    y = int(input('give a nonnegative integer: '))
#    if y >= 0:
#        lst.append(y)
#    else:
#        break

#print(lst)

#part2
#lst=[]
#while True:
#    y = int(input('give a nonnegative integer: '))
#    if y >= 0:
#        lst.append(y)
#    else:
#        break
#print(lst)

#new_list=[]
#for b in lst:
#    if b not in new_list:
#        new_list.append(b)

#print(*new_list)

#HW6
#import random
#n = 10
#list_of_lists = [random.sample(list(range(n)), n) for _ in range(5)]
#print(list_of_lists)
#new=[]
#for i in list_of_lists:
#    for k in i:
#        new.append(k)
#print(new)

#HW7
#lst=[]
#while True:
#    y = int(input('give a nonnegative integer: '))
#    if y >= 0:
#        if y not in lst:
#            lst.insert(0,y)
#        else:
#            lst.remove(y)
#            lst.insert(0,y)
#    else:
#        print(lst)
#        break

#HW8
#original = []
#indices= []
#result=[]
#while True:
#    y = input('give words: ')
#    if y != '!':
#        original.append(y)
#    else:
#        break
#while True:
#    x = int(input('give indices: '))
#    if x >= 0 and x not in indices:
#        indices.append(x)
#    else:
#        break  
#print(original)
#print(indices)

#HW9
def transpose(a):
    return[list(x)for x in zip(*a)]

print(transpose([[1,2,3],[4,5,6]]))
















    




