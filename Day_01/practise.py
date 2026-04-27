name = input("Enter your name:")
age = int(input("Enter your age:"))
city = input("Enter your city:")
fav_food = input("Enter your favourite food:")


print("\n student Profile:")
print("Name:", name)
print("age after 5 years:", age + 5)
print("city" , city )
print("favourite food:", fav_food)


if age >=18:
    print("You are an adult.")

else: 
    print("your are younger learner.")