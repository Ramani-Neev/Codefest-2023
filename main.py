wrrrongpass = 0
password = "Oak-cODEfest_2-3"
passasker = input("Enter the password")
if passasker == "Oak-cODEfest_2-3":
  print("Password Accepted")
else:
  wrongpass = wrongpass + 1
  while wrongpass < 5:
    print("Access Denied")
    passasker = input("Enter the password: ")
    if passasker == "Oak-cODEfest_2-3":
      print("Password Accepted")
    else:
      wrongpass = wrongpass + 1
      print("Access Denied")
      
      passasker = input("Enter the password")
      if passasker == "Oak-cODEfest_2-3":
      print("Password Accepted")
      else:
      wrongpass = wrongpass + 1
      print("Access Denied")




print("\t\t\t\t\tTECHRIDGERS")
playername = input("What should we call you?: ")
print("Hello", playername)
userwins=""
#userwins is a variable that shows how many wins the user has.
compwins=""
#compwins is a variable that shows how many wins the user has.

print("\n REMEMBER: \n 1. Tech beats Gers \n 2. Gers beats Rid \n 3. Rid beats Tech \n \n Choose wisely and have fun :)")
