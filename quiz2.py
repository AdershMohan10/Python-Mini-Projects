import time

mark = 0

# ---------------------- Q1 ----------------------
print('A. Which planet is known as The Red Planet?')
print('1. Venus\n2. Mars\n3. Jupiter\n')
start = time.time()
ans1 = int(input("Enter your answer: "))
end = time.time()

if end - start <= 3 and ans1 == 2:
    mark += 1
else:
    print("⏰ Time’s up or wrong answer!")

# ---------------------- Q2 ----------------------
print('\nB. What is the capital of Japan?')
print('1. Tokyo\n2. Osaka\n3. Kyoto\n')
start = time.time()
ans2 = int(input("Enter your answer: "))
end = time.time()

if end - start <= 3 and ans2 == 1:
    mark += 1
else:
    print("⏰ Time’s up or wrong answer!")

# ---------------------- Q3 ----------------------
print('\nC. Which data type is immutable in Python?')
print('1. List\n2. Dictionary\n3. Tuple\n')
start = time.time()
ans3 = int(input("Enter your answer: "))
end = time.time()

if end - start <= 3 and ans3 == 3:
    mark += 1
else:
    print("⏰ Time’s up or wrong answer!")

# ---------------------- Q4 ----------------------
print('\nD. Who developed the theory of relativity?')
print('1. Isaac Newton\n2. Albert Einstein\n3. Galileo Galilei\n')
start = time.time()
ans4 = int(input("Enter your answer: "))
end = time.time()

if end - start <= 3 and ans4 == 2:
    mark += 1
else:
    print("⏰ Time’s up or wrong answer!")

# ---------------------- Q5 ----------------------
print('\nE. What is the chemical symbol for gold?')
print('1. Au\n2. Ag\n3. Gd\n')
start = time.time()
ans5 = int(input("Enter your answer: "))
end = time.time()

if end - start <= 3 and ans5 == 1:
    mark += 1
else:
    print("⏰ Time’s up or wrong answer!")

# ---------------------- Result ----------------------
print("\n====================")
print("Total Marks:", mark)
print("====================")
        

# 2 1 3 2 12