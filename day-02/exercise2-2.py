# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

weight=input("Enter your weight?\n")
height=input("Enter your height?\n")
# ! input function returns str


bmi= float(weight)/float(height)**2
# ** is power, in this case heightxheight 
print(int(bmi))