# TO CALCULATE  THE TIME SPENT
from datetime import datetime
from dateutil.relativedelta import relativedelta

dob = datetime(2001, 1, 14, 10, 0)

current_datetime = datetime.now()
time_spent = relativedelta(current_datetime, dob)
print(f"Time spent: {time_spent.years} years, {time_spent.months} months, "
      f"{time_spent.days} days, {time_spent.hours} hours, {time_spent.minutes} minutes")


# to calculate the DOB
from datetime import datetime, timedelta
current_datetime = datetime.now()
years = 23
months = 11
days = 25
hours = 7
minutes = 15
dob = current_datetime - timedelta(days=(years * 365) + (months * 30) + days,
                                    hours=hours,
                                    minutes=minutes)

print(f"Your Date of Birth is approximately: {dob}")


# ////////////////////////////////////////
def multi(name, default = '-'):
    line = default * len(name)
    print(line)
    print(name)
    print(line)
multi('Sonali')
multi('Hrishali', '*')
multi('Hrishali', 'Saaransh')

# //////////////////
a=5
def samp(b):
    global a
    while a>0:
        c = b*a
        print(c)
        a -= 1
samp('*')


# /////////////////////////////////
a = 5
def samp(b):
    for i in range(a, 0, -1):  # Iterate from 'a' down to 1
        c = b * i
        print(c)
samp('*')

# ///////////////////////////
def samp(b):
    a=10
    while a>0:
        if a%2 ==0:
            c = b*a
            print('$$',c,'$$')
        a -= 1
samp('*')

# /////////--TUPLE--//////////
a=(1,2,('sonali', 'Hrishi'), (232,876))
print(a[0], '\n', a[2][1])

a=(234)
b=(389,)
c=1,2,3,4,5,6
print('a:', type(a), '\n b:',type(b), '\n c:',type(c))

def minmax(i):
    return min(i), max(i)
print(minmax([3,6,7,2,98,1]))

# or #unpacking the tuple.
min, max = minmax([3,6,7,2,98,1])       #1
print(min, max)

(a,b,(c,(d,e))) = (1,4,(2,(3,7)))       #2
print(' a:', a, '\n b:', b, '\n c:', c, '\n d:', d, '\n e:', e)

#swapping using unpacking tuples
a='Sonali'
b='Hrishi'
a, b = b, a
print(a,b)

print(tuple('SonaliHrishikesh'))
print(5 in(15, 6, 3))
print(5 in[15, 6, 3])


# //////////--STRING--////////////
# concatination
print('sonali + ' + 'hrishikesh = ', 'hrishali')        #this is temporary
s = 'sonali'
print(s, '\n', s + 'hrishi')                            #this is temporary
name = ';'.join(['sonali', 'sahebrao', 'sangle'])       #this is permanent
print(name)
print(name.split(';'))

# partition
print('sonaliHrishikeshShinde'.partition('Hrishikesh'))
name, middle_name, last_name = 'sonaliHrishikeshShinde'.partition('Hrishikesh')
print(name, '\n', middle_name, '\n', last_name)

# string formatting
a = 'My name is {name} and age is {age}'.format(name='Sonali', age=24)
print(a)
a = 'My name is {0} and age is {1}'.format('Sonali', 24)
print(a)
a = 'My name is {} and age is {}'.format('Sonali', 24)
print(a)
a = 'My name is {0} and age is {1}. My full name is {0} {2}'.format('Sonali', 24, 'Sangle')
print(a)
name1 = 'My first name is {name[0]}, middle name is {name[1]} and last name is {name[2]}'.format(name=('sonali', 'sahebrao', 'sangle'))
print(name1)

# f-string and string formatting difference:
value = 4*20        #string formatting
print('the value is {value}'.format(value=value))   #without value=value, will get error
value = 4*20        #f-string
print(f'the value is {value}')   #no need of value=value

# ////////--RANGE--////////
for i in range(5):
    print(i*i)

for i in range(5, 10):
    print(i*i)

a=int(input("Enter num: "))
for i in range(a):
    print(i*i)

print(list(range(1, 5)))
print(list(range(1, 15, 2)))        #start=1, stop=15, step=2

# ///--ENUMERATE--///
s = [1,2,34,45]
for i, a in enumerate(s):
    print(f'index: {i} and value {a}')
s.append([49, 55])
s.extend([49, 55])
print(s)

# ////////////--LIST--////////////
l=[23,384,894,328]
s = l       # assigned to reference the same list l
print(s, '\n', s is l, '\n', l is s)
#copy to other list
c = s[:]        #is a copy of s, using slicing [:]
print(c, '\n', c is s, '\n', c is l, '\n', c==s)
a= l.copy()
b = list(l)
print(a, '\n', b)

l.append(23)
print(l, '\n', s, '\n', c)      #will change s as it if refering to same list as l,but will not change the c as it stores the copy of s
s.append(123)
print(l, '\n', s, '\n', c)      #will change l as it if refering to same list as s, but will not change the c as it stores the copy of s
c.append(213)
print(l, '\n', s, '\n', c)      #only changes in c, not in l & s

a = [[1,2,3], [5,6]]
b = a[:]        #will copy the value to b
print(b, '\n', a[1], '\n', b[1], '\n', a[1] is b[1])
a[1] = [8,9]    #only replace value of a[1]
print(a, '\n', b, '\n', a[1], '\n', b[1], '\n', a[1] is b[1])
a[0].append(10)
print(a, '\n', b, '\n', a[0], '\n', b[0], '\n', a[0] is b[0])

a=[[-1,1]]
a = a * 5
print(a)        #[[-1, 1], [-1, 1], [-1, 1], [-1, 1], [-1, 1]]
a[2].append(4)
print(a)        #[[-1, 1, 4, 4], [-1, 1, 4, 4], [-1, 1, 4, 4], [-1, 1, 4, 4], [-1, 1, 4, 4]]

a = 'A list is an ordered collection of elements that can be accessed by their index or position.'.split()
print(a)
c=0
l=[]
for i in a:
    if i == 'elements':
        c = c + 1
        l.append(a.index(i))
print(c, '\n', l)

print(a.count('elements'))
if 'can' in a:
    print('present')
else:
    print('absent')

# INSERT
a = 'My name sonali sahebrao sangle'
b = a.split()
print(b)
b.insert(2, 'is')
print(b)
a1 = ' '.join(b)
print(a1)

# Sort using key
b.sort(key = len)   #will sort the list by len of elements
print(b)
a.sort(key = len, reverse= True)        #will sort the list by len of elements and reverse the list
print(a)
a.sort()
a=[1,27,4,86,9]
a.reverse()
c=reversed(a)
print(list(c))
print(sorted(a))


#///////--DICT--/////////
d = dict([(1, 'sonali'), (2, 'Hrishikesh'), (3, 'Hrishali'), (4, 'Saaransh')])
print(d)
for key in d:
    # print(f'{key} => {d[key]}')
    print(key)

for values in d.values():
    print(f'=> {values}')

for keys in d.keys():
    print(f'=> {keys}')

for items in d.items():         #will print tuple of key value pair
    print(f'=> {items}')

for key, value in d.items():       #customized key value pair
    print(f' {key} => {value}')


