wrongpass = 0
password = "Oak-cODEfest_2-3"
passasker = input("Enter the password: ")
if passasker == "Oak-cODEfest_2-3":
  print("Password Accepted")
else:
  wrongpass = wrongpass + 1
  print("Access Denied")
  while wrongpass < 5:
    passasker = input("Try again: ")
    if passasker == "Oak-cODEfest_2-3":
      print("Password Accepted")
    else:
      wrongpass = wrongpass + 1
      print("Access Denied")
      
      passasker = input("Try Again: ")
      if passasker == "Oak-cODEfest_2-3":
        print("Password Accepted")
      else:
        wrongpass = wrongpass + 1
        print("Access Denied")

