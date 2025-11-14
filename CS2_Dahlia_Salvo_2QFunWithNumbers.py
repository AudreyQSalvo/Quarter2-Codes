#variables for the input and for accumulating the sum.
age = int(input("Hi there! Please enter your age: "))
sum_age = 0

#for loop for the total sum of all numbers from 1 up to the age of the user.
for i in range(1, age+1):
    sum_age += i

#display the answer
print(f"The sum of all numbers from 1 to {age} is: {sum_age}")