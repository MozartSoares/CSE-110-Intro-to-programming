from time import sleep

#In addition to meeting the program requirements, I ensured to prompt the verb in the correct tense to maintain story cohesion. Moreover, I added a pause using the sleep function to simulate the story generation process and provide a more immersive user experience.
#I've also added the option for the user to write another story without the need to re-run the program

def tell_clever_story():
  print('please enter the following ')

  adjective = input('one adjective: ')
  animal = input('one animal: ')
  verb = input('one present participle verb: ')
  exclamation = input('one exclamation: ').capitalize()
  second_verb = input('one present simple verb: ')
  third_verb = input('another present simple verb: ')
  
  print('wait for your clever story to be generated...')
  
  sleep(3)

  print(f''' Your story is:

  The other day, I was really in trouble. It all started when I saw a very 
  {adjective} {animal} {verb} down the hallway. "{exclamation}!" I yelled. But all 
  I could think to do was to {second_verb} over and over. Miraculously, 
  that caused it to stop, but not before it tried to {third_verb} right in front of my family.

  ''')
  tell_another()

def tell_another():
  while True:
    write_another = input("Would you like to write another story? (y/n): ").lower()
    if write_another == "y":
      tell_clever_story()
      break
    elif write_another == "n":
      print("Thank you for playing, goodbye !.")
      break
    else:
      print("Invalid input. Please enter 'y' or 'n'.")

tell_clever_story()

