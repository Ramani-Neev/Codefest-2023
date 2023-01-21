import random
wropass = "False"
vartrue = "None"
wrongpass = 0
comp_choice = ""
user_choice = ""
user_score = 0
comp_score = 0
# A variable that stores the number of attempts you entered wrong
password = "1234"
# If you enter this password you can access the game.
passasker = input("Password:- ")
# It is a variable that stores your input of the password.
if passasker == password:
    print("\nPassword Accepted")
    vartrue = "True"
# This is an if statement that tells if the variable(passasker) == to the right password.

else:
    print("Access Denied")
    wropass = "True"
    quit()


  

if wropass == "False":
  print("\t\t\t\t\t\tWELCOME-TO-TECHRIDGERS")

  print("\n\t\t\t\t\t\t\t  -SIGN IN-\n")
  playername = input("Choose your username:\n ")
  
  playeremail = input("Type in your E-mail: ")
  
  
  print("Hello", playername, "! Let's play a game!")
  
  userwins = ""
  # userwins is a variable that shows how many wins the user has.
  compwins = ""
  # compwins is a variable that shows how many wins the user has.
  
  print(
      "\n Note: \n 1. Tech beats Gers \n 2. Gers beats Rid \n 3. Rid beats Tech \n \n Have fun! :)")
  
  userchoice = input("Choose your move-\n 1 for Tech \n 2 for Rid \n 3 for Gers \n Your answer :- ")
  if userchoice == "Tech":
      print("Your choice is Tech")
      user_choice = "Tech"
  elif userchoice == "Rid":
      print("Your choice is Rid")
      user_choice = "Rid"
  else:
      print("Your choice is Gers")
      user_choice = "Gers"
  print("The Bot is choosing...\n")
  compchoice = random.randint(1, 3)
  if compchoice == 1:
      print("The Bot chose Tech")
      comp_choice = "Tech"
  elif compchoice == 2:
      print("The Bot chose Rid")
      comp_choice = "Rid"
  else:
      print("The Bot chose Gers")
      comp_choice = "Gers"

  
if   comp_choice == "Tech" and user_choice == "Tech":
  print("It's a Draw!")
elif   comp_choice == "Tech" and user_choice == "Rid":
  print("You get a point!")
  user_score = user_score + 1
elif   comp_choice == "Tech" and user_choice == "Gers":
  print("The Bot gets a point!")
elif   comp_choice == "Rid" and user_choice == "Rid":
  print("It's a Draw!")
elif   comp_choice == "Rid" and user_choice == "Tech":
  print("The Bot gets a point!")
elif   comp_choice == "Rid" and user_choice == "Gers":
  print("You get a point!")
elif   comp_choice == "Gers" and user_choice == "Tech":
  print("You get a point!")
  user_score = user_score + 1
elif   comp_choice == "Gers" and user_choice == "Rid":
  print("The bot gets a point!")
elif   comp_choice == "Gers" and user_choice == "Gers":
  print("It's a Draw!")