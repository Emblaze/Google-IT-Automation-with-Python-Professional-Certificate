import re

def repeating_letter_a(text):
  """The repeating_letter_a function checks if the text passed includes\
  the letter "a" (lowercase or uppercase) at least twice"""
  result = re.search(r"___", text)
  return result != None

print(repeating_letter_a("banana")) # True
print(repeating_letter_a("pineapple")) # False
print(repeating_letter_a("Animal Kingdom")) # True
print(repeating_letter_a("A is for apple")) # True