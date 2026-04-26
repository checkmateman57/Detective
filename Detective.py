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
        game = input('Would you like to play? ')
        if game.lower() == 'yes':
            action = 2
        elif game.lower() == 'no':
            play = False
        else:
            print('Your answer must be yes or no.')

    if action == 2:
        decision =  input('What would you like to do? A: Look at the victim  B: Investigate the crime scene  C: Interrogate the suspects \n')
        if decision.lower() == 'a':
            action = 3
        elif decision.lower() == 'b':
            action = 4


    if action == 3:
        decision = input('What would you like to do? A: Look at the autopsy report  B: Look at his medical records  C: Read his story  D: Go back \n')
        if decision.lower() == 'a':
            print('The autopsy report reveals that he died due to suffocation.\n'
                  'He was found by the servant in his underwear.'
                  'When examining the body, there appeared to be grip marks and scratch marks around his throat.\n'
                  'His toxicology report indicates increased levels of histamine.\n')
            time.sleep(1)
        elif decision.lower() == 'b':
            print('The medical records reveal that the victim was taking medications for high blood pressure.\n'
                  'Additionally, the victim also has a severe allergy to shellfish and peaches.\n'
                  'Lastly, he had a knee replacement surgery 2 years ago.\n')
            time.sleep(1)
        elif decision.lower() == 'c':
            print("Alistair Vane was a man who was loved by many and hated by few. At the young age of 15, he figured out a way to harness the energy from the Earth's core\n"
                  "and turn it into electricity, making energy sources like fossil fuels and solar power useless.\n"
                  "Naturally, he got very rich, but money made him into a bad person. For those that knew him, he acted like he was far superior to everyone else,"
                  "and made sure he treated anyone other than his family as inferior.\n"
                  "After he got rich, Alistair started multiple other businesses for fun, and in recent news he cut off one of his partners for undisclosed reasons.")
            time.sleep(2)
        elif decision.lower() == 'd':
            action = 2
        else:
            print('Your answer must be A, B, C, or D.')


    if action == 4:
        decision = input('Which room would you like to inspect? A: The bedroom  B: The kitchen  C: The bathroom  D: The living room  E: Go back \n')
        if decision.lower() == 'a':
            action = 5
        elif decision.lower() == 'b':
            action = 6
        elif decision.lower() == 'c':
            action = 7
        elif decision.lower() == 'd':
            action = 8
        elif decision.lower() == 'e':
            action = 2
        else:
            print('Your answer must be A, B, C, D, or E')

    if action == 5:
        decision = input('Which object would you like to inspect? A: The night stand  B: The closet  C: A journal  D: A suspicious looking wall  E: Go back \n')
        if decision.lower() == 'a':
            print("When looking through the night stand, you find an empty bottle of his blood pressure pills.\n")
            time.sleep(1)
        elif decision.lower() == 'b':
            print("When you open the closet, it is filled with pristine clothes. However, you notice that one of the shirts hanging seems to be stained with marinara sauce.\n")
            time.sleep(1)
        elif decision.lower() =='c':
            print("Journals are always great to find clues. You go the most recent entries and find one dated the day he died.\n"
                  "It reads: One of my old business partners came today to have a chat with me. We had a nice meal and drink, and then he went on his way.\n")
            time.sleep(2)
            print('You decide to go to another entry a few days ago that reads:\n'
                  ' My daughter came today asking for money to buy a designer purse. I declined, she needs to learn how to make money. She was very upset with me.\n')
            time.sleep(2)
        elif decision.lower() == 'd':
            print('You feel along a wall and notice some hairline gaps in the shape of a square. You knock in that area, and it feels a little hollow.\n'
                  'After more searching, you find a button underneath the bed and press it, and the area along the wall opens.\n'
                  'In it, you find blocks of cash along with a note: Emergency funds, $100 000 in this location.\n'
                  'You count the money: Exactly $100 000.')
            time.sleep(3)
        elif decision.lower() == 'e':
            action = 4
        else:
            print('Your answer must be A, B, C, D or E')


    if action == 6:
        decision = input('What would you like to inspect? A: The trash  B: The sink  C: The fridge  D: Cabinets  E: Go back \n')
        if decision.lower() == 'a':
            print("When you take a look inside the trash can, you find clam shells, and another empty bottle of his pills.\n")
            time.sleep(1)
        elif decision.lower() == 'b':
            print("In the sink you find some dirty dishes. A few of the plates look like pasta has been eaten from them. \n"
                  "The others show remnants of pastries, and you find a couple cups with bits of coffee grounds of the bottom.\n")
            time.sleep(2)
        elif decision.lower() == 'c':
            print("When you inspect the fridge, it all seems normal. There's your cheeses, fruits, vegetables, and deli meats. \n"
                  "When you look at the freezer, it's filled with beef, pork, and lamb. But you also see some clams and shrimp. \n")
            time.sleep(2)
        elif decision.lower() =='d':
            print("You go through a few cabinets seeing the normal pots and pans. However, on one cabinet, you find a hidden compartment on the bottom with another stack of cash. \n"
                  "It reads: Emergency funds: $50 000. You count it out, and it checks out.")
        elif decision.lower() == 'e':
            action = 4
        else:
            print('Your answer must be A, B, C, D, or E')