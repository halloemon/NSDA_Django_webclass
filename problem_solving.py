# Print numbers from 1 to 20 using while loop

i = 1

while i <= 20:
    print(i)
    i += 1

# Print numbers from 1 to 20 using for loop

for i in range(1, 21):
    print(i)

# Print even numbers from 1 to 50

for i in range(1, 51):
    if i % 2 == 0:
        print(i)

# Print odd numbers from 1 to 50

for i in range(1, 51):
    if i % 2 != 0:
        print(i)
    
# 5. reverse 30–1
for i in range(30, 0, -1):
    print(i)

# 6. name 10 times
for i in range(10):
    print("Emon")

# 7. divisible by 3
for i in range(1, 101):
    if i % 3 == 0:
        print(i)

# 8. divisible by 5 and 7
for i in range(1, 101):
    if i % 5 == 0 and i % 7 == 0:
        print(i)

# 9. sum 1–50
total = 0
for i in range(1, 51):
    total += i
print(total)

# 10. sum even 1–100
total = 0
for i in range(1, 101):
    if i % 2 == 0:
        total += i
print(total)


# 11. table of 7
for i in range(1, 11):
    print(7 * i)


# 12. table of any number
n = int(input("Enter number: "))
for i in range(1, 11):
    print(n * i)

# 13. count even (1–200)
count = 0
for i in range(1, 201):
    if i % 2 == 0:
        count += 1
print(count)

# 14. count odd
count = 0
for i in range(1, 201):
    if i % 2 != 0:
        count += 1
print(count)

# 15. factorial
n = int(input("Enter number: "))
fact = 1
for i in range(1, n+1):
    fact *= i
print(fact)

# 16. reverse number
n = int(input())
rev = 0
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10
print(rev)

# 17. sum of digits
n = int(input())
sum = 0
while n > 0:
    sum += n % 10
    n //= 10
print(sum)

# 18. count digits
n = int(input())
count = 0
while n > 0:
    count += 1
    n //= 10
print(count)

# 19. square 1–15
for i in range(1, 16):
    print(i*i)

# 20. cube 1–12
for i in range(1, 13):
    print(i**3)

# 21. positive/negative/zero
n = int(input())
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")

# 22. even/odd
n = int(input())
if n % 2 == 0:
    print("Even")
else:
    print("Odd")

#22 Find the largest number among three numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest number is:", a)
elif b >= a and b >= c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)


