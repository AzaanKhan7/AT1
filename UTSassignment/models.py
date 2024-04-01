import random

# Data Structure
class User:
    def __init__(self, username, password, categories=None):
        self.username = username
        self.password = password
        self.categories = categories if categories else []

# Subprogram
def create_profile():
    print("Create a Profile:")
    username = input("Enter username: ")
    while True:
        password = input("Enter password (4 digits only): ")
        if password.isdigit() and len(password) == 4:
            break
        else:
            print("Invalid password. Please enter a 4-digit number.")
    categories = ["Sports", "Gaming", "Art", "Music"]  # Define categories here
    print("Choose categories (Enter numbers from 1 to 4, separate with commas):")
    print("1. Sports\n2. Gaming\n3. Art\n4. Music")
    print("Hint: You can choose multiple categories by entering their numbers separated by commas.")
    selected_categories = []
    while True:
        choice = input("Enter the number of the category you want to select: ")
        try:
            category_index = int(choice)
            if 1 <= category_index <= 4:
                category = categories[category_index - 1]
                selected_categories.append(category)
                print(f"Category '{category}' added.")
                break
            else:
                print("Invalid category number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    user = User(username, password, selected_categories)
    print("Profile created successfully.")
    print(f"Username: {user.username}")
    print(f"Password: {user.password}")
    print("Selected Categories:")
    for category in user.categories:
        print(f"- {category}")
    print("Thank you! Your profile has been created.")

# Main program
def main():
    create_profile()

if __name__ == "__main__":
    main() 