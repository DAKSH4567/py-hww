n = int(input("Enter a number: "))

odd_below = [i for i in range(n) if i % 2 != 0]
odd_above = [i for i in range(n, n+20) if i % 2 != 0]

print("Odd numbers below:", odd_below)
print("Odd numbers above:", odd_above)

fruits = ["apple", "mango", "banana", "orange", "grapes"]

updated = [f[0].upper() + f[1:] for f in fruits]

print("Updated fruits:", updated)
