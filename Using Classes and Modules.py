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
txt = "Mi casa, su casa." 
x = txt.rfind("casa")
print(x) #prints starting index of where casa starts, spaces are included in len

def file_type(s):
    while '.' in s and s.rfind('.') != len(s)-1:
        b = s.rfind(".")
        return s[b+1:]
    else:
        return ""

g = 'foo.docx'
print(file_type(g))





    
            
