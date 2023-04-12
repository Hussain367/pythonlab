Numbers=[]
print('Enter 10 numbers =\n') 
for i in range(10):
    num = int(input('Enter number'))
    Numbers.append(num)

even_num = [num for num in Numbers if num % 2 == 0]
print("The list of all numbers is =", Numbers)
print("The even numbers are =", even_num)

sum_even = sum(even_num)
print("The sum of even numbers", sum_even)