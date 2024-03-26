import random
from hangman_words import word_list
from hangman_art import stages


pick= random.choice(word_list)
print(pick)

for i in range(len(pick)):
  new= i+1
spaces = "_"* new
listed_spaces = list(spaces)

print(spaces)
new_stage= len(stages)
game = True

empty=[]
for x in range(len(pick)):
  empty += "_"

while game == True:
  guess=input("guess a letter\n")
  for position in range(len(pick)):
    letter=pick[position]
    if guess == letter:
      empty[position]=guess
      print("".join(empty))
    elif guess in empty:
      print("you've already guessed that letter")
      if '_' not in empty:
        print("you won!")
        game= False
  if guess not in pick:
    new_stage-=1
    print(stages[new_stage])
    if new_stage == 0:
      game = False
      print("Game Over")

      
      print(empty)



    #   listed_spaces[index] = guess
    #   new_string = "".join(listed_spaces)
    #   print(new_string)

    # else:
    #   new_stage-=1
    #   print(stages[new_stage])
    #   if new_stage == 0:
    #     game = False
    #     print("Game Over")

    # else:
    #     print("Game Over") 



#     if guess == letter:
#         letter
#        index= pick.index(guess)
#        listed_spaces[index] = guess
#        new_string = "".join(listed_spaces)
#        print(new_string)

#   else:
#     new_stage-=1
#     print(stages[new_stage])
#     if new_stage == 0:
#       game = False
#       print("Game Over")

# else:
#   print("Game Over") 

