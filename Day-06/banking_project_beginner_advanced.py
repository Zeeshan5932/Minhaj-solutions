"""
Loop Practice Projects
Topics Covered:
- for loop
- while loop
- nested loops
- pattern printing
- input
- control structures
"""

# -------------------------------
# Project 1: Star Pattern using For Loop
# -------------------------------

# print("\n--- Star Pattern using For Loop ---")

# rows = int(input("Enter number of rows: "))

# for i in range(1, rows + 1):
#     print("*" * i)


# -------------------------------
# Project 2: Countdown using While Loop
# -------------------------------

# print("\n--- Countdown using While Loop ---")

# number = int(input("Enter starting number: "))

# while number >= 1:
#     print(number)
#     number = number - 1

# print("Countdown Finished!")


# # -------------------------------
# # Project 3: Square Pattern using Nested Loop
# # -------------------------------

# print("\n--- Square Star Pattern using Nested Loop ---")

# size = 6

# for i in range(size):
#     for j in range(size):
#         print("*", end="\t \t")
#     print()


# # -------------------------------
# # Extra Pattern 1: Reverse Star Pattern
# # -------------------------------

# print("\n--- Reverse Star Pattern ---")

# rows = int(input("Enter number of rows: "))

# for i in range(rows, 0, -1):
#     print("*" * i)


# # -------------------------------
# # Extra Pattern 2: Number Pattern
# # -------------------------------

# print("\n--- Number Pattern ---")

# rows = int(input("Enter number of rows: "))

# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()


numbers = [10, 15, 23, 42, 55, 60, 77]

even = 0
odd = 0

for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even:", even)
print("Odd:", odd)


