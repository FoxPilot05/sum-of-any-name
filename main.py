#!/usr/bin/python

alphabet = "abcdefghijklmnopqrstuvwxyz"
forbidden = "123456789!§$%&/()=?*+#-_.:,;'\"äüö <>|^°"

def name(name): #takes a str name and returns as lowercase list
  name = name.lower()
  name = list(name)
  return name

def checkforbidden(letter): #checks if a letter is in the forbidden str
  try:
    forbidden.index(letter)
  except Exception:
    return False
  else:
    return True

def sumname():
  sum = 0 #variable stores the sum of the letters
  BigStop = False #if an unrecognizable letter is found, this turns ture and the program stops
  
  for letter in name(input("What is your name? ")): #goes through every letter in name
    if checkforbidden(letter) == True: #if in forbidden str, program ignores it
      pass
    else: #if not in forbidden str, program adds the letter's value to sum
      try:
        sum = sum + int(alphabet.index(letter))
      except Exception: #letter isnt in forbidden/alphabet str
        print(f"Weird, I cant recognise that character ({letter})")  
        BigStop = True
        
  if BigStop == False: #if no unrecognizable letters were found, program prints the sum
    print(f"The sum of your name is {sum}")
  elif BigStop == True: #if unrecognizable letters were found, program errors and restarts
    print("Please try again")
    sumname()


if __name__ == "__main__":
  sumname()

#Feedback:
#I didnt need much longer than maybe 30-45min inculding Testing
#Program was pretty easy to write