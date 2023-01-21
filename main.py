import random
#This is so that later in this code, we can incorperate the random.randint function
wrongpass = 0
# A variable that stores the number of attempts you entered wrong 
password = "1234"
#If you enter this password for accessing the game.
varhelp = 4
passasker = input("Enter the security key to unlock the game:- \n")
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
#If the password is wrong it will add +1 to your attempts.
      
      passasker = input("Try Again: ")
      if passasker == "1234":
        print("Password Accepted")
#If you get the password wrong it will show the message 'Try Again' and if you get the answer right it will print 'Password accepted'.
      else :
        wrongpass = wrongpass + 1
        print("Access Denied")

if wrongpass == 5:
  print("Too many failed attempts :(")
  quit()
  #If you fail to type the correct password more than 5 times, the program automatically breaks
print("\t\t\t\t\tWELCOME-TO-TECHRIDGERS")
#This is the heading tag and \t means tab.
print("\n\t\t\t\t\t\t ~SIGN IN~\n")
playername = input("Create your unique username:-  \n")
playerage = input("Specify your age:-  ")
if int(playerage) > 4:
    print(input("You are eligible. Press enter to continue..."))
else:
    print("You are not eligible :(")
    quit()

playerclass = input("Your class:-  ")

print("\nHello", playername, " Let's play a game!")  

userwins = ""
  # userwins is a variable that shows how many wins the user has.
compwins = ""
  # compwins is a variable that shows how many wins the user has.
  
print("\n Note: \n 1. Tech beats Gers \n 2. Gers beats Rid \n 3. Rid beats Tech \n \n Have fun! :)")
  
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


if comp_choice == "Tech" and user_choice == "Tech":
    print("It's a Draw!")
    userwins=userwins+str(1)
    compwins=compwins+str(1)
    
elif   comp_choice == "Tech" and user_choice == "Rid":
    print("You get a point!")
    userwins=userwins+str(1)
    
elif   comp_choice == "Tech" and user_choice == "Gers":
    print("The Bot gets a point!")
    compwins=compwins+str(1)
  
elif   comp_choice == "Rid" and user_choice == "Rid":
    print("It's a Draw!")
    userwins=userwins+str(1)
    compwins=compwins+str(1)
    
elif   comp_choice == "Rid" and user_choice == "Tech":
    print("The Bot gets a point!")
    compwins=compwins+str(1)
    
elif   comp_choice == "Rid" and user_choice == "Gers":
    print("The bot gets a point!")
    compwins=compwins+str(1)
    
elif   comp_choice == "Gers" and user_choice == "Tech":
    print("You get a point!")
    userwins=userwins+str(1)
    
elif   comp_choice == "Gers" and user_choice == "Rid":
    print("The bot gets a point!")
    compwins=compwins+str(1)
    
elif   comp_choice == "Gers" and user_choice == "Gers":
    print("It's a Draw!")
    userwins=userwins+str(1)
    compwins=compwins+str(1)

  

while int(comp_choice) < int(varhelp) and int(user_choice) < int(varhelp):
  userchoice = input("Enter the next one you will choose...")
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
      print("It's a Draw!")
      userwins=userwins+str(1)
      compwins=compwins+str(1)
      
  elif   comp_choice == "Tech" and user_choice == "Rid":
      print("You get a point!")
      userwins=userwins+str(1)
      
  elif   comp_choice == "Tech" and user_choice == "Gers":
      print("The Bot gets a point!")
      compwins=compwins+str(1)
    
  elif   comp_choice == "Rid" and user_choice == "Rid":
      print("It's a Draw!")
      userwins=userwins+str(1)
      compwins=compwins+str(1)
      
  elif   comp_choice == "Rid" and user_choice == "Tech":
      print("The Bot gets a point!")
      compwins=compwins+str(1)
      
  elif   comp_choice == "Rid" and user_choice == "Gers":
      print("The bot gets a point!")
      compwins=compwins+str(1)
      
  elif   comp_choice == "Gers" and user_choice == "Tech":
      print("You get a point!")
      userwins=userwins+str(1)
      
  elif   comp_choice == "Gers" and user_choice == "Rid":
      print("The bot gets a point!")
      compwins=compwins+str(1)
      
  elif   comp_choice == "Gers" and user_choice == "Gers":
      print("It's a Draw!")
      userwins=userwins+str(1)
      compwins=compwins+str(1)
  