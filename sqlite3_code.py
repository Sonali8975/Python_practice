import sqlite3
conn = sqlite3.connect('my_database')
cursor = conn.cursor()
sql1 ='''create table salesman(salesman_id int(5),
        name char(30), 
        city char(35), 
        commission float(7, 2));'''
cursor.execute(sql1)

sql2 ='''insert into salesman values(1, "Sonali", "Nashik", 1.2),
                                    (2, "Devashree", "Mumbai", 0.9);'''
cursor.execute(sql2)

sql3 = '''select * from salesman;'''
cursor.execute(sql3)

sql4 = '''update salesman 
            set city = "Bangalore"
            where salesman_id = 1;'''
cursor.execute(sql4)

sql5 = '''delete from salesman
            where salesman_id = 2;'''

cursor.execute(sql5)
conn.close()





