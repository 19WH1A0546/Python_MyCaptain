n = int(input("Enter no of elements: "))
numbers = []
for i in range(n):
    x = int(input())
    numbers.append(x)

positive_numbers = []
for i in numbers:
    if (i >=0):
        positive_numbers.append(i)
print(positive_numbers)
