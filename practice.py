d = {"a": 1, "b": 2.875626, "c": 4, "e": 6, "ab": 7}
c = {"a": 1, "b": 2.875626, "c": 4.758468, "e": 6, "ab": 7}

def fun(d):
    d['b'] = round(d['b'], 2)
    return d
print(fun(d))

def fun(dict, key):
    dict[key] = round(dict[key], 2)
    return dict
print(fun(c, 'c'))
print(d)

d['b'] = round(d['b'], 2)
print(d)

///////////////////////////////////
d = {"a": 1, "b": 2.875626, "c": 4, "e": 6, "ab": 7}
a = ["a", "b", "e", "ab"]
b = 0
for k in d.keys():
    for e in a:
        if k == e:
            b += 1
            break
print(b)

///////////////////////////
x="Go"
if(x=="Go"):
  print('Go ')

else:
  print('Stop')
print('Mike')

/////////////////////

x=5
while(x!=2):
  print(x)
  x=x-1


class Points(object):
  def __init__(self,x,y):
    self.x=x
    self.y=y

  def print_point(self):
    print('x=',self.x,' y=',self.y)

p2=Points(1,2)
p2.x='A'
p2.print_point()


a=1
def do(x):
    a=100
    return(x+a)
print(do(1))


fruit = 'Banana'
fruit[0] = 'b'
print(fruit)

my_list = [1, 3, 5, 7, 9]
my_list.reverse()
print(my_list.reverse())


a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(len(c))


class Points(object):
  def __init__(self,x,y):
    self.x=x
    self.y=y

  def print_point(self):
    print('x=',self.x,' y=',self.y)
p1=Points(1,2)
p1.print_point()


class Points(object):
  def __init__(self,x,y):
    self.x=x
    self.y=y

  def print_point(self):
    print('x=',self.x,' y=',self.y)

p2=Points(1,2)
p2.x=2
p2.print_point()


x="A"
if(x=="A"):
  print('Hello')
else:
  print('Hi')
print('Mike')

my_list = [1, 3, 5, 7, 9]
print(my_list[0:4])
print(my_list[2:-1])
print(my_list[3:-1])
print(my_list[::-1])


a = 5
for a in range(12):
    val = (a*2)-3
print(val)

num = 5
a = 0
for a in range(0,12):
    num = (num*2)-3
print(num)


print(list(range(0, 4, 1)))
print(list(range(0, 5, 1)))
print(list(range(0, 5)))
print(range(0, 5))


L = [[1, 3, 5], [2, 4, 5], [4, 0, 8]]
def get_diagonal_and_non_diagonal(L):
    diagonal = []
    non_diagonal = []
    for row in range(len(L)):
        for col in range(len(L)):
            if row == col:
                diagonal.append(L[row][row])
            elif row != col:
                non_diagonal.append(L[row][col])
    return (diagonal, non_diagonal)

print(get_diagonal_and_non_diagonal(L))


import string
list1 = ["Hello", "World"]
print(list1[-1])
def string_processing(string_list):
    var = ""
    for i in string_list:
        var = var + i.lower() + " "
    return var
print(string_processing(list1))



def minion_game(string):
    # your code goes here
    vowel = "AEIOU"
    ss = 0
    ks = 0
    l = len(string)
    for i in range(l):
        if string[i] in vowel:
            ks += l - i
        else:
            ss += l - i
    if ss > ks:
        print("Stuart", str(ss))
    elif ks > ss:
        print("Kevin", str(ks))
    else:
        print("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)

# Add two lists using map and lambda

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))

# List of strings
l = ['sat', 'bat', 'cat', 'mat']
# map() can listify the list of strings individually
test = list(map(list, l))
print(test)
t1 = map(list, l)
print(list(t1))



n = int(input())
arr = map(int, input().split())
b = list(arr).sort()
print(list(arr))


print(1/2)
print(1//2)


x= 1
if(x!=1):
     print('Hello')
else:
     print('Hi')
print('Mike')


# /////
def print_rangoli(size):
    # your code goes here
    import string
    design = string.ascii_lowercase

    L = []
    for i in range(n):
        s = "-".join(design[i:n])
        L.append((s[::-1]+s[1:]).center(4*n-3, "-"))

    print('\n'.join(L[:0:-1]+L))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

# /////////////factorial
# no of ways to drop 3 fruit from 8
from math import factorial as fac
n = 8
k = 3

ways = fac(n) / (fac(k) * fac(n-k))
print(ways)
ways1 = fac(n) // (fac(k) * fac(n-k))
print(ways1)
fac(100)
len(str(fac(1000)))



# ////////////////////////////
n = int(input())
integer_list = map(int, input().split())
t = ()
for i in n:
    t.append(integer_list)

print(t)


# /////////////////////////////////////////
def CheckLeap(Year):
  if((Year % 400 == 0) or
     (Year % 100 != 0) and
     (Year % 4 == 0)):
    print("Yes");
  else:
    print ("No")
Year = int(input())
CheckLeap(Year)

# /////////////////
def greet(name):
    print(f"Hello, {name}!")
    return "Hello Jyoti!"

greet("Alice")

x = int(98.6)
print(x)


# to print the freq of each element
L=[6,5,7,4,2,2,5,6,6,6,2,9,1]
freq = {}
for i in L:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
for num, count in freq.items():
    print(f"{num} comes {count} times")


while True:
    name = input('Enter your name: ')
    if name == 'Sonali':
        break
    print('Hello!!')
print(f'Hello {name}')

# ////////////////////////////////////////
count = 0
avg = 0
sum = 0.0
while True:
    num = input("Enter the number: ")
    if num == 'done':
        break
    try:
        fnum = float(num)
    except:
        print("Invalid Input...")
    # print(fnum)
    count = count + 1
    sum = sum + fnum
print(f'Sum is:{sum} \n Count is: {count} \n Avg is: {sum/count}')



/////////////////////////////////////////////////////////
larg = None
small = None
while True:
    num = input("Enter the number: ")
    if num == 'done':
        break
    try:
        inum = int(num)
    except:
        print("Invalid input")
    if larg is None or small is None:
        larg = inum
        small = inum
    elif inum > larg:
        larg = inum
    elif inum < small:
        small = inum
print(f'Maximum is {larg}\nMinimum is {small}')
