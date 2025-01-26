import pandas as pd
# import csv
file_path_1 = "C:\\Users\sosangle\Downloads\Dashboard_Data_AA.xlsx"
reading_excel = pd.read_excel(file_path_1, index_col=0, sheet_name='Assessments')
print(reading_excel)
reading_excel.to_csv('C:\\Users\sosangle\Downloads\Assessments.csv')
read_file1 = pd.read_csv("C:\\Users\sosangle\Downloads\Assessments.csv", skiprows=1)
print(read_file1)
print(read_file1.columns.values)


# //////////////////////
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
d3 = {}

for key in d1:
    if key in d2:
        d1[key] = d2[key] + d1[key]
    else:
        d1[key] = d2[key]
print(d1)


for key in d1.keys() | d2.keys():
    d3[key] = d1.get(key, 0) + d2.get(key, 0)
print(d3)



# //////////
l1 = [{'student_id':1, 'name': 'Jean Castro', 'class': 'V'}, {'student_id':2, 'name': 'Lull Powell', 'class': 'V'},
      {'student_id':3, 'name': 'Brain Howell', 'class': 'VI'}, {'student_id':4, 'name': 'Lynne Foster', 'class': 'VI'},
      {'student_id':5, 'name': 'Zachary Siman', 'class': 'VII'}]
l3=[]
l4=[]
for i in l1:
    # for k in i:
    l2 = list(i.values())
    l3.append(l2)
    l2 = list(i.values())[1:]
    l4.append(l2)
print(l3)
print(l4)

l4= []
for i in l1:
    for k in i:
        l2 = list(i.values())[1:]
    l4.append(l2)
print(l4)

l5 = []
for i in l3:
    l2 = i[1:]
    l5.append(l2)
print(l5)



# /////////
models = [{'make':'Nokia', 'model':216, 'color':'Black'}, {'make':'Mi Max', 'model':'2', 'color':'Gold'}, {'make':'Samsung', 'model': 7, 'color':'Blue'}]
print(models)
models_sort = sorted(models, key = lambda x: x['color'])
print(models_sort)

/////
L = [1, 2, 4, 4, 5, 6, 6, 6, 7, 8,8,8,8]
R = []
for i in L:
    if i not in R:
        R.append(i)
print(R)

/////////////////2nd last largest no

a = [3, 2, 1, 4, 5]
A = sorted(a)
print(A)
print(A[-2])


////////////////////////////////////////
# snake water gun
print("************ It's a Snake-Water-Gun Game ************")
import random

Game_list = ["Snake", "Water", "Gun"]
Comp_score = 0
User_score = 0
# turns = 10
x = 1
while (x <= 10):
    Comp_Choice = random.choice(Game_list)
    # print(Comp_Choice)
    User_choice = input("What is ur choice?\n"
                        "1. Snake\n"
                        "2. Water\n"
                        "3. Gun \n:-")

    if (Comp_Choice == "Snake" and User_choice == "Water") or \
            (Comp_Choice == "Gun" and User_choice == "Snake") or \
            (Comp_Choice == "Water" and User_choice == "Gun"):
        print("Ooops!, U loss")
        Comp_score += 1

    elif (Comp_Choice == "Snake" and User_choice == "Gun") or \
            (Comp_Choice == "Gun" and User_choice == "Water") or \
            (Comp_Choice == "Water" and User_choice == "Snake"):
        print("Congrats u won!")
        User_score += 1

    elif (Comp_Choice == User_choice):
        if x == 10:
            print("Sorry!,U choose same choice as computer and no. of turns are finished")
        else:
            print(" Try Again...U choose same choice as computer ")
    else:
        if x == 10:
            print("Sorry!,U have given wrong input and no of turns are finished")
        else:
            print("U have given wrong input")

    print("U have only ", 10 - x, "turns")
    x += 1
print("Computer Score is :", Comp_score)
print("Your Score is :", User_score)
if (Comp_score < User_score):
    print("Congrats u won the game by ", (User_score - Comp_score), "score points")
elif (Comp_score > User_score):
    print("Ooops!, Copmuter won the game by ", (Comp_score - User_score), "score points")
else:
    print("Ayyyooooo! , Laptop baba n tuza score same aahe***")
