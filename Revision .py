#USING CLASSES AND MODULES
#HW1
#import math
#for k in range(11):
#    alpha = k*(math.pi/5)
#    print(alpha, math.sin(alpha), math.cos(alpha))

#HW2
#def date_of_birth(ssn):
#   m = int(ssn[2:4])
#    d = int(ssn[0:2])
#    if ssn[6] == '+':
#        y = int('18'+ ssn[4:6])
#    elif ssn[6]=='-':
#        y = int('19' + ssn[4:6])
#    else:
#        y = int('20'+ ssn [4:6])
#    return (y,m,d)

#h = '140598+abcd'
#print(date_of_birth(h))

#HW3
#def dashify_substring(s,sub):
#    if sub in s:
#        new_sub = '-'+ sub +'-'
#        return s.replace(sub, new_sub,1)
#    else:
#        return s

#h = 'foo'
#n = 'o'
#print(dashify_substring(h,n))

#HW4
#def file_type(s):
#    if '.' in s:
#        n = s.rfind('.')
#       y = s[n+1:]
#        return y
#   else:
#       return ''
#c = 'foo.bar.docx'
#print(file_type(c))

#HW5
#while True:
#    c = (input('give an operation: '))
#    if c == '':
#        break
#    else:
#        [x,y,z] = c.split()
#        x = float(x)
#        z = float(z)
#        if '+' in c:
#            print(x+z)
#        elif '-' in c:
#            print(x-z)
#        else:
#            print(x*z)

#HW6
#def max_char_rep(s):
#    max_count = 1
#    if not s:
#        return 0
#    for i in range(1,len(s)):
#        if s[i] == s[i-1]:
#            count += 1
#            if count > max_count:
#                max_count = count
#        else:
#            count = 1
#    return max_count
#c = 'abbbcdd'
#print(max_char_rep(c))

#BOOLEAN ALGEBRA AND FLAGS
#while (response:= int(input('give a day of the week in range 1-7: '))) not in range(1,6) and response > 5:
#    break
#while (other:= input('is he on vacation: ')) != 'no' and other == 'yes':
#    break
#print(other == 'yes' or response >5)

#HW1
#current_time = int(input('give current time in range 0-23: '))
#sunshine = input('is the sun shining: ')
#if current_time in range (10,17) and sunshine == 'yes':
#    y = True
#else:
#    y = False

#if y == True:
#    print('please use sunscreen')
#else:
#    print('sunscreen not needed')

#HW2
#y = int(input('give first integer: '))
#x = int(input('give second integer: '))
#if y % 10 == x % 10:
#    print(True)
#else:
#    print(False)

#HW3
#s = int(input('give an integer: '))
#n = 0
#while s > 0 and s> n**3-10*n**2:
#    n +=1
#print(f'{n}, {n**2-10*n**2}')

#HW4
#a = int(input('give integer: '))
#b = int(input('give integer: '))
#n = 1
#while n % a != 0 or n % b != 0:
#    n += 1

#print(n)    


#LISTS
#HW2:
#negative =[]
#positive=[]
#while True:
#    y = int(input('give an integer: '))
#    if y < 0:
#        negative.append(y)
#    elif y >0:
#        positive.append(y)
#    else:
#        print(negative)
#        print(positive)
#        break

#HW3
#import math
#lst=[]
#for c in range(8):
#    lst.append(c**2)
#print(lst)

#lst = []
#for i in range(0,4):
#    y = f'2**{i} is {2**i}'
#    lst.append(y)
#print(lst)

#c = [b for b in range(6)]
#v = [a for a in range(5,11)]
#lst = []
#for i in zip(c,v):
#    lst.append(i)
#print(lst)

#HW4
#lst = []
#while True:
#    y = input('give a word or say ! to stop: ')
#    if y != '!':
#        lst.append(y)
#    else:
#        break

#while True:
#    b = input('give more words or say ! to stop: ')
#    if b in lst:
#        print('hit')
#        break

#HW5
#biglist=[]
#onlyonce=[]
#while True:
#    y = int(input('give integers and non negative integer to stop: '))
#    if y > 0:
#        biglist.append(y)
#    else:
#        break

#for b in biglist:
#    if biglist.count(b) == 1:
#        onlyonce.append(b)

#print(biglist, onlyonce)

#HW6
#import random
#n = 10
#list_of_lists = [random.sample(list(range(n)),n) for _ in range(5)]
#print(list_of_lists)
#newlist=[]
#for b in list_of_lists:
#    for i in b:
#        newlist.append(b)
#print(newlist)

#HW7
#yo = []
#while True:
#    y = int(input('give integers or a non negative integer to stop: '))
#    if y > 0:
#        if y not in yo:
#            yo.insert(0,y)
#        else:
#            yo.remove(y)
#            yo.insert(0,y)
#    else:
#        print(yo)
#        break

#HW8
#words = []
#indices = []
#combined = []
#while True:
#    h = input('give words or ! to stop: ')
#    if h != '!':
#        words.append(h)
#    else:
#        break
#while True:
#    b = int(input('give integers and negative integers to stop: '))
#    if b >= 0:
#        indices.append(b)
#    else:
#        break
#for index in range(len(words)):
#    if index not in indices:
#        combined.append(words[index])
#print(words)
#print(indices)
#print(combined)

#HW9
#def transpose(a):
#    new =[]
#    n = len(a[0])
#    for i in range(n): #outer loop shows which index we are looking for 
#        column= []
#        for b in a: #inner loop finds it within the list of list
#            column.append(b[i]) #finds the element at the given outer loop index
#        new.append(column)
#    return new
#v = [[1,2,3],[4,5,6]]
#print(transpose(v))

#BOOLEAN ALGEBRA
#HW10
#import random
#count = 0
#for i in range(10000):
#    x = random.uniform(-1,1)
#    y = random.uniform(-1,1)
#    if x**2 + y**2 <= 1:
#        count += 1
#print(f'{count/10000}')

#HW9
#n = 2
#lst = []
#while n < 10000:
#    sum = 0
#    for i in range(1,n):
#        if n % i == 0:
#            sum += i
#    if sum == n:
#        lst.append(n)
#    n += 1
#else:
#    print(lst)

#HW8
#primes= []
#n = 0
#while n <100:
#    divisor_count= 0
#    for i in range(2,n):
#        if n % i == 0:
#            divisor_count += 1
#    if divisor_count == 0:
#        primes.append(n)
#    n += 1
#else:
#    print(primes)

#PART2
#l = 0
#nice = []
#while len(nice) < 101:
#    div = 0
#    for b in range(2,l):
#        if l % b == 0:
#            div += 1
#   if div == 0:
#        nice.append(l)
#    l += 1
#else:
#    print(nice)


#HW6
#numbers = []
#prime = False
#y = int(input('give a positive integer: '))
#divisors = 0
#for i in range(2,y):
#    if y % i == 0:
#        divisors += 1
#if divisors == 0:
#    numbers.append(y)
#   prime = True
#print(prime)


#USING CLASSES AND MODULES
#HW6
#def max_char_rep(s):
#    count = 1
#    for i in range(1,len(s)):
#        if s[i] == s[i-1]:
#            count += 1
#        else:
#            count = 1
#   return count
#yay = 'aaaabcddddd'
#print(max_char_rep(yay))

#HW5
#while True:
#    y = input('give a calc: ')
#    if y != '':
#        lst = y.split()
#        lst[0] = float(lst[0])
#        lst[2] = float(lst[2])
#        if '+' in lst:
#           print(lst[0]+lst[2])
#        if '-' in lst:
#           print(lst[0]-lst[2])
#        if '*' in lst:
#            print(lst[0]*lst[2])
#    else:
#        break

#HW4
#def file_type(s):
#    y = s.rfind('.')
#    while s.rfind('.') != -1:
#        return s[y+1:]
#    else:
#        return ''
#j = 'foo.doc'
#print(file_type(j))

#HW3
#def dashify_substring(s,sub):
#    g = s.find(sub)
#    if g != -1:
#        y = '-' + sub + '-'
#        y = s.replace(sub,y,1)
#        return y
#    else:
#        return s
#v = 'foobar'
#f = 'o'
#print(dashify_substring(v,f))

def between(val,numbers):
    lst1=[]
    lst2=[]
    for num in numbers:
        if num > val:
            lst1.append(num)
        if num < val:
            lst2.append(num)
    if len(lst1) => 1 and len(lst2) => 1:


    
    
        

    





    
    
















