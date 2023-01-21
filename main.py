import random
#This is so that later in this code, we can incorperate the random.randint
wrongpass = 0
# A variable that stores the number of attempts you entered wrong 
password = "1234"
#If you enter this password for accessing the game.
passasker = input("Enter the password for accessing the game:- \n")
#It is a variable that stores your input of the password.
if passasker == "1234":
  print("Password Accepted")
#This is an if statement that tells if the variable(passasker) == to the right password.

  
else:
  wrongpass = wrongpass + 1
  print("Access Denied")
  while wrongpass < 5:
    passasker = input("Try again: ")
    if passasker == "1234":
      print("Password Accepted")
#This else statement will tell if you get the password wrong, you will have the chance to try again for 4 more times.
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
print("\t\t\t\t\tWELCOME-TO-TECHRIDGERS")
print("\n\t\t\t\t\t\t ~SIGN IN~")
playername = input("Choose your username \n")
playerage = input("Enter your age \n")
if int(playerage) > 3:
  print("You are eligible to play this game\n")
else:
  print("You are too young to play :(")
  quit()
playerclass = input("What class you are in? \n")
playeremail = input("Please enter your E-mail \n")


  

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
  print("Your choice is Gers")
  user_choice="Ger"
print("Now for the computers turn\n")
compchoice=random.randint(1,3)
if compchoice == 1:
  print("The computer chose Tech")
  comp_choice="Tech"
elif compchoice == 2:
  print("The computer chose Rid")
  comp_choice="Rid"
elif compchoice == 3:
  print("The computer chose Gers")
  comp_choice="Gers"


