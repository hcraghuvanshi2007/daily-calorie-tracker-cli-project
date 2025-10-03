"""
Daily Calorie Tracker
Author: [Himanchal Raghuvanshi]
Roll no.: [2501420001]
Program: [B.Tech CSE (Specialization: Data Science), 1st Year, 1st Semester]
Date: 2025 October,04
Title: Mini Project Assignment: Daily Calorie Tracker CLI 
Course: Programming for Problem Solving using Python
Submitted to: [Ms. Jyoti Yadav Ma'am , Python Faculty] 
"""

import datetime

# Part 1: Welcome message
print("=" * 50)
print("DAILY CALORIE TRACKER CLI")
print("=" * 50)
print("This tool helps you log meals, track calories, and compare with your limit.\n")

# Part 2: Input & Data Collection
#-we have let the user input the meal names and calorie amounts

m = []
ca = []
#- meal_names is m and calorie_amounts is ca

nm = int(input("How many meals would you like to enter? "))
for i in range(nm):
    print(f"\nMeal {i+1}:")
    meal = input("Enter meal name (e.g., Breakfast , Lunch , Dinner): ")
    calories = float(input(f"Enter calories for {meal}: "))
    m.append(meal)
    ca.append(calories)

# Part 3: Calorie Calculations


tc = sum(ca)
average_calories = tc / len(ca)  #'''len(ca) will give the number of meals entered'''

#- tc is total calories
#- average_calories is average calories per meal

dl = float(input("\nEnter your daily calorie limit: "))

# Part 4: Exceed Limit Warning and Status Message
if tc > dl:
    status_message = f"You exceeded your daily limit by {tc - dl:.1f} calories!"
elif tc == dl:
    status_message = "Perfect! You hit your daily limit exactly."
else:
    status_message = f"Great! You are within your limit. {dl - tc:.1f} calories remaining."

# Part 5: Output Summary

print("\n" + "=" * 50)
print("DAILY CALORIE SUMMARY")
print("=" * 50)
print(f"{'Meal Name':15} : Calories")
print("-" * 40)

for i in range(len(m)):
    print(f"{m[i]:15} : {ca[i]:.1f}") # indexing for structured output

print("-" * 40)
print(f"{'Total':15} : {tc:.1f}")
print(f"{'Average':15} : {average_calories:.2f}")
print(f"{'Daily Limit':15} : {dl:.1f}")
print("=" * 50)
print(status_message)
print("=" * 50)


# Part 6 : Save Session Log
sc = input("\nWould you like to save this report to a file? (y/n): ")

if sc.lower() == "y":
    now = datetime.datetime.now()
    filename = f"calorie_log_{now.strftime('%Y%m%d_%H%M%S')}.txt"

    with open(filename, "w") as f:
        f.write("DAILY CALORIE TRACKER - SESSION LOG\n")
        f.write("="*40 + "\n")
        f.write(f"Date & Time: {now}\n\n")
        f.write("MEAL DETAILS:\n")
        f.write(f"{'Meal Name':15} : Calories\n")
        f.write("-"*40 + "\n")
        for i in range(len(m)):
            f.write(f"{m[i]:15} : {ca[i]:.1f}\n")
        f.write("-"*40 + "\n")
        f.write(f"{'Total':15} : {tc:.1f}\n")
        f.write(f"{'Average':15} : {average_calories:.2f}\n")
        f.write(f"{'Daily Limit':15} : {dl:.1f}\n\n")
        f.write("Status:\n")
        f.write(status_message + "\n")
# save the file 
    print(f"Report saved as {filename}")
# Thanku message
print("\nThank you for using the Daily Calorie Tracker CLI!")
