import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
seed_input=int(input("Enter the seed? "))
random.seed(seed_input)

random_index=random.randint(0,len(names)-1)
print(f"{names[random_index]} is going to buy the meal today!")

