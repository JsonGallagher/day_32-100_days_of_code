from random import randint
greeting_list = ["Hello", "Hola", "Bonjour", "Guten tag"]

def gen_greeting(name):
  print(f"{greeting_list[rand_num]} {name}!")

name = input("Please enter your name: ")

while True:
  rand_num = randint(0,len(greeting_list)-1)
  gen_greeting(name)
  another_greeting = input("Generate another greeting? y or n ")
  if another_greeting == 'y':
    continue
  elif another_greeting == 'n':
    break
  else:
    print("Please enter a valid response.")
  print()
