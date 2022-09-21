#Oturum açmak için kullanıcı adı ve şifre kontrolü 

usersinformations = {
    "ricardo":"1234",
    "pele":"lp12",
    "benzema":"cr7",
    "souza":"sza45"

}

username = input("Username: ")
password = input("Password: ")

if username in usersinformations.keys():
    if  usersinformations[username] == password:
        print("Login Successful..")
    else:
        print("Login not Successful..Please Check Your Password..")

else:
    print("Username doesn't Exist..Try again..")

