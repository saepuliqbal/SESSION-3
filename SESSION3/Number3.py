def is_eligible_to_vote(age):
 
  return 18 <= age <= 65

age = int(input("Enter your age: "))

if is_eligible_to_vote(age):
  print("You are eligible to vote.")
else:
  print("You are not eligible to vote.")
