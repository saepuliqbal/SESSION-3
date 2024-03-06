def sum_of_digits(num):

  if num < 0:
    num = abs(num)
    is_negative = True
  else:
    is_negative = False

  sum = 0

  while num > 0:
    digit = num % 10

    sum += digit

    num //= 10

  if is_negative:
    sum *= -1

  return sum

number = 12345
result = sum_of_digits(number)
print(f"The sum of digits in {number} is: {result}")
