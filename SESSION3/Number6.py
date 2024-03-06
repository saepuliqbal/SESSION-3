def is_even_and_greater_than_ten(number):

  return number % 2 == 0 and number > 10

number = int(input("Enter a number: "))

if is_even_and_greater_than_ten(number):
  print(f"The number {number} is even and greater than 10.")
else:
  print(f"The number {number} is not even and/or not greater than 10.")
