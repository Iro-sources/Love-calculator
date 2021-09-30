# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combined_string = name1 + name2

t = combined_string.count("t")

r = combined_string.count("r")

u = combined_string.count("u")

e = combined_string.count("e")

total_true = t + r + u + e 
print(total_true)

l = combined_string.count("l")


o = combined_string.count("o")


v = combined_string.count("v")


e = combined_string.count("e")
total_love =  l + o + v + e
print(total_love)

love_score = int(str(total_true) + str(total_love))
print(love_score)

if love_score < 10 or love_score > 90:
  print(f"Your love score is: {love_score}, go together like coke and mentos")
elif love_score >= 40 and love_score <= 50:
  print(f"Your love score is: {love_score}, you are alright together")
else:
  print(f"Your love score is: {love_score}")


