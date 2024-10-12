'''
Author : Lalitha Sri Chennapragada
Date : 11/10/2024
Description : The following program runs a cloud storage tracking system, It has a variety of functions, to create a user account, 
delete it, upload files and display the accounts and exits depending on the choices selected .
'''

#Lists
available_storage = []
storage_list = []
username = []
usernames = []
#option 1:To user a user account
def create_user_account():
    print("create user account>>")
    
    user = input("Enter a user name>>")
    if user == "":
        print("username field cannot be left empty>>")
        return user, 0
    
storage = input("Enter available storage (MB): ")
    
if storage.isdigit() and int(storage) > 0:  # Check if storage is a valid positive number which is the criteria
        storage_value = int(storage)
        usernames.append(username)  # Add the username to the list of users
        storage_list.append(storage_value)  # Add storage to the list of user's storage
        print(f"User '{username}' created with {storage_value}MB storage.")
else:
        print("Storage must be a positive number.")

# Option 2 : To delete the created user account
def delete_user_account():
    username = input("Enter the username to delete: ")
    
    if username in usernames:  # to verify if the username exists
        index = usernames.index(username)
        usernames.pop(index)  # To remove the username
        storage_list.pop(index)  # To removethe relevant attached storage 
        print(f"User '{username}' deleted.")
    else:
        print("Username not found.")

#Option 3 To upload a File, and check if the storage is available from the allocated amount of storage
def upload_file():
    username = input("Enter the username: ")
    
    if username in usernames:  # Check if the user exists
        index = usernames.index(username)
        filesize = input("Enter the file size (MB): ")
        
        if filesize.isdigit() and int(filesize) > 0:  # Check if the file size is a valid positive number
            filesize_value = int(filesize)
            if storage_list[index] >= filesize_value:  # Check if there's enough storage
                storage_list[index] -= filesize_value  # Minus the file size amount from the allocated storage amount
                print(f"File uploaded. {filesize_value}MB used. {storage_list[index]}MB remaining.")
            else:
                print("Not enough storage space.")
        else:
            print("Please enter a valid file size.")
    else:
        print("Username not found.")
#Option 4: To display the present user information, checks if the user exists or not
def display_users():
    if not usernames:  # Check if the list of usernames is empty
        print("No users found.")
    else:
        print("Current users and available storage:")
        for i in range(len(usernames)):
            print(f"User: {usernames[i]}, Available Storage: {storage_list[i]}MB")
# To Display the options in a Menu
def menu():
    while True:
        print("\n1. Create User")
        print("2. Delete User")
        print("3. Upload File")
        print("4. Display Users")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            create_user_account()
        elif choice == "2":
            delete_user_account()
        elif choice == "3":
            upload_file()
        elif choice == "4":
            display_users()
        elif choice == "5":
            print("Exiting...")
            break
    
        else:
            print("Invalid Choice, please select from the available options")

#To initiate the program displaying the menu first
menu()
