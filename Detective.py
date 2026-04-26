print('Welcome to this detective game!\n'
      "A rich 50 year old man has is suspected of being murdered, and it's your job to figure out who!\n"
      "The suspects are his daughter, the cook, the maid, and his past business partner.\n"
      "How does the saying go? It may be the one you suspect the least.\n"
      "But anyways, good luck!")

play = True
action = 1
while play == True:
    if action == 1:
        game = input('Would you like to play?')
        if game.lower() == 'yes':
            action = 2
        elif game.lower() == 'no':
            play = False
        else:
            print('Your answer must be yes or no.')