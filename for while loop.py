#1.Print numbers from 1 to 100
for i in range(1, 101):
    print(i)

#2.Print all even numbers between 1 to 50
for i in range(1, 51):
    if i % 2 == 0:
        print(i)

#3.Sum of first n natural numbers
n = int(input("Enter n: "))
total = 0
for i in range(1, n+1):
    total += i
print(total)

#4.Multiplication table
num = int(input("Enter number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num*i)

#5.Print all elements of a list
lst = [10, 20, 30, 40]
for i in lst:
    print(i)

#6.Count vowels in a string
s = input("Enter string: ")
count = 0
for ch in s:
    if ch.lower() in "aeiou":
        count += 1
print(count)

#7.Largest number in a list
lst = [10, 5, 80, 25]
largest = lst[0]
for i in lst:
    if i > largest:
        largest = i
print(largest)

#8.Prime numbers between 1 and 100
for num in range(2, 101):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    if prime:
        print(num)

#9.Factorial using for loop
n = int(input("Enter number: "))
fact = 1
for i in range(1, n+1):
    fact *= i
print(fact)

#10.Reverse a string
s = input("Enter string: ")
rev = ""
for ch in s:
    rev = ch + rev
print(rev)

#--- WHILE LOOP Programs -----

#11.Print numbers 1 to 50
i = 1
while i <= 50:
    print(i)
    i += 1

#12.Print odd numbers
i = 1
while i <= 50:
    if i % 2 != 0:
        print(i)
    i += 1

#13.Sum of digits
n = int(input("Enter number: "))
s = 0
while n > 0:
    s += n % 10
    n //= 10
print(s)

#14.Reverse a number
n = int(input("Enter number: "))
rev = 0
while n > 0:
    rev = rev*10 + n%10
    n //= 10
print(rev)

#15.Factorial using while
n = int(input("Enter number: "))
fact = 1
while n > 0:
    fact *= n
    n -= 1
print(fact)

#16.Input until user enters 0
num = int(input("Enter number: "))
while num != 0:
    num = int(input("Enter number: "))

#17.Largest digit
n = int(input("Enter number: "))
largest = 0
while n > 0:
    digit = n % 10
    if digit > largest:
        largest = digit
    n //= 10
print(largest)

#18.Palindrome number
n = int(input("Enter number: "))
temp = n
rev = 0
while n > 0:
    rev = rev*10 + n%10
    n //= 10
print("Palindrome" if rev == temp else "Not Palindrome")

#19.Fibonacci series
n = int(input("Enter terms: "))
a, b = 0, 1
i = 1
while i <= n:
    print(a)
    a, b = b, a+b
    i += 1

#20.Number guessing game
secret = 7
guess = int(input("Guess number: "))
while guess != secret:
    guess = int(input("Try again: "))
print("Correct!")

# ------MIXED (FOR + WHILE)

#21.Number pattern
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

#22.Frequency of characters
s = input("Enter string: ")
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)

#23.Armstrong numbers (1–1000)
for num in range(1, 1001):
    temp = num
    s = 0
    while temp > 0:
        digit = temp % 10
        s += digit ** 3
        temp //= 10
    if s == num:
        print(num)

#24.ATM Menu
balance = 10000
while True:
    print("1.Check Balance 2.Deposit 3.Withdraw 4.Exit")
    ch = int(input("Enter choice: "))
    if ch == 1:
        print(balance)
    elif ch == 2:
        balance += int(input("Enter amount: "))
    elif ch == 3:
        balance -= int(input("Enter amount: "))
    elif ch == 4:
        break

#25.GCD of two numbers
a = int(input("Enter a: "))
b = int(input("Enter b: "))
while b != 0:
    a, b = b, a % b
print("GCD =", a)