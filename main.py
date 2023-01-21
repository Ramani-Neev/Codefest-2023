import random
#This is so that later in this code, we can incorperate the random.randint function
wrongpass = 0
# A variable that stores the number of attempts you entered wrong 
password = "1234"
#If you enter this password for accessing the game.
varhelp = 4
comp_choice = ""
user_choice = ""
compchoice = ()
userchoice = ()
wrongpass = ()
playerage = ()
variable = ()
compwins = 0
userwins = 0
playerclass = ""
passasker = input("Enter the security key to unlock the game:- \n")
#It is a variable that stores your input of the password.
if passasker == "1234":
  print("Password Accepted")
#This is an if statement that tells if the variable(passasker) == to the right password.

  
else:
  wrongpass = wrongpass + 1
  print("Access Denied")
  quit()



   
print("\t\t\t\t\tWELCOME-TO-TECHRIDGERS")
#This is the heading tag and \t means tab.
print("\n\t\t\t\t\t\t ~SIGN IN~\n")
playername = input("Create your username:-  \n")
playerage = input("Specify your age:-  ")
if int(playerage) > 5:
    print(input("You are eligible. Press enter to continue..."))
else:
    print("You are not eligible :(")
    quit()

playerclass = input("Your class and section:-  ")

print("\nHey", playername, "! Let's play a game!")  

userwins = 0
  # userwins is a variable that shows how many wins the user has.
compwins = 0
  # compwins is a variable that shows how many wins the user has.
  
print("\n Note: \n 1. Tech beats Gers \n 2. Gers beats Rid \n 3. Rid beats Tech \n \n Have fun! :)")
  
userchoice = int(input("Choose your move-\n 1 for Tech \n 2 for Rid \n 3 for Gers \n Your answer :- "))
if userchoice == 1:
  print("Your choice is Tech")
  user_choice = "Tech"
elif userchoice == 2:
  print("Your choice is Rid")
  user_choice = "Rid"
elif userchoice==3:
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


if comp_choice == "Tech" and user_choice == "Tech":
  print("It's a Draw!\n")
  userwins=userwins + 1
  compwins=compwins + 1
    
elif   comp_choice == "Tech" and user_choice == "Rid":
  print("You get a point!\n")
  userwins=userwins + 1
    
elif   comp_choice == "Tech" and user_choice == "Gers":
  print("The Bot gets a point!\n")
  compwins=compwins + 1
  
elif   comp_choice == "Rid" and user_choice == "Rid":
  print("It's a Draw!\n")
  userwins=userwins + 1
  compwins=compwins + 1
    
elif   comp_choice == "Rid" and user_choice == "Tech":
  print("The Bot gets a point!\n")
  compwins=compwins + 1
    
elif   comp_choice == "Rid" and user_choice == "Gers":
  print("The bot gets a point!\n")
  compwins=compwins + 1
    
elif   comp_choice == "Gers" and user_choice == "Tech":
  print("You get a point!\n")
  userwins=userwins + 1
    
elif   comp_choice == "Gers" and user_choice == "Rid":
  print("The bot gets a point!\n")
  compwins=compwins + 1
    
elif   comp_choice == "Gers" and user_choice == "Gers":
  print("It's a Draw!\n")
  userwins=userwins + 1
  compwins=compwins + 1

  


while userwins < 5 and compwins < 5:
  userchoice = input("Enter the next one you will choose...\n")
 if 
  print("waiting....")
  if userchoice == 1:
    print("Your choice is Tech")
    user_choice = "Tech"
  elif userchoice == 2:
    print("Your choice is Rid")
    user_choice = "Rid"
  elif userchoice==3:
    print("Your choice is Gers")
    user_choice = "Gers"
  
  compchoice = random.randint(1, 3)
  if compchoice == 1:
    print("The Bot chose Rid")
    comp_choice = "Rid"
  elif compchoice == 2:
    print("The Bot chose Tech")
    comp_choice = "Tech"
  else:
    print("The Bot chose Gers")
    comp_choice = "Gers"
    
    
  if comp_choice == "Tech" and user_choice == "Tech":
    print("It's a Draw!\n")
    userwins=userwins + 1
    compwins=compwins + 1
        
  elif comp_choice == "Tech" and user_choice == "Rid":
    print("You get a point!\n")
    userwins=userwins + 1
        
  elif comp_choice == "Tech" and user_choice == "Gers":
    print("The Bot gets a point!\n")
    compwins=compwins + 1
      
  elif comp_choice == "Rid" and user_choice == "Rid":
    print("It's a Draw!\n")
    userwins=userwins + 1
    compwins=compwins + 1
        
  elif comp_choice == "Rid" and user_choice == "Tech":
    print("The Bot gets a point!\n")
    compwins=compwins + 1
        
  elif comp_choice == "Rid" and user_choice == "Gers":
    print("The bot gets a point!\n")
    compwins=compwins + 1
        
  elif   comp_choice == "Gers" and user_choice == "Tech":
    print("You get a point!\n")
    userwins=userwins + 1
        
  elif comp_choice == "Gers" and user_choice == "Rid":
    print("The bot gets a point!\n")
    compwins=compwins + 1
        
  elif comp_choice == "Gers" and user_choice == "Gers":
    print("It's a Draw!\n")
    userwins=userwins + 1
    compwins=compwins + 1

print("_"*90)
sb=("\t\tYou\t\t\t\t\t\t\tComputer\nRound 1-\t\t", userwins,"\t\t\t\t\t\t\t",compwins)
print(sb)
print("_"*90)
  


  
  