import random
#It is a ramdom library of functions we are calling.
# This is so that later in this code, we can incorperate the random.randint function
wrongpass = 0
# A variable that stores the number of attempts you entered wrong
password = "1234"
# If you enter this password for accessing the game.
varhelp = 4
comp_choice = ""
user_choice = ""
compchoice = ()               
userchoice = ()
wrongpass = ()
playerage = ()
variable = 2
compwins = 0
userwins = 0
playerclass = ""
#Line 9 to 19 is all the variables we are going to use.
passasker = input("Enter the security key to unlock the game:- \n")
# It is a variable that stores your input of the password.
if passasker == "1234":
    print("Password Accepted")
# This is an if statement that tells if the variable(passasker) == to the right password.

else:
    wrongpass = wrongpass + 1
    print("Access Denied")
    quit()

print("\t\t\t\t\tWELCOME-TO-TECHRIDGERS")
# This is the heading tag and \t means tab.
print("\n\t\t\t\t\t\t ~SIGN IN~\n")
playeremail=input("Enter your oakridge email:-\n")
playeremail1=playeremail[::-1]
playeremail2=playeremail1[:11]
if playeremail2=="ni.egdirkao":
    print("Email Accepted")
else:
    print("Access Denied")
    quit()

playername = input("Create your username:-  \n")
playerage = int(input("Specify your age:-  "))
if int(playerage) > 5:
    print(input("You are eligible. Press enter to continue..."))
  #Line 35 to 38 is made for security and to acces the game you have to be above 5 years.
else:
    print("You are not eligible :(")
    quit()
  #Orelese it wil quit the game for you.

playerclass = input("Your class and section:-  ")

print("\nHey", playername, "! Let's play a game!")

userwins = 0
# userwins is a variable that shows how many wins the user has.
compwins = 0
# compwins is a variable that shows how many wins the user has.

print("\n Note: \n 1. Tech beats Gers \n 2. Gers beats Rid \n 3. Rid beats Tech \n \n Have fun! :)")
#An important note to guide the user.
userchoice = int(input("Choose your move-\n 1 for Tech \n 2 for Rid \n 3 for Gers \n Your answer :- "))
if userchoice == 1:
    print("Player chose Tech")
    user_choice = "Tech"
#Since we want to make this creative we are using numbers instead of the actual letters.
elif userchoice == 2:
    print("Player chose Rid")
    user_choice = "Rid"
elif userchoice == 3:
    print("Player chose Gers")
    user_choice = "Gers"
print("Bot is choosing...\n")
compchoice = random.randint(1, 3)
#Random.randit is a function which will randomly pick a number from your starting number to ender number.
if compchoice == 1:
    print("Bot chose Tech")
    comp_choice = "Tech"
#We are creating the if and elif functions to tell if the integer equals to the values.
elif compchoice == 2:
    print("Bot chose Rid")
    comp_choice = "Rid"
else:
    print("Bot chose Gers")
    comp_choice = "Gers"



if comp_choice == "Tech" and user_choice == "Tech":
    print("It's a Draw!\n")
    userwins = userwins + 1
    compwins = compwins + 1

  #And if the userinput is greater than the computerinput it will add 1 Point and vice versa for the same.

elif comp_choice == "Tech" and user_choice == "Rid":
  print(playername, " gained +1 Point\n")
  userwins = userwins + 1

elif comp_choice == "Tech" and user_choice == "Gers":
  print("Bot gained +1 Point\n")
  compwins = compwins + 1

elif comp_choice == "Rid" and user_choice == "Rid":
  print("It's a Draw!\n")
  userwins = userwins + 1
  compwins = compwins + 1

elif comp_choice == "Rid" and user_choice == "Tech":
  print("Bot gained +1 Point\n")
  compwins = compwins + 1

elif comp_choice == "Rid" and user_choice == "Gers":
  print(playername, " gained +1 Point\n")
  userwins = userwins + 1

elif comp_choice == "Gers" and user_choice == "Tech":
  print(playername, " gained +1 Point\n")
  userwins = userwins + 1

elif comp_choice == "Gers" and user_choice == "Rid":
  print("Bot gained +1 Point\n")
  compwins = compwins + 1

elif comp_choice == "Gers" and user_choice == "Gers":
  print("-Tie-\n")
  userwins = userwins + 1
  compwins = compwins + 1


while userwins < 5 and compwins < 5:
  userchoice = int(input("Enter the next one you will choose...\n")) 
  if userchoice == 1:
    print(playername, " chose Tech")
    user_choice = "Tech"
  elif userchoice == 2:
    print(playername, " chose Rid")
    user_choice = "Rid"
  elif userchoice == 3:
    print(playername, " chose Gers")
    user_choice = "Gers"
      
  print("waiting....")

  compchoice = random.randint(1, 3)
  if compchoice == 1:
    print("Bot chose Rid")
    comp_choice = "Rid"
  elif compchoice == 2:
    print("Bot chose Tech")
    comp_choice = "Tech"
  else:
    print("Bot chose Gers")
    comp_choice = "Gers"

  if comp_choice == "Tech" and user_choice == "Tech":
    print("-Tie-\n")
    userwins = userwins + 1
    compwins = compwins + 1

  elif comp_choice == "Tech" and user_choice == "Rid":
    print(playername, "gained +1Point")
    userwins = userwins + 1

  elif comp_choice == "Tech" and user_choice == "Gers":
    print("Bot gained +1Point\n")
    compwins = compwins + 1

  elif comp_choice == "Rid" and user_choice == "Rid":
    print("-Tie-\n")
    userwins = userwins + 1
    compwins = compwins + 1

  elif comp_choice == "Rid" and user_choice == "Tech":
    print("Bot gained +1Point\n")
    ompwins = compwins + 1

  elif comp_choice == "Rid" and user_choice == "Gers":
    print("Bot gained +1Point\n")
    compwins = compwins + 1

  elif comp_choice == "Gers" and user_choice == "Tech":
    print(playername, " gained +1Point\n")
    userwins = userwins + 1

  elif comp_choice == "Gers" and user_choice == "Rid":
    print("Bot gained +1Point\n")
    compwins = compwins + 1

  elif comp_choice == "Gers" and user_choice == "Gers":
    print("-Tie-\n")
    userwins = userwins + 1
    compwins = compwins + 1

  #We are using a wild loop for indicating that there will be 5 rounds and the while loop will repeat not more than 5 times.

print("_"*70)
print("\t\t\t\t\tComputer\t\t\t\tPlayer\n")
print("Overall Score:- \t   ", compwins, "\t\t\t\t\t  ", userwins, "\n")
print("_"*70)

if userwins == compwins:
  print("TIE!!")
elif userwins > compwins:
  print(playername, " WINS!!!")
else:
  print("--GAME OVER--")
  print("Sorry, ", playername, "please try again.")

#This is to make the scorecard of the player and computer after 5 rounds.