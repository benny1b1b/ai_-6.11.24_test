#1
import statistics
#
num1: float = float(input("enter a number: "))
num2: float = float(input("enter a number: "))
for i in range(3):
    print(min(num1,num2))

#2

num1_2: int = int(input("enter a number: "))
num2_2: int = int(input("enter a number: "))
avg: float = (num1_2 + num2_2) / 2
print(avg)

#3

num1_3: float = float(input("enter a number: "))
num2_3: float = float(input("enter a number: "))
num3_3: float = float(input("enter a number: "))
print(max(num1_3,num2_3,num3_3))

#4

movie_length_in_min: int = int(input("How many minutes is the movie? "))
hours: int = movie_length_in_min //60
last_minutes: int = movie_length_in_min %60

print(f"{hours} hour(s) and {last_minutes} minute(s)")


#5

num_4_digit: int= int(input("enter 4 digit number: "))
print(num_4_digit % 10)

#6
num_4_digit_6: int= int(input("enter 4 digit number: "))
print(num_4_digit_6// 10 % 10)

#7
number:int  = int(input("enter 2 digit number: "))

ahadot: int = number % 10
asarot: int = number // 10
sum_digit: int = ahadot + asarot
print(f"this number {number} the sum digit is {sum_digit}")

#9

SENTINEL: int = 0

while True:
    try:
        num: int = int(input("enter a number:"))
        if num == SENTINEL:
            break
        if num %2 == 0:
            print("even")
        else:
            print("odd")
    except ValueError as e:
        print(e)

#10

salary = int(input("enter salary :"))
tax: float = 0
origin = salary
while True:
    if origin < 6_000:
        tax = 0
        break
    else:
        salary -= 6_000
    if origin > 12_000:
        tax += 6_000 * 0.1
        salary -= 6_000
    else:
        tax += salary * 0.1
        break
    if origin > 18_000:
        tax += 6_000 * 0.2
        salary -= 6_000
    else:
        tax += salary * 0.2
        break
    if origin > 25_000:
        tax += 7_000 * 0.3
        salary -= 7_000
    else:
        tax += salary * 0.3
        break
    if origin > 35_000:
        tax += 10_000 * 0.4
        salary -= 10_000
    else:
        tax += salary * 0.4
        break
    if origin > 50_000:
        tax += 15_000 * 0.45
        salary -= 15_000
    else:
        tax += salary * 0.45
        break
    if origin > 50_000:
        tax += salary * 0.51
        break
print(f" Total tax for your {origin} are : {tax}")

#loops

#1

top: int = int(input("enter a top number: "))
list1_top: list = [i for i in range(1,top) if i > 0]
print(list1_top)

#2
num1: int = int(input("enter a number: "))
num2: int = int(input("enter a number: "))
for number in range(num1, num2 + 1):
    print(number, end=" ")
if num1 > num2:
    for number in range(num2, num1 + 1):
        print(number, end=" ")
else:
    print(f"same numbers")

#עיבןד נתונים

#1
number: int = 0
sum_numbers: int = 0
SENTINEL: int = -99
while True:
    number= int(input("enter a number: "))
    if number ==SENTINEL:
        break
    if sum_numbers is None:
       sum_numbers = 0
    sum_numbers += number

print(sum_numbers)

#2
max_number: int = None
min_number: int = None
while True:
    number: int = int(input("enter a number: "))
    if number <= 0 or number == SENTINEL:
        break
    if max_number is None or max_number < number:
        max_number = number
    if min_number is None or min_number > number:
        min_number = number
print(f"maximum number is: {max_number}")
print(f"minimum number is: {min_number}")

#3

list_5_num: list[int] = [int(input("enter a number: ")) for i in range(5)]
print(max(list_5_num))


#לולאות מורכבות

import statistics


temperature: float = -1
total: int = 12
list_temp: list[float] = []
while len(list_temp) < total:
    try:
        temperature = float(input("enter temperature:"))
        if temperature < -5 or temperature > 40:# if invalid data , stop and print only!
            print("wrong data")
            break
        print("correct data")
        if not temperature and( list_temp and not list_temp[len(list_temp) - 1]):
            continue
        list_temp.append(temperature)
    except ValueError as e :
        print(e)
    except Exception as e:
        print(e)
else:
    if list_temp:
        print("avg:", statistics.mean(list_temp))
        print("max:", max(list_temp))
        print("min:", min(list_temp))


