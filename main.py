import random
wrongpass = 0
# A variable that stores the number of attempts you entered wrong 
password = "Oak-cODEfest_2-3"
#If you enter this password you can access the game.
passasker = input("Enter the password for accessing the game ")
#It is a variable that stores your input of the password.
if passasker == "Oak-cODEfest_2-3":
  print("Password Accepted")
#This is an if statement that tells if the variable(passasker) == to the right password.

  
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

if wrongpass == 5:
  print("Too many failed attempts :(")
  quit()
print("\t\t\t\t\tTECHRIDGERS")
playername = input("What is your name?: ")
playerage = input("How old are you?:" )
playerclass = input("What class you are in ")

print("Hello", playername, "! Let's play a game!")

userwins=""
#userwins is a variable that shows how many wins the user has.
compwins=""
#compwins is a variable that shows how many wins the user has.

print("\n REMEMBER: \n 1. Tech beats Gers \n 2. Gers beats Rid \n 3. Rid beats Tech \n \n Choose wisely and have fun :)")
 
userchoice=input("Type-\n 1 for Tech \n 2 for Rid \n 3 for Gers \n Your answer :- ")
if userchoice=="1":
  print("Your choice is Tech")
  user_choice= "Tech"
elif userchoice=="2":
  print("Your choice is Rid")
  user_choice= "Rid"
elif userchoice=="3":
  print("Your choice is Ger")
  user_choice="Ger"
print("Now for the computers turn\n")
compchoice=random.randint(1,3)
if compchoice



