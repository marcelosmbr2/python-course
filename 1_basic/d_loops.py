# While
option = int(input("Enter 1 to continue or 0 to exit: "))

while option == 1:
    print("Continuing...")
    option = int(input("Enter 1 to continue or 0 to exit: "))

# For

for i in range(5):
    print(i)

for num in range(1, 6):
    if num == 3:
        continue  # Skips 3
    if num == 5:
        break     # Ends the loop early
    print(num)
else:
    print("Loop finished completely!")

fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")