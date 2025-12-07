start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

squares = [i*i for i in range(start, end+1)]
even_values = [x for x in squares if x % 2 == 0]
odd_values = [x for x in squares if x % 2 != 0]

print("Squares:", squares)
print("Even squares:", even_values)
print("Odd squares:", odd_values)
