# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

num=input("Enter two digit Number: ")
num_str= str(num)
print(int(num_str[0])+int(num_str[1]))