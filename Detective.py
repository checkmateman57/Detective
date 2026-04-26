print('Welcome to this detective game!\n'
      "A rich 50 year old man has is suspected of being murdered, and it's your job to figure out who!\n"
      "The suspects are his daughter, the cook, the maid, and his past business partner.\n"
      "How does the saying go? It may be the one you suspect the least.\n"
      "But anyways, good luck!")

import time
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

    if action == 2:
        decision =  input('What would you like to do? A: Look at the victim  B: Investigate the crime scene  C: Interrogate the suspects ')
        if decision.lower() == 'a':
            action = 3


    if action == 3:
        decision = input('What would you like to do? A: Look at the autopsy report  B: Look at his medical records  C: Read his story  D: Go back ')
        if decision.lower() == 'a':
            print('The autopsy report reveals that he died due to suffocation.\n'
                  'When examining the body, there appeared to be grip marks and scratch marks around his throat.\n'
                  'His toxicology report indicates increased levels of histamine.\n')
            time.sleep(1)
        elif decision.lower() == 'b':
            print('The medical records reveal that the victim was taking medications for high blood pressure.\n'
                  'Additionally, the victim also has a severe allergy to shellfish and peaches.\n'
                  'Lastly, he had a knee replacement surgery 2 years ago.\n')
            time.sleep(1)
        elif decision.lower() == 'c':
            print("Alistair Vane was a man who was loved by many and hated by few. At the young age of 15, he figured out a way to harness the energy from the Earth's core"
                  " and turn it into electricity, making energy sources like fossil fuels and solar power useless.\n"
                  "Naturally, he got very rich, but money made him into a bad person. For those that knew him, he acted like he was far superior to everyone else,"
                  "and made sure he treated anyone other than his family as inferior.\n"
                  "After he got rich, Alistair started multiple other businesses for fun, and in recent news he cut off one of his partners for undisclosed reasons.")
            time.sleep(2)
        elif decision.lower() == 'd':
            action = 2
        else:
            print('Your answer must be A, B, C, or D.')