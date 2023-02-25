import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator")
nLetters= int(input("How many letters would you like in your password?\n"))
nNumbers= int(input("How many numbers would you like?\n"))
nSymbols= int(input("How many symbols would you like?\n"))

#Easy Level
password=""
for char in range(1,nLetters+1):
    password+=random.choice(letters)
for num in range(1,nNumbers+1):
    password+=random.choice(numbers)
for sys in range(1,nSymbols+1):
    password+=random.choice(symbols)
print(password)

#Hard Level
passwordList=[]
for char in range(1,len(password)+1):
    passwordList.append(random.choice(password))
# print(passwordList)

randomized=""
for char in passwordList:
    randomized+=char
print(randomized)
