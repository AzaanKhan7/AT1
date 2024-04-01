# Data Structure
class User:
    def __init__(self, username, password, categories=None):
        self.username = username
        self.password = password
        self.categories = categories if categories else []

# Subprogram for creating a profile
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
    return user

# Subprogram to group users by category
def group_users_by_category(users):
    grouped_users = {}
    for user in users:
        for category in user.categories:
            if category not in grouped_users:
                grouped_users[category] = []
            grouped_users[category].append(user)
    return grouped_users

# Main program
def main():
    users = []
    users.append(create_profile())
    grouped_users = group_users_by_category(users)
    print("\nUsers Grouped by Category:")
    for category, users_in_category in grouped_users.items():
        print(f"\nCategory: {category}")
        for user in users_in_category:
            print(f"- Username: {user.username}")

if __name__ == "__main__":
    main()