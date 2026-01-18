# Fibonacci series using while loop

n = int(input("Enter how many terms you want: "))

a  = 0
b = 1
count = 0

print("Fibonacci Series:")

while count < n:
    print(a, end=" ")
    a, b = b, a + b
    count += 1
