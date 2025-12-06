d = {"a": 3, "b": 5, "c": 3, "d": 2, "e": 3}

value = int(input("Enter value to check frequency: "))

freq = list(d.values()).count(value)

print("Frequency:", freq)

