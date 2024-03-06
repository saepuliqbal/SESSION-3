def extract_domain(email):

  at_index = email.find('@')

  if at_index == -1:
    return None

  domain = email[at_index + 1:]

  return domain

email = input("Enter your email address: ")

domain_name = extract_domain(email)

if domain_name:
  print(f"The domain name is: {domain_name}")
else:
  print("Invalid email address (no '@' symbol found).")
