# List + input + control structure

marks = [
    int(input("Enter Python marks: ")),
    int(input("Enter English marks: ")),
    int(input("Enter Computer marks: "))
]

total = sum(marks)
average = total / 3

if average >= 50:
    print("Pass")
else:
    print("Fail")

print("Marks List:", marks)
print("Average:", average)