login_dict = {'ashwin':'2008@abc','isaa':'2007@abc'}
username = input("enter your username")
if username in login_dict.keys():
    password = input("enter the password")
    if password == login_dict[username]:
        print(f"welcome{username}")
    else:
        print("invalid password")
else:
    print("invalid username")