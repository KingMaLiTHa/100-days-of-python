# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
lname1=name1.lower()
lname2=name2.lower()

noT= lname1.count("t") + lname2.count("t")

noR= lname1.count("r") + lname2.count("r")
noU= lname1.count("u") + lname2.count("u")
noE= lname1.count("e") + lname2.count("e")

noL= lname1.count("l") + lname2.count("l")
noO= lname1.count("o") + lname2.count("o")
noV= lname1.count("v") + lname2.count("v")
noE= lname1.count("e") + lname2.count("e")

noTRUE=noT+noR+noU+noE
noLOVE=noL+noO+noV+noE
Score= noTRUE*10 + noLOVE

if Score<10 or Score>90:
    print(f"Your Score is {Score}, you go together like coke and mentos.")
elif Score>=40 and Score<=50:
    print(f"Your Score is {Score}, you are alright together.")
else:
    print(f"Your Score is {Score}")