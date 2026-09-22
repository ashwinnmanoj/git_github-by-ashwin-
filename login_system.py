#concept:string,variable,==,and,ifelse
#login credientials
correct_username = "Ashwin"
correct_password = "12345678" 
username = input("enter the username")
password = input("enter the password")
if username == correct_username and password == correct_password:
    print("login succesfull")
else:
    print("invalid usename and password")

