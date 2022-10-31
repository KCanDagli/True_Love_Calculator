
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

case1=name1.lower()
t=case1.count("t")
r=case1.count("r")
u=case1.count("u")
e=case1.count("e")
result1=t+r+u+e

case3=name2.lower()
t=case3.count("t")
r=case3.count("r")
u=case3.count("u")
e=case3.count("e")
result2=t+r+u+e
true_name=result1+result2
print(f"{true_name}")

case2=name1.lower()
l=case2.count("l")
o=case2.count("o")
v=case2.count("v")
e=case2.count("e")
result3=l+o+v+e

case4=name2.lower()
l=case4.count("l")
o=case4.count("o")
v=case4.count("v")
e=case4.count("e")
result4=l+o+v+e
love_name=result3+result4
print(f"{love_name}")

love_score=str(true_name)+str(love_name)
love_scores_integer=int(love_score)

# print(f"{love_scores_integer}")
if love_scores_integer<10 or love_scores_integer>90:
  print(f"Your score is {love_scores_integer}, you go like coke mentos.")
elif love_scores_integer>40 and love_scores_integer<50:
  print(f"your score is {love_scores_integer}, you are alright together.")
else:
  print(f"your score is {love_scores_integer}")








