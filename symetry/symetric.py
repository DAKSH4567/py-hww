set1 = set(map(int, input("Enter elements of first set: ").split()))
set2 = set(map(int, input("Enter elements of second set: ").split()))

result = set1.symmetric_difference(set2)

print("Symmetric Difference:", result)
