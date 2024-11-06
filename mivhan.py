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
num:int  = int(input("enter 2 digit number: "))

ahadot: int = num % 10
asarot: int = num//10
sum_digit: int = ahadot + asarot
print(f"this number {num} the sum digit is {sum_digit}")

#loops

#1

top: int = int(input("enter a top number: "))
list1_top: list = [i for i in range(1,top) if i > 0]
print(list1_top)

2
num1: int = int(input("enter a number: "))
num2: int = int(input("enter a number: "))
for num in range(num1, num2 + 1):
    print(num, end= " ")
if num1 > num2:
    for num in range(num2, num1 + 1):
        print(num, end=" ")
else:
    print(f"same numbers")

#עיבןד נתונים

#1
num: int = 0
sum_numbers: int = 0
SENTINEL: int = -99
while True:
    num= int(input("enter a number: "))
    if num ==SENTINEL:
        break
    else:
        sum_numbers += num
print(sum_numbers)

#2
max_number: int = 1
min_number: int = 100
while True:
    num: int = int(input("enter a number: "))
    if num <= 0:
        break
    if num > max_number:
        max_number = num
    if num < min_number:
        min_number = num
print(f"maximum number is: {max_number}")
print(f"minimum number is: {min_number}")

#3

list_5_num: list[int] = [int(input("enter a number: ")) for i in range(5)]
print(max(list_5_num))

#לולאות מורכבות

