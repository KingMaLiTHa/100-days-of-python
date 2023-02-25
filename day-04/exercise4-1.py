#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲
import random

seed_input= int(input("Enter the seed? "))
random.seed(seed_input)
# For same seed number, the random output is same for every try

random_value= random.randint(0,1)
if random_value==1:
    print("Heads")
else:
    print("Tails") 