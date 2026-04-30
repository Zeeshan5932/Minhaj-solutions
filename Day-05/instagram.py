# Instagram Style Mini System Using Functions

# User profile data
username = "ali_python"
password = "1234"
followers = 120
following = 80
likes = 45
bio = "Learning Python and building cool projects"


# Function 1: Login system
def login(input_username, input_password):
    if input_username == username and input_password == password:
        print("Login Successful")
        return True
    else:
        print("Wrong username or password")
        return False


# Function 2: Show profile
def show_profile():
    print("\n--- Instagram Profile ---")
    print("Username:", username)
    print("Bio:", bio)
    print("Followers:", followers)
    print("Following:", following)


# Function 3: Like post
def like_post(current_likes):
    current_likes = current_likes + 1
    print("Post liked")
    print("Total Likes:", current_likes)
    return current_likes


# Function 4: Follow user
def follow_user(current_followers):
    current_followers = current_followers + 1
    print("You followed this user")
    print("Total Followers:", current_followers)
    return current_followers


# Main program
print("--- Welcome to Mini Instagram ---")

user_name = input("Enter username: ")
user_pass = input("Enter password: ")

is_login = login(user_name, user_pass)

if is_login:
    show_profile()

    print("\nWhat do you want to do?")
    print("1. Like Post")
    print("2. Follow User")

    choice = input("Enter your choice: ")

    if choice == "1":
        likes = like_post(likes)
    elif choice == "2":
        followers = follow_user(followers)
    else:
        print("Invalid Choice")
else:
    print("Please try again")