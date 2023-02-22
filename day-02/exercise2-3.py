# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
final= 60
r_years= final-int(age)
r_months=r_years*12
r_weeks=r_years*52
r_days=r_years*365

print(f"You have {r_days} days, {r_weeks} weeks, and {r_months} months left.")
