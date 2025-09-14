# # # # # # # # # # # # # # # # list2 = ([1, 2, 3], [4, 8, 15], [-3, -8, 13])
# # # # # # # # # # # # # # # # for list in list2:
# # # # # # # # # # # # # # # #     print(list)
# # # # # # # # # # # # # # # #unpacking
# # # # # # # # # # # # # # # # a, b, c = [1,'hello', 5]
# # # # # # # # # # # # # # # # print(a)
# # # # # # # # # # # # # # # # print(b)
# # # # # # # # # # # # # # # # print(c)
# # # # # # # # # # # # # # # #unpacking
# # # # # # # # # # # # # # # # print(2 + 2)
# # # # # # # # # # # # # # # # print('2' + '2')
# # # # # # # # # # # # # # # # your list is [1, 2, 3]
# # # # # # # # # # # # # # # # make a new list where each item is twice as big as original
# # # # # # # # # # # # # # # #so I want to get [2, 4, 6]
# # # # # # # # # # # # # # # # original = [1, 2, 3]
# # # # # # # # # # # # # # # # newlist =[]
# # # # # # # # # # # # # # # # for item in original:
# # # # # # # # # # # # # # # #     newlist.append(2*item)
# # # # # # # # # # # # # # # from typing import Tuple
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # countries = [ 'Nepal', 'Vietnam', 'Iran', 'Morocco', 'Australia']
# # # # # # # # # # # # # # # # countries[1]= 'Finland'
# # # # # # # # # # # # # # # # print(countries)
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # Mylist = [1, 2, 3, 4, 5, 6, 7, 9, 10, 15]
# # # # # # # # # # # # # # # # if 7 in Mylist:
# # # # # # # # # # # # # # # #     print('7 is in the list')
# # # # # # # # # # # # # # # # else:
# # # # # # # # # # # # # # # #     print('no 7 in the list')
# # # # # # # # # # # # # # # # from random import randint
# # # # # # # # # # # # # # # # mylist =(randint(1,))
# # # # # # # # # # # # # # # # input('list three diffrent fruit')
# # # # # # # # # # # # # # # # Ask the user to enter 3 different fruits
# # # # # # # # # # # # # # # # fruits = []
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # for i in range(3):
# # # # # # # # # # # # # # # #     fruit = input(f"Enter fruit {i+1}: ")
# # # # # # # # # # # # # # # #     fruits.append(fruit)
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # Print the fruits as a list using a loop
# # # # # # # # # # # # # # # # print("Here are the fruits you entered:")
# # # # # # # # # # # # # # # # for fruit in fruits:
# # # # # # # # # # # # # # # #     print(fruit)
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # mylist = []
# # # # # # # # # # # # # # # # for i in range(3):
# # # # # # # # # # # # # # # #     fruit = input("Give me a fruit")
# # # # # # # # # # # # # # # #     mylist.append(fruit)
# # # # # # # # # # # # # # # # print(mylist)
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # countries = [ 'Nepal', 'Vietnam', 'Iran', 'Morocco', 'Australia', 'Russia', 'Bulgaria', 'Sirlanka', 'Ethiopia']
# # # # # # # # # # # # # # # # if 5 in countries
# # # # # # # # # # # # # # # # print('more then 5 letters')
# # # # # # # # # # # # # # # # # print a new list only containing 5 letter countries
# # # # # # # # # # # # # # # # countries = ['Nepal', 'Vietnam', 'Iran', 'Morocco', 'Australia', 'Russia', 'Bulgaria', 'Sirlanka', 'Ethiopia', 'Cambodia']
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # make a new list with only 5-letter countries
# # # # # # # # # # # # # # # # five_letter_countries = []
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # for country in countries:
# # # # # # # # # # # # # # # #     if len(country) == 5:  # check if the word has 5 letters
# # # # # # # # # # # # # # # #         five_letter_countries.append(country)
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # print("5-letter countries:", five_letter_countries)
# # # # # # # # # # # # # # # # countries = ['Nepal', 'Vietnam', 'Iran', 'Morocco', 'Australia', 'Russia', 'Bulgaria', 'Sirlanka', 'Ethiopia']
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # five_letter_countries = [country for country in countries if len(country) == 5]
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # print("5-letter countries:", five_letter_countries)
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # countries = ['Nepal', 'Vietnam', 'Iran', 'Morocco', 'Australia', 'Russia', 'Bulgaria', 'Sirlanka', 'Ethiopia']
# # # # # # # # # # # # # # # # Mylist = []
# # # # # # # # # # # # # # # # for country in countries:
# # # # # # # # # # # # # # # #    if len(country) > 5:
# # # # # # # # # # # # # # # #        Mylist.append(country)
# # # # # # # # # # # # # # # # print('5 letter countries:', Mylist)
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # write a program that operates on a list of numbers.
# # # # # # # # # # # # # # # # The output is the numbers which are even
# # # # # # # # # # # # # # # #  the expected out put is [6, 8,48]
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # number_list = [6,15,19,8,21,48,17]
# # # # # # # # # # # # # # # # x = []
# # # # # # # # # # # # # # # # if x in number_list:
# # # # # # # # # # # # # # # #     if x % 2 == 0:
# # # # # # # # # # # # # # # # print(x)
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # This is how to remover number 5 from the list and print a new list
# # # # # # # # # # # # # # # # nums = [2, 5, 10, 5, -8, 12, 5, 15]
# # # # # # # # # # # # # # # # empty_list = []
# # # # # # # # # # # # # # # # for number in nums:
# # # # # # # # # # # # # # # #     if number != 5:
# # # # # # # # # # # # # # # #         empty_list.append(number)
# # # # # # # # # # # # # # # # print(empty_list)
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # mylis.remove(5)
# # # # # # # # # # # # # # # # print(mylis)
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # if number in number_list:
# # # # # # # # # # # # # # # # a = [2, 5, 10, 5, -8, , 70]
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # Elements to remove
# # # # # # # # # # # # # # # # remove = [20, 40, 60]
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # Remove elements using list comprehension
# # # # # # # # # # # # # # # # a = [x for x in a if x not in remove]
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # print(a)
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # ---Tuple---
# # # # # # # # # # # # # # # # ChatGPT said:
# # # # # # # # # # # # # # # # # A tuple is an ordered collection of values, written in parentheses (e.g., ('apple', 5, 1.99)), and once created it cannot be changed. In databases, each row returned is essentially a tuple of column values.
# # # # # # # # # # # # # # # # indexing, slicing, unpacking,
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # A tuple is an ordered, immutable collection of values (e.g., t = (10, 20, 30)), where you can access items by indexing (t[0] → 10), take parts using slicing (t[0:2] → (10, 20)), and assign values to variables using unpacking (a, b, c = t).
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # mylist = [1, 2, 3]
# # # # # # # # # # # # # # # # mytuple= (1, 2, 3)
# # # # # # # # # # # # # # # # print(mylist, id(mylist))
# # # # # # # # # # # # # # # # print(mytuple,id(mylist))
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # mylist.append(4)
# # # # # # # # # # # # # # # # mytuple = (1, 2, 3, 4)
# # # # # # # # # # # # # # # # print(mylist, id(mylist))
# # # # # # # # # # # # # # # # print(mytuple,id(mytuple))
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # mytuple = (1, 2, 10, 15, 18, -25, 200)
# # # # # # # # # # # # # # # # print()
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # mytuple = (1, 2, 10, 15, 18, -25, 200, -10, 90, 82)
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # convert to list
# # # # # # # # # # # # # # # # temp = list(mytuple)
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # remove 18
# # # # # # # # # # # # # # # # temp.remove(18)
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # convert back to tuple
# # # # # # # # # # # # # # # # mytuple = tuple(temp)
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # print(mytuple)
# # # # # # # # # # # # # # # # ---------------------------------------------------------
# # # # # # # # # # # # # # # #remove number, 4 start, to 8 but not including 8th spot
# # # # # # # # # # # # # # # # mytuple = (1, 2, 10, 15, 18, -25, 200, -10, 90, 82)
# # # # # # # # # # # # # # # # print((mytuple [4:8]))
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # mytuple = (1, 2, 10, 15, 18, -25, 200, -10, 90, 82)
# # # # # # # # # # # # # # # # # check if #18 is an item of the tuple
# # # # # # # # # # # # # # # # print(18 in mytuple)
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # t2 = (4, 8, 9)
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # a, b, c = t2
# # # # # # # # # # # # # # # # print(t2)
# # # # # # # # # # # # # # # #define three vairables and assign them as follows:
# # # # # # # # # # # # # # # # a = 4
# # # # # # # # # # # # # # # # b = 8
# # # # # # # # # # # # # # # # c = 9
# # # # # # # # # # # # # # # # how to select #90 from the list
# # # # # # # # # # # # # # # # t2 = (4, 8, [1, 2, 3,], [5, -8, 90, 12])
# # # # # # # # # # # # # # # # print(t2[3][2])
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # extra: Counter
# # # # # # # # # # # # # # # # import random
# # # # # # # # # # # # # # # # for _ in range(10):
# # # # # # # # # # # # # # # #     num = random.randint(1, 6)
# # # # # # # # # # # # # # # #     print(num)
# # # # # # # # # # # # # # # #     if num == 6:
# # # # # # # # # # # # # # # #         counter + = 1
# # # # # # # # # # # # # # # #     print(f'you got {count} times')
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # Make a python program that counts how many 5's are in a tuple.
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # t = (2, 5, 7, 8, 5, 9, 6, -10, 5)
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # count = 0
# # # # # # # # # # # # # # # # for number in t:
# # # # # # # # # # # # # # # #     if number == 5:
# # # # # # # # # # # # # # # #         count += 1
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # print(count)
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # t = (2, 5, 6)
# # # # # # # # # # # # # # # # lt = list(t)
# # # # # # # # # # # # # # # # # print(lt)
# # # # # # # # # # # # # # # # t1 = (2, 3, 4)
# # # # # # # # # # # # # # # # t2 = (4, 5, 6)
# # # # # # # # # # # # # # # # t3 = (6, 8, 9)
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # print(t1[0:1:2] + t2[0:1:2])
# # # # # # # # # # # # # # # # import mysql.connector
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # import mysql.connector
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # print("MySQL driver is installed and working!")
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # import mysql.connector
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # connection = mysql.connector.connect(
# # # # # # # # # # # # # # # #          host='127.0.0.1',
# # # # # # # # # # # # # # # #          port= 3306,
# # # # # # # # # # # # # # # #          database='people',
# # # # # # # # # # # # # # # #          user='dbuser',
# # # # # # # # # # # # # # # #          password='pAs5w_0rD',
# # # # # # # # # # # # # # # #          autocommit=True
# # # # # # # # # # # # # # # #          )
# # # # # # # # # # # # # # # import mysql.connector
# # # # # # # # # # # # # # # from mysql.connector import errorcode
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # try:
# # # # # # # # # # # # # # #     connection = mysql.connector.connect(
# # # # # # # # # # # # # # #         host="127.0.0.1",
# # # # # # # # # # # # # # #         port=3306,
# # # # # # # # # # # # # # #         user="dbuser",
# # # # # # # # # # # # # # #         password="pAsSw_0rD",
# # # # # # # # # # # # # # #         database="people",
# # # # # # # # # # # # # # #         autocommit=True,
# # # # # # # # # # # # # # #     )
# # # # # # # # # # # # # # #     print("✅ Connected successfully!")
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #     cursor = connection.cursor()
# # # # # # # # # # # # # # #     cursor.execute("SELECT DATABASE();")
# # # # # # # # # # # # # # #     print("Current database:", cursor.fetchone())
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # except mysql.connector.Error as err:
# # # # # # # # # # # # # # #     if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
# # # # # # # # # # # # # # #         print("❌ Access denied: check username or password")
# # # # # # # # # # # # # # #     elif err.errno == errorcode.ER_BAD_DB_ERROR:
# # # # # # # # # # # # # # #         print("❌ Database does not exist")
# # # # # # # # # # # # # # #     else:
# # # # # # # # # # # # # # #         print("❌ MySQL Error:", err)
# # # # # # # # # # # # # # # finally:
# # # # # # # # # # # # # # #     try:
# # # # # # # # # # # # # # #         cursor.close()
# # # # # # # # # # # # # # #         connection.close()
# # # # # # # # # # # # # # #     except:
# # # # # # # # # # # # # # #         pass
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # import mysql.connector
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # def get_employees_by_last_name(last_name):
# # # # # # # # # # # # # #     sql = f"SELECT Number, Last_name, First_name, Salary FROM Employee WHERE Last_name='{last_name}'"
# # # # # # # # # # # # # #     print(sql)
# # # # # # # # # # # # # #     cursor = connection.cursor()
# # # # # # # # # # # # # #     cursor.execute(sql)
# # # # # # # # # # # # # #     result = cursor.fetchall()
# # # # # # # # # # # # # #     if cursor.rowcount >0 :
# # # # # # # # # # # # # #         for row in result:
# # # # # # # # # # # # # #             print(f"Hello! I'm {row[2]} {row[1]}. My salary is {row[3]} euros per month.")
# # # # # # # # # # # # # #     return
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # # Main program
# # # # # # # # # # # # # # connection = mysql.connector.connect(
# # # # # # # # # # # # # #          host='localhost',
# # # # # # # # # # # # # #          port= 3306,
# # # # # # # # # # # # # #          database='people',
# # # # # # # # # # # # # #          user='dbuser',
# # # # # # # # # # # # # #          password='pAs5w_0rD',
# # # # # # # # # # # # # #          autocommit=True
# # # # # # # # # # # # # #          )
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # last_name = input("Enter last name: ")
# # # # # # # # # # # # # # get_employees_by_last_name(last_name)
# # # # # # # # # # # # # connection = mysql.connector.connect(
# # # # # # # # # # # # #     host="localhost",   # instead of 127.0.0.1
# # # # # # # # # # # # #     port=3306,
# # # # # # # # # # # # #     user="dbuser",
# # # # # # # # # # # # #     password="pAsSw_0rD",
# # # # # # # # # # # # #     database="people",
# # # # # # # # # # # # #     autocommit=True
# # # # # # # # # # # # # )
# # # # # # # # # # # # import mysql.connector   # <-- add this back
# # # # # # # # # # # #
# # # # # # # # # # # # connection = mysql.connector.connect(
# # # # # # # # # # # #     host="localhost",    # instead of 127.0.0.1
# # # # # # # # # # # #     port=3306,
# # # # # # # # # # # #     user="dbuser",
# # # # # # # # # # # #     password="pAsSw_0rD",
# # # # # # # # # # # #     database="people",
# # # # # # # # # # # #     autocommit=True
# # # # # # # # # # # # )
# # # # # # # # # # # #
# # # # # # # # # # # # print("✅ Connected to people database as dbuser")
# # # # # # # # # # # import mysql.connector
# # # # # # # # # # #
# # # # # # # # # # # def get_employees_by_last_name(last_name):
# # # # # # # # # # #     sql = f"SELECT Number, Last_name, First_name, Salary FROM Employee WHERE Last_name='{last_name}'"
# # # # # # # # # # #     print(sql)
# # # # # # # # # # #     cursor = connection.cursor()
# # # # # # # # # # #     cursor.execute(sql)
# # # # # # # # # # #     result = cursor.fetchall()
# # # # # # # # # # #     if cursor.rowcount > 0:
# # # # # # # # # # #         for row in result:
# # # # # # # # # # #             print(f"Hello! I'm {row[2]} {row[1]}. My salary is {row[3]} euros per month.")
# # # # # # # # # # #     return
# # # # # # # # # # #
# # # # # # # # # # # # Main program
# # # # # # # # # # # connection = mysql.connector.connect(
# # # # # # # # # # #          host='localhost',      # ✅ use localhost
# # # # # # # # # # #          port=3306,
# # # # # # # # # # #          database='people',
# # # # # # # # # # #          user='dbuser',
# # # # # # # # # # #          password='pAsSw_0rD',  # ✅ fixed password
# # # # # # # # # # #          autocommit=True
# # # # # # # # # # # )
# # # # # # # # # # #
# # # # # # # # # # # last_name = input("Enter last name: ")
# # # # # # # # # # # get_employees_by_last_name(last_name)
# # # # # # # # # # import mysql.connector
# # # # # # # # # #
# # # # # # # # # # def get_employees_by_last_name(last_name):
# # # # # # # # # #     sql = f"SELECT Number, Last_name, First_name, Salary FROM Employee WHERE Last_name='{last_name}'"
# # # # # # # # # #     print(sql)
# # # # # # # # # #     cursor = connection.cursor()
# # # # # # # # # #     cursor.execute(sql)
# # # # # # # # # #     result = cursor.fetchall()
# # # # # # # # # #     if cursor.rowcount > 0:
# # # # # # # # # #         for row in result:
# # # # # # # # # #             print(f"Hello! I'm {row[2]} {row[1]}. My salary is {row[3]} euros per month.")
# # # # # # # # # #     return
# # # # # # # # # #
# # # # # # # # # # # Main program
# # # # # # # # # # connection = mysql.connector.connect(
# # # # # # # # # #     host='localhost',      # <-- IMPORTANT
# # # # # # # # # #     port=3306,
# # # # # # # # # #     database='people',
# # # # # # # # # #     user='dbuser',
# # # # # # # # # #     password='pAsSw_0rD',  # <-- IMPORTANT
# # # # # # # # # #     autocommit=True
# # # # # # # # # # )
# # # # # # # # # #
# # # # # # # # # # last_name = input("Enter last name: ")
# # # # # # # # # # get_employees_by_last_name(last_name)
# # # # # # # # # def update_salary(number, new_salary):
# # # # # # # # #     sql = f"UPDATE Employee SET Salary={new_salary} WHERE Number={number}"
# # # # # # # # #     print(sql)
# # # # # # # # #     cursor = connection.cursor()
# # # # # # # # #     cursor.execute(sql)
# # # # # # # # #     if cursor.rowcount == 1:
# # # # # # # # #         print("Salary updated")
# # # # # # # # #     else:
# # # # # # # # #         print("No row updated (check the Number).")
# # # # # # # # number = int(input("Enter number: "))
# # # # # # # # new_salary = float(input("Enter new salary: "))
# # # # # # # # update_salary(number, new_salary)
# # # # # # # import mysql.connector
# # # # # # #
# # # # # # # def get_employees_by_last_name(last_name):
# # # # # # #     sql = f"SELECT Number, Last_name, First_name, Salary FROM Employee WHERE Last_name='{last_name}'"
# # # # # # #     print(sql)
# # # # # # #     cursor = connection.cursor()
# # # # # # #     cursor.execute(sql)
# # # # # # #     result = cursor.fetchall()
# # # # # # #     if cursor.rowcount > 0:
# # # # # # #         for row in result:
# # # # # # #             print(f"Hello! I'm {row[2]} {row[1]}. My salary is {row[3]} euros per month.")
# # # # # # #     return
# # # # # # #
# # # # # # # def update_salary(number, new_salary):   # <-- must be defined before use
# # # # # # #     sql = f"UPDATE Employee SET Salary={new_salary} WHERE Number={number}"
# # # # # # #     print(sql)
# # # # # # #     cursor = connection.cursor()
# # # # # # #     cursor.execute(sql)
# # # # # # #     if cursor.rowcount == 1:
# # # # # # #         print("Salary updated")
# # # # # # #     else:
# # # # # # #         print("No row updated (check the Number).")
# # # # # # #
# # # # # # # # Main program
# # # # # # # connection = mysql.connector.connect(
# # # # # # #     host='localhost',
# # # # # # #     port=3306,
# # # # # # #     database='people',
# # # # # # #     user='dbuser',
# # # # # # #     password='pAsSw_0rD',
# # # # # # #     autocommit=True
# # # # # # # )
# # # # # # # 
# # # # # # # last_name = input("Enter last name: ")
# # # # # # # get_employees_by_last_name(last_name)
# # # # # # #
# # # # # # # number = int(input("Enter number: "))
# # # # # # # new_salary = float(input("Enter new salary: "))
# # # # # # # update_salary(number, new_salary)
# # # # # # # numbers = [5, 9, 15, 3, 1, -8, 18]
# # # # # # # numbers.sort()
# # # # # # # print(numbers)
# # # # # # numbers2 = (5, 9, 15, 3, 1, -8, 18)
# # # # # # # print(numbers + numbers)
# # # # # # num2 =list(numbers2)
# # # # # # num2.sort()
# # # # # # num3 = tuple(num2)
# # # # # # print(num3)
# # # # #
# # # # # #in a SET you cant have the same element
# # # # # # lis = [2,3,2.42, (2,6,7), True, [5, 8, 22], 2, 8]
# # # # # # print(lis)
# # # # # # -----------------------------------------------------------------------------SET-------------------
# # # # # myset = {2, 5, 7}
# # # # # myset2 = {3,4}
# # # # # myset3 = myset | myset2
# # # # # print(myset3)
# # # # # #  use | example myset | myset2 = mysetmyset2
# # # # #
# # # # # emptset = set()
# # # # # list(), []
# # # # # tuple()
# # # # # str(''), ''
# # # # # set()
# # # #
# # # # games = {"Monopoly", "Chess", "Cluedo"}
# # # # print(games)
# # # #
# # # # games.add("Dominion")
# # # # print(games)
# # # #
# # # # games.remove("Chess")
# # # # print(games)
# # # #
# # # # games.add("Cluedo")
# # # # print(games)
# # # #
# # # # for g in games:
# # # #     print(g)
# # # # ------MATH------
# # # def f(x):
# # #     y = 2*x + 1
# # #     return y
# # #
# # # a = f(20)
# # # print(a)
# # def change_nymber(n):
# #     n = n +5
# #     print(f"Inside chage_number: n = {n}n")
# # def change_list(lst):
# #     lst.append(99)
# #     print(f"inside change_list: lst = {lst}")
# #
# # x = 10
# # number = [2,17,25,13]
# #
# # print('')
# # change_number(x)
# # change_list(numbers)
# #
# # print(20*'=')
# # print(f"After change_number: x = {x}")
# #print only even numbers
# # Moduel 1 and 2
# # lst1 = [1, 6, 18, 5, -5, 90, 37]
# #
# # def f()
# #     y = 1+1
# #     return y
# # print(f)
# #
# # numbers = {"Viivi}: 050-1234567",
# #           "Ahmed:040-1112223",
# #           "Pekka: 050-7654321"}
# #
# # for item in numbers:
# #     print(item)
#
# # numbers = {"viivi":"050-03245642",
# #            "ahmed":"010-12335643",
# #            "pekka":"070-21046069"} #this is a dictionary/dict viivi etc is a key not an index the numbers are values
# #
# # numbers["ahmed"] = "050-1234568" #way to replace value of a key
# # numbers["george"] = "040-7525252" #way to add a key and value to the dictionary
# # print(numbers)
# # print(numbers["ahmed"])
# # print(f"pekka's number is {numbers['pekka']}")
# #
# # for item in numbers:
# #     #print(item)
# #     print(numbers[item])
# #The program asks for the phone number, is it exists say sweet if not say it dosnt
#
# # numbers = {"viivi":"050-03245642",
# #            "ahmed":"010-12335643",
# #            "pekka":"070-21046069",
# #            "George":"040-7525252"}
# #
# # input("What is your phone number?")
# # for list in numbers:
# #     if (number) + (f"050-03245642")) == True:
# #     print(numbers)
#
#
# numbers = {"viivi":"050-03245642",
#            "ahmed":"010-12335643",
#            "pekka":"070-21046069",
#            "George":"040-7525252"}
# # ask for input
# phone = input("what is your phone number:")
# for item in numbers:
#     if numbers[item] == phone:
#      print(f"{phone} is {item}'s number")
# else:
#     print("ahaha")
# #Check if itme exists in list, using a loop = if statement.
#
#
#
# #
# # # check if number exists in dictionary values
# # if number in numbers.values():
# #     print("Sweet! That number exists.")
# # else:
# #     print("Sorry, that number doesn't exist.")
#
#
# # function to remove odd numbers
# def remove_odds(numbers):
#     evens = []
#     for n in numbers:
#         if n % 2 == 0:   # check if even
#             evens.append(n)
#     return evens
#
# # main program
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# new_list = remove_odds(my_list)
#
# print("Original list:", my_list)
# print("Even numbers only:", new_list)
# original = [1, 2, 3]
# # # # # # # # # # # # # # # # # newlist =[]
# # # # # # # # # # # # # # # # # for item in original:
# # # # # # # # # # # # # # # # #     newlist.append(2*item)
#You need to add each member of t1 added to corresponding member of t2
t1 = (1, 2, 3)
t2 = (4, 5, 6)
#both lists
t3 =

print(t3)