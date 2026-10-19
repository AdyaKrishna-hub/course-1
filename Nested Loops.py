#EXAMPLE1
#N = 7
# = N
#for row in range(N):
#    for number in range(1,k + 1):
#        print(number, end = ' ')
#    k -= 1 #why is indentation here 
#    print() #prints a new row so it starts on a new row
#method 2
#N = 4
#for row in range(N):
#    k = N - row #table of values, when k = n-1, row = 1
#    for number in range(1,k + 1):
#        print(number, end = ' ')
#    print() #prints a new row so it starts on a new row

#EXAMPLE3
#flights = ['AY664','BA047', 'AF110', 'LH554','AY101']
#airlines = ['AY', 'UA', 'LH']
#print('flights:', flights)
#print('airlines:',airlines)
#for a in airlines:
#    print(f'{a}:', end='')
#    for f in flights:
#        if f.startswith(a):
#            print(f,end = ' ')
#    print()

#HW1
#for i in range(1,6):
#   for b in range(1,6):
#        print(b, end = ' ')
#    print()
#PART2
#s = [c for c in range (1,6)]
#for b in range(1,6):
#    print(s, end = ' ')
#    s.pop(0)
#    s.append(s[-1]+1)
#print()

#HW5
def uniques(numbers):
    unique = False
    count = 0
    for i in range(len(numbers)):
        
    if count > 1:
        unique = True
    return unique
lst = [1,7,2,4,5,3]
print(uniques(lst))
        
