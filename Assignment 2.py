#Imported 'math' package to use math.sqrt() (square root) function
import math
print("Welcome to the prime number checker")


awaiting_integer = True
while awaiting_integer: #while true do the following
  user_number=(input("Please enter a whole number:"))
  try:
    user_number_as_int=int(user_number) #try to convert the user input to an integer
  except:
    print("That is not a whole number.") #if you can't convert to integer, print
  else:
    awaiting_integer = False #else, if we could convert user input to integer, awaiting_integer is then false so loop is then broken

if user_number_as_int <2: #if the user input (now integer) is less than 2, print
  print(f"{user_number_as_int} is not a prime number.")
else:
  square_root=math.sqrt(user_number_as_int)
  number_to_check=2 #checking numbers against the square root of the user input (starting with 2)
  while number_to_check <= square_root: #while the number we are checking is less than or equal to the square root of the user input
    if (user_number_as_int % number_to_check) == 0: #if there is no remainder when the user input is divided by the number we're checking it against, print
      print(f"{user_number_as_int} is not a prime number.")
      break
    number_to_check += 1 #this adds 1 to the number we are checking the user input against in each loop until the loop is broken
  if number_to_check > square_root:
    print(f"{user_number_as_int} is a prime number.")
    
