#EXAMPLE1
#txt ='what is this?'
#print(txt.replace(' ','<pause>', count =1)) #removes space and puts <pause>, count only replaces first instance of <pause>

#EXAMPLE2
#txt = 'food.bar.what.txt'
#def last_dot_kept(s):
#    new = s.replace('.','-dot-',count = s.count('.')-1)
#    return new
#print(last_dot_kept(txt))

#strings as immutable
#s = 'thingamabob'
#print(s[1:])#str starting from 1 number index
#for c in s:
#    print(c, end=' ')
#    if c < 'd': #checks value agaisnt dictionary
#        print(c, end = ' ')

#EXAMPLE 3
#def find_all(s, sub):
#    start = 0 #index where we start our search
#    result =[]
#    while (m:= s.find(sub,start)) != -1:
#        result.append(m)
#        start = m + 1
#    return result

#s = 'ababab'
#print(find_all(s,'aba'))
#print(find_all(s,'ab'))
#print(find_all(s,'b'))


#HW2
#def date_of_birth(ssn):
#    d = int(ssn[0:2])
#    m = int(ssn[2:4])
#    y = (ssn[4:6])
#    c = ssn[6]
#    if c =='+':
#        j= int('18'+y)
#    elif c =='-':
#        j = int('19'+y)
#    else:
#        j = int('20'+y)
#    return (j,m,d)

#b = '140598+abcd'
#print(date_of_birth(b))

#HW4
#txt = "Mi casa, su casa." 
#x = txt.rfind("casa")
#print(x) #prints starting index of where casa starts, spaces are included in len

#def file_type(s):
#    while '.' in s and s.rfind('.') != len(s)-1:
#        b = s.rfind(".")
#        return s[b+1:]
#    else:
#        return ""

#g = 'foo.docx'
#print(file_type(g))

#HW1
#import math 
#for k in range(11):
#    alpha = k*(math.pi/5)
#    b = math.sin(alpha)
#    v = math.cos(alpha)
#    print(alpha,b,v)

#HW3
#def dashify_substring(s,sub):
#    if sub not in s:
#        return s
#    else:
#        yay = '-'+sub+'-'
#        return s.replace(sub,yay,1)
#b = 'foobar'
#hehe='oba'
#print(dashify_substring(b,hehe))


#HW5
#while True:
#    s=(input('give operation: '))
#    if s == '':
#        break
#    else:
#        [y,x,z]= (s.split())
#        h = [y,x,z]
#        y= float(y)
#        z = float(z)
#        if '-' in h:
#            print(y-z)
#        elif '+' in h:
#            print(y+z)
#        else:
#            print(y*z)

#HW6
#def max_char_rep(s):
#   if not s:
#        return 0
#    max_count = 1
#    count = 1
#    for i in range(1,len(s)):
#        if s[i]==s[i-1]:        
#            count += 1
#            if count > max_count:
#                max_count= count
#        else:
#            count = 1
#    return max_count

#f = 'abbbcdd'
#print(max_char_rep(f))


        

        


    

        













    
            
