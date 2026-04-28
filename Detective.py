print('Welcome to this detective game!\n'
      "A rich 50 year old man has is suspected of being murdered, and it's your job to figure out who!\n"
      "The suspects are his daughter, the cook, the butler, and his past business partner.\n"
      "How does the saying go? It may be the one you suspect the least.\n"
      "But anyways, good luck!")

import time
play = True
action = 1
while play == True:
    if action == 1:
        game = input('Would you like to play? ')
        if game.lower() == 'yes':
            stage1 = 0
            stage2 = 0
            stage3 = 0
            ButlerEvidence = False
            CookEvidence = False
            DaughterEvidence = False
            PartnerEvidence = False
            ButlerInterrogation = False
            CookInterrogation = False
            PartnerInterrogation = False
            DaughterInterrogation = False
            action = 2
        elif game.lower() == 'no':
            play = False
        else:
            print('Your answer must be yes or no.')

    if action == 2:
        decision =  input('What would you like to do? A: Look at the victim  B: Investigate the crime scene  C: Interrogate the suspects D: Make your arrest \n')
        if decision.lower() == 'a':
            action = 3
        elif decision.lower() == 'b':
            action = 4
        elif decision.lower() == 'c':
            action = 9


    if action == 3:
        decision = input('What would you like to do? A: Look at the autopsy report  B: Look at his medical records  C: Read his story  D: Go back \n')
        if decision.lower() == 'a':
            print('The autopsy report reveals that he died due to suffocation.\n'
                  'He was in his bedroom, in only his underwear, and was found by the servant. \n'
                  'When examining the body, there appeared to be grip marks and scratch marks around his throat.\n'
                  'His toxicology report indicates increased levels of histamine, and a drop in arterial pressure at time of death\n')
            time.sleep(1)
            stage1 += 1
        elif decision.lower() == 'b':
            print('The medical records reveal that the victim was taking medications for high blood pressure.\n'
                  'Additionally, the victim also has a severe allergy to shellfish and peaches.\n'
                  'Lastly, he had a knee replacement surgery 2 years ago.\n')
            time.sleep(1)
            stage1 += 1
        elif decision.lower() == 'c':
            print("Alistair Vane was a man who was loved by many and hated by few. At the young age of 15, he figured out a way to harness the energy from the Earth's core\n"
                  "and turn it into electricity, making energy sources like fossil fuels and solar power useless.\n"
                  "Naturally, he got very rich, but money made him into a bad person. For those that knew him, he acted like he was far superior to everyone else,"
                  "and made sure he treated anyone other than his family as inferior.\n"
                  "After he got rich, Alistair started multiple other businesses for fun, and in recent news he cut off one of his partners for undisclosed reasons.")
            time.sleep(2)
            stage1 += 1
        elif decision.lower() == 'd':
            action = 2
        else:
            print('Your answer must be A, B, C, or D.')


    if action == 4:
        if stage1 < 1:
            print('Woah There, please look at minimum 1 thing from the victim first before you can investigate.')
            action = 2
        else:
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
            ButlerEvidence = True
            time.sleep(1)
            stage2 += 1
        elif decision.lower() == 'b':
            print("When you open the closet, it is filled with pristine clothes. However, you notice that one of the shirts hanging seems to be stained with marinara sauce.\n")
            time.sleep(1)
            stage2 += 1
        elif decision.lower() =='c':
            print("Journals are always great to find clues. You go the most recent entries and find one dated the day he died.\n"
                  "It reads: One of my old business partners came today to have a chat with me. We had a nice meal and drink, and then he went on his way.\n")
            time.sleep(2)
            print('You decide to go to another entry a few days ago that reads:\n'
                  ' My daughter came today asking for money to buy a designer purse. I declined, she needs to learn how to make money. She was very upset with me.\n')
            time.sleep(2)
            stage2 += 1
        elif decision.lower() == 'd':
            print('You feel along a wall and notice some hairline gaps in the shape of a square. You knock in that area, and it feels a little hollow.\n'
                  'After more searching, you find a button underneath the bed and press it, and the area along the wall opens.\n'
                  'In it, you find blocks of cash along with a note: Emergency funds, $100 000 in this location.\n'
                  'You count the money: Exactly $100 000. \n')
            time.sleep(3)
            stage2 += 1
        elif decision.lower() == 'e':
            action = 4
        else:
            print('Your answer must be A, B, C, D or E')


    if action == 6:
        decision = input('What would you like to inspect? A: The trash  B: The sink  C: The fridge  D: Cabinets  E: Go back \n')
        if decision.lower() == 'a':
            print("When you take a look inside the trash can, you find clam shells, and another empty bottle of his pills.\n")
            time.sleep(1)
            ButlerEvidence = True
            CookEvidence = True
            stage2 += 1
        elif decision.lower() == 'b':
            print("In the sink you find some dirty dishes. A few of the plates look like pasta has been eaten from them. \n"
                  "The others show remnants of pastries, and you find a couple cups with bits of coffee grounds of the bottom.\n")
            time.sleep(2)
            stage2 += 1
        elif decision.lower() == 'c':
            print("When you inspect the fridge, it all seems normal. There's your cheeses, fruits, vegetables, and deli meats. \n"
                  "When you look at the freezer, it's filled with beef, pork, and lamb. But you also see some clams and shrimp. \n")
            time.sleep(2)
            stage2 += 1
        elif decision.lower() =='d':
            print("You go through a few cabinets seeing the normal pots and pans. However, on one cabinet, you find a hidden compartment on the bottom with another stack of cash. \n"
                  "It reads: Emergency funds: $50 000. You count it out, and it checks out. \n")
            time.sleep(2)
            stage2 += 1
        elif decision.lower() == 'e':
            action = 4
        else:
            print('Your answer must be A, B, C, D, or E')


    if action == 7:
        decision = input('Which object would you like to inspect? A: The medicine cabinet  B: Sink  C: Laundry hamper  D: Shower wall  E: Go back \n')
        if decision.lower() == 'a':
            print("When you open the cabinet, you find pill bottles, average pain relievers, vitamins, and toiletries. \n"
                  "You decide to take a look at one of the blood pressure pill bottles. \n"
                  "It is nearly half empty, despite the date of fulfillment being 5 days ago, with a count of 40 pills and instructions to take 1 every day.\n")
            time.sleep(3)
            ButlerEvidence = True
            stage2 += 1
        elif decision.lower() == 'b':
            print("When inspecting the sink, you find dried up streaks of mascara. \n")
            time.sleep(1)
            stage2 += 1
        elif decision.lower() == 'c':
            print("When you open the hamper, you find some guest hand towels that were used. \n")
            time.sleep(1)
            stage2 += 1
        elif decision.lower() == 'd':
            print("You notice an area along the shower wall that looks suspicious, so you press around it and something clicks. \n"
                  "Another case opens up with stacks of cash. It reads: Emergency funds, $50 000. This time, there's only $40 000 inside, and a note that reads: \n"
                  '"Consider this my weekly salary" \n')
            PartnerEvidence = True
            time.sleep(3)
            stage2 += 1
        elif decision.lower() == 'e':
            action = 4
        else:
            print('Your answer must be A, B, C, D, or E')


    if action == 8:
        decision = input("Which object would you like to inspect? A: The carpet  B: The desk  C: A chair  D: A painting on the wall  E: Go back \n")
        if decision.lower() == 'a':
            print("When you get down and look at the carpet, you notice a sauce stain, so you decide to look into it further. \n"
                  "You go to the trash to see some spaghetti noodles, and they smell a little ocean-like. \n")
            CookEvidence = True
            time.sleep(2)
            stage2 += 1
        elif decision.lower() == 'b':
            print("You go to the desk and find a laptop open with an email chain. It's between Alistair and his daughter. \n"
                  "Alistair has the second last message saying I'm cutting your allowance to $10 000 a month. You need to get a job and earn money. \n"
                  "His daughter responded with Screw you Dad! I'm going to make you pay me more.")
            DaughterEvidence = True
            time.sleep(3)
            stage2 += 1
        elif decision.lower() == 'c':
            print("You look over a comfy chair, and see a note tucked in between the armrest and the cushion. \n"
                  'It reads: "I will make sure the world knows what kind of person you are. Just because you invented some energy source 30 years ago does not mean you are God." \n')
            time.sleep(2)
            PartnerEvidence = True
            stage2 += 1
        elif decision.lower() == 'd':
            print("The painting seems interesting enough but you've read mystery books before. \n"
                  "You take the painting off, and behind is another stack of cash, with a note. \n"
                  '"Emergency funds: $27 000" There is $27000 inside, but the type of writing on the note seems a bit feminine. \n')
            DaughterEvidence = True
            time.sleep(3)
            stage2 += 1
        elif decision.lower() == 'e':
            action = 4
        else:
            print('Your answer must be A, B, C, D, or E')


    if action == 9:
        decision = input('Who would you like to interrogate? A: The butler  B: The cook  C: The daughter  D: The business partner  E: Go back \n'
                         'Please note: You can only interrogate them one time. \n')
        if decision.lower() == 'a':
            action = 10
        elif decision.lower() == 'b':
            action = 11
        elif decision.lower() == 'c':
            action = 12
        elif decision.lower() == 'd':
            action = 13
        elif decision.lower() == 'e':
            action = 2
        else:
            print('Your answer must be A, B, C, D, or E')

    if action == 10:
        if ButlerInterrogation == True:
            print("You already interrogated the butler! You can't do that again")
            action = 9
        else:
            decision = input('You are now interrogating the butler. Before we start, would you like to know some background info on the butler? \n')
            if decision.lower() == 'yes':
                print("The butler is a 25 year old male, and holds a warehouse job during the night. He's trying to support his parents as well, as they are struggling. \n"
                      "His parents also suffer from blood pressure issues, and bottles are getting expensive. \n")
            decision = input('What would you like to ask the butler? \n'
                             'A: What were you doing up to the moment of his death? \n'
                             'B: What are your duties as a butler to Alistair? \n')
            if decision.lower() == 'a':
                print("I was having dinner with the cook in the kitchen, and when I finished my meal, I went to check on Alistair.")
                answer = False
                while answer == False:
                    decision = input('What is your next question? \n'
                                     'A: What did you have for dinner? \n'
                                     "B: Did you hear anything coming from Alistair's room? \n")
                    if decision.lower() == 'a':
                        print('I had a seafood pasta for dinner.')
                        time.sleep(1)
                        print('Anything else you would like to tell me?')
                        time.sleep(2)
                        print("No, that's all.")
                        time.sleep(1)
                        print('Your interview with the butler has finished')
                        ButlerInterrogation = True
                        answer = True
                        action = 9
                    elif decision.lower() == 'b':
                        print("No, I can't say that I did")
                        time.sleep(1)
                        print("And when you went into the room, what did you see? \n")
                        time.sleep(1)
                        print("I saw Alistair down on the bed, with food sprawled over him, he wasn't breathing, and he had no pulse. He was dead. \n")
                        time.sleep(1)
                        print('Anything else you would like to tell me?')
                        time.sleep(2)
                        print("No, that's all.")
                        time.sleep(1)
                        print('Your interview with the butler has finished')
                        ButlerInterrogation = True
                        answer = True
                        action = 9
                    else:
                        print('Your answer must be A or B')
            elif decision.lower() == 'b':
                print("My duties involve greeting guests, helping Alistair with tasks, such as giving him his medication, selecting/prepping his clothes, and getting him drinks. \n")
                time.sleep(1)
                answer = False
                while answer == False:
                    decision = input('What would your next question be? \n'
                                     'A: Had Alistair been acting weird today, or saying anything unusual? \n'
                                     'B: Could you go more into length about his medication, such as when you give him the pills, how many, stuff like that? \n')
                    if decision.lower() == 'a':
                        print('Alistair had a couple visitors today, his daughter and his old business partner. After both of them had their visits, we were having a conversation. \n'
                              'He was saying about he was afraid of his daughter, and for his business partner, he was expressing dissatisfaction.')
                        time.sleep(2)
                        answer = True
                        answer1 = False
                        while answer1 == False:
                            decision = input('What is your next question? \n'
                                             'A: What did he say about his daughter? \n'
                                             'B: What did he say about his old business partner? \n')
                            if decision.lower() == 'a':
                                print("He said that he was concerned that she wouldn't survive out in the real world without depending on him for money, \n"
                                      "and that she might go to drastic measures to get her money. \n")
                                time.sleep(3)
                                print('Anything else you would like to tell me?')
                                time.sleep(2)
                                print("No, that's all.")
                                time.sleep(1)
                                print('Your interview with the butler has finished')
                                ButlerInterrogation = True
                                answer1 = True
                                action = 9
                            elif decision.lower() == 'b':
                                print("He said that he hasn't realized yet that his proposed business model was stupid, and that he would cost the company millions. \n"
                                      "He is still quite angry at me for firing him. \n")
                                time.sleep(2)
                                print('Anything else you would like to tell me?')
                                time.sleep(2)
                                print("No, that's all.")
                                time.sleep(1)
                                print('Your interview with the butler has finished')
                                ButlerInterrogation = True
                                answer1 = True
                                action = 9
                            else:
                                print('Your answer must be A or B')
                    elif decision.lower() == 'b':
                        print("When we talk about administering his blood pressure medication, it's usually once per day, along with his meal. \n"
                              "If his blood pressure is unusually bad, I'll give him 2 for the day\n")
                        time.sleep(2)
                        answer = True
                        if ButlerEvidence == False:
                            print('When did you give him his medication on the day of his death?')
                            time.sleep(3)
                            print('I gave him his medication along with dinner, due to his visitors earlier in the day.')
                            time.sleep(2)
                            print('Anything else you would like to tell me?')
                            time.sleep(2)
                            print("No, that's all.")
                            time.sleep(1)
                            print('Your interview with the butler has finished')
                            ButlerInterrogation = True
                            action = 9
                        else:
                            answer1 = False
                            while answer1 == False:
                                decision = input("What is your next question? \n"
                                                 "A: When did you give him his medication on the day of his death? \n"
                                                 "B: I've noticed a few empty pill bottles, care to explain that for me? \n")
                                if decision.lower() == 'a':
                                    print('I gave him his medication along with dinner, due to his visitors earlier in the day.')
                                    time.sleep(2)
                                    print('Anything else you would like to tell me?')
                                    time.sleep(2)
                                    print("No, that's all.")
                                    time.sleep(1)
                                    print('Your interview with the butler has finished')
                                    ButlerInterrogation = True
                                    answer1 = True
                                    action = 9
                                elif decision.lower() == 'b':
                                    print("The butler starts breaking down about how he's been stealing pills from Alistair so his parents could get the medication they needed. \n"
                                          "He starts breaking down about how poor they are, and how this was the only way they could get their pills in a continuous stream. \n"
                                          "He pleads that you don't arrest him, since it didn't hurt Alistair in any way.")
                                    decision = input('Will you arrest him? Yes or no \n')
                                    if decision.lower() == 'yes':
                                        print('You arrest the butler and he is taken away')
                                    else:
                                        print('The butler thanks you many times over.')
                                    print('Your interview with the butler has finished')
                                    ButlerInterrogation = True
                                    answer1 = True
                                    action = 9
                                else:
                                    print('Your answer must be A or B')
                else:
                    print('Your answer must be A or B')

            else:
                print('You must choose A or B')


    if action == 11:
        if CookInterrogation == True:
            print("You already interrogated the cook! You can't do that again.")
            action = 9
        else:
            decision = input('You are now interrogating the cook. Before we start, would you like to have some background info on the cook? \n')
            if decision.lower() == 'yes':
                print('The cook is a single 24 year old, who recently graduated from culinary school. He lives by himself in a rented apartment, and can be described as quite egotistical. \n')
                time.sleep(2)
            decision = input('What would you like to ask? \n'
                             'A: How is your relationship with Alistair? \n'
                             'B: What were you doing the evening when Alistair died? \n')
            if decision.lower() == 'a':
                print("In all honesty, I wouldn't say we had a good relationship. He kept insulting my cooking disliked some of my dishes, so I wasn't very happy with him.")
                time.sleep(1)
                answer = False
                while answer == False:
                    decision = input('What would you like to ask next? \n'
                                     "A: If you don't like him, why did you continue to work for him? \n"
                                     "B: Has there been any tension between the two of you lately? \n")
                    if decision.lower() == 'a':
                        print("Because it pays well, I'm getting $30 000 a month. \n")
                        time.sleep(1)
                        answer = True
                        answer1 = False
                        while answer1 == False:
                            decision = input('What would you like to ask next? \n'
                                             "A: Why's he paying you so high? \n"
                                             "B: Has he at least complimented your cooking? \n")
                            if decision.lower() == 'a':
                                print("Because the guy is made of money, 30k is pocket change. Also, I'm sure he wants the best the market has to offer, and I'm the best. \n")
                                time.sleep(1)
                                answer1 = True
                                print('Anything else you would like to tell me?')
                                time.sleep(2)
                                print("No, that's all.")
                                time.sleep(1)
                                print('Your interview with the cook has finished')
                                CookInterrogation = True
                                answer = True
                                action = 9
                            elif decision.lower() == 'b':
                                print('He has, but rarely does. He does seem to like my Beef Wellington the most though.')
                                time.sleep(1)
                                answer1 = True
                                print('Anything else you would like to tell me?')
                                time.sleep(2)
                                print("No, that's all.")
                                time.sleep(1)
                                print('Your interview with the cook has finished')
                                CookInterrogation = True
                                answer = True
                                action = 9
                            else:
                                print('Your answer must be A or B')
                    elif decision.lower() == 'b':
                        print('Actually we did. Last week, he was telling me that my steak was overcooked, when I knew that is was a pristine medium rare. \n'
                              'We got into an argument about it. \n')
                        time.sleep(2)
                        answer = True
                        answer1 = False
                        while answer1 == False:
                            decision = input('What would you like to ask next? \n'
                                             'A: What did you do after your argument? \n'
                                             "B: How would've you liked to respond to him? \n")
                            if decision.lower() == 'a':
                                print("I honestly was ready to start looking for new jobs, but he's paying me pretty well, and I need to pay off culinary school. \n")
                                time.sleep(1)
                                answer1 = True
                                print('Anything else you would like to tell me?')
                                time.sleep(2)
                                print("No, that's all.")
                                time.sleep(1)
                                print('Your interview with the cook has finished')
                                CookInterrogation = True
                                answer = True
                                action = 9
                            elif decision.lower() == 'b':
                                print("I would've like to get some random dude off the street to cook him a steak and see how he likes it so he can start appreciating me. \n")
                                time.sleep(1)
                                answer1 = True
                                print('Anything else you would like to tell me?')
                                time.sleep(2)
                                print("No, that's all.")
                                time.sleep(1)
                                print('Your interview with the cook has finished')
                                CookInterrogation = True
                                answer = True
                                action = 9
                            else:
                                print('Your answer must be A or B')
                    else:
                        print('Your answer must be A or B')
            elif decision.lower() == 'b':
                print('I was in the kitchen as normal, making dinner.')
                time.sleep(1)
                answer = False
                while answer == False:
                    decision = input('What would you like to ask next? \n'
                                     'A: What did you make for dinner? \n'
                                     'B: Did anything unusual happen while making dinner? \n')
                    if decision.lower() == 'a':
                        print('I was making a pasta with a tomato sauce base and some ground beef as the protein.')
                        time.sleep(1)
                        answer = True
                        if CookEvidence == False:
                            print("And does food ever leave the kitchen? Where do you eat?")
                            time.sleep(1)
                            print("Me and the butler eat in the kitchen, while I go through the living room to Alistair's room and give him his food.")
                            time.sleep(1)
                            print('Anything else you would like to tell me?')
                            time.sleep(2)
                            print("No, that's all.")
                            time.sleep(1)
                            print('Your interview with the cook has finished')
                            CookInterrogation = True
                            answer = True
                            action = 9
                        else:
                            answer = True
                            answer1 = False
                            while answer1 == False:
                                decision = input("What would you like to ask next? \n"
                                                 "A: And does food ever leave the kitchen, Where do you eat? \n"
                                                 "B: I noticed some clams, do you have anything to say about that? \n")
                                if decision.lower() == 'a':
                                    print("Me and the butler eat in the kitchen, while I go through the living room to Alistair's room and give him his food.")
                                    time.sleep(1)
                                    print('Anything else you would like to tell me?')
                                    time.sleep(2)
                                    print("No, that's all.")
                                    time.sleep(1)
                                    print('Your interview with the cook has finished')
                                    CookInterrogation = True
                                    answer1 = True
                                    action = 9
                                elif decision.lower() == 'b':
                                    print("Oh yeah, about that. That was for me and the butler, cus Alistair's allergic.")
                                    time.sleep(1)
                                    print('Anything else you would like to tell me?')
                                    time.sleep(2)
                                    print("No, that's all.")
                                    time.sleep(1)
                                    print('Your interview with the cook has finished')
                                    CookInterrogation = True
                                    answer1 = True
                                    action = 9
                                else:
                                    print('Your answer must be A or B')
                    elif decision.lower() == 'b':
                        print('No, nothing happened, it was business as usual. Maybe the butler came into the kitchen a few times but that was all. \n')
                        time.sleep(1)
                        answer = True
                        print('Anything else you would like to tell me?')
                        time.sleep(2)
                        print("No, that's all.")
                        time.sleep(1)
                        print('Your interview with the cook has finished')
                        CookInterrogation = True
                        answer1 = True
                        action = 9
                    else:
                        print('Your answer must be A or B')
            else:
                print('Your answer must be A or B')


    if action == 12:
        if DaughterInterrogation == True:
            print("You already interrogated the daughter! You can't do that again.")
            action = 9
        else:
            decision = input('You are now interrogating the daughter. Before you start, would you like to have some background information? \n')
            if decision.lower() == 'yes':
                print("Alistair's daughter is 20 years old, and single. As a kid, she constantly got spoiled and got everything she wanted. \n"
                      "In the past couple of years, Alistair realized his mistake and started spending less money on her, until she hopefully became self-sufficient. \n"
                      "However, it takes a long time for a bad habit to get fixed, especially if they grew up that way...\n")
                time.sleep(3)
            decision = input('What would you like to ask? \n'
                             'A: How is your relationship with your father? \n'
                             'B: What happened during your visit that day? \n')
            if decision.lower() == 'a':
                print("Right now our relationship isn't too good. He's cutting me off financially. But I wouldn't kill him for that. ")
                time.sleep(1)
                answer = False
                while answer == False:
                    decision = input("What would you like to ask next? \n"
                                     "A: So then how are you surviving with being cut off? \n"
                                     "B: Do you know of anyone else who might need money? \n")
                    if decision.lower() == 'a':
                        print("I drastically reduced my spending, and I'm looking at getting a job. \n")
                        time.sleep(1)
                        answer = True
                        if DaughterEvidence == True:
                            answer1 = False
                            while answer1 == False:
                                decision = input("What would you like to ask next? \n"
                                                 "A: I noticed an e-mail chain saying how you'd make your dad pay. Care to explain? \n"
                                                 "B: Can you write the words Emergency Funds: $27 000? \n")
                                if decision.lower() == 'a':
                                    print("I was planning on suing my dad for leaving me unable to function in the real world, so I could get some money. \n")
                                    time.sleep(1)
                                    print('Anything else you would like to tell me?')
                                    time.sleep(2)
                                    print("No, that's all.")
                                    time.sleep(1)
                                    print('Your interview with the daughter has finished')
                                    DaughterInterrogation = True
                                    answer1 = True
                                    action = 9
                                elif decision.lower() == 'b':
                                    print('She writes the words, and as you compare them with the note you found in the living room, they match. \n')
                                    time.sleep(2)
                                    print('Anything else you would like to tell me?')
                                    time.sleep(2)
                                    print("No, that's all.")
                                    time.sleep(1)
                                    print('Your interview with the daughter has finished')
                                    DaughterInterrogation = True
                                    answer1 = True
                                    action = 9
                                else:
                                    print('Your answer must be A or B')
                        else:
                            print('Anything else you would like to tell me?')
                            time.sleep(2)
                            print("No, that's all.")
                            time.sleep(1)
                            print('Your interview with the daughter has finished')
                            DaughterInterrogation = True
                            action = 9
                    elif decision.lower() == 'b':
                        print("I'm pretty sure the butler needs money to support his family, and the cook needs to pay off student loans. \n"
                              "One of his old business partners is looking for compensation as well. \n")
                        time.sleep(2)
                        answer = True
                        answer1 = False
                        while answer1 == False:
                            decision = input('What would you like to ask next? \n'
                                             'A: Tell me more about his old business partner. \n'
                                             'B: Would any of them kill him for his money? \n')
                            if decision.lower() == 'a':
                                print('Well he started some random business with this guy, and I believe his partner came up to him with a proposition at one point. \n'
                                      'My dad got pretty angry at him for such an idea, and proceeded to remove him as partner. That got his partner pretty riled up.\n')
                                time.sleep(2)
                                print('Anything else you would like to tell me?')
                                time.sleep(2)
                                print("No, that's all.")
                                time.sleep(1)
                                print('Your interview with the daughter has finished')
                                DaughterInterrogation = True
                                answer1 = True
                                action = 9
                            elif decision.lower() == 'b':
                                print("The butler seems to nice of a guy and pretty fearful, so I wouldn't think it's him. I haven't had much interaction with the cook, but he's pretty chill. \n"
                                      "As for the old business partner, depending on how much pent up anger he has, he might have done something to my father. \n")
                                time.sleep(2)
                                print('Anything else you would like to tell me?')
                                time.sleep(2)
                                print("No, that's all.")
                                time.sleep(1)
                                print('Your interview with the daughter has finished')
                                DaughterInterrogation = True
                                answer1 = True
                                action = 9
                            else:
                                print('Your answer must be A or B')
                    else:
                        print('Your answer must be A or B')
            elif decision.lower() == 'b':
                print('I came in to have a chat with my father, and I wanted him to buy me a designer purse all my friends had. He said no')
                time.sleep(1)
                answer = False
                while answer == False:
                    decision = input("What would you like to ask next? \n"
                                     "A: How did you respond to his rejection? \n"
                                     "B: When was the last time he's accepted purchasing stuff like that for you? \n")
                    if decision.lower() == 'a':
                        print("I kind of expected it, but I still got angry at him, telling how hard my life's been since he's cut me off, and how he ruined me. \n")
                        time.sleep(1)
                        answer = True
                        answer1 = False
                        while answer1 == False:
                            decision = input("What would you like to ask next? \n"
                                                     "A: How do you survive now with less money? \n"
                                                     "B: Has he tried helping you get on your feet? \n")
                            if decision.lower() == 'a':
                                print("I still get a small allowance, and I'm looking at jobs. I can live, but I can't live comfortably. \n")
                                time.sleep(1)
                                print('Anything else you would like to tell me?')
                                time.sleep(2)
                                print("No, that's all.")
                                time.sleep(1)
                                print('Your interview with the daughter has finished')
                                DaughterInterrogation = True
                                answer1 = True
                                action = 9
                            elif decision.lower() == 'b':
                                print("I mean he's given me some allowance and some advice on how to stay afloat, but I think he's trying to make me more independent, so therefore not really. \n"
                                      "I think he's getting more harsh on me now. \n")
                                time.sleep(2)
                                print('Anything else you would like to tell me?')
                                time.sleep(2)
                                print("No, that's all.")
                                time.sleep(1)
                                print('Your interview with the daughter has finished')
                                DaughterInterrogation = True
                                answer1 = True
                                action = 9
                            else:
                                print('Your answer must be A or B')
                    elif decision.lower() == 'b':
                        print("He hasn't bought anything really expensive for me for like a year now. I understand why, but I still don't like the reason why.\n")
                        time.sleep(1)
                        answer = True
                        answer1 = False
                        while answer1 == False:
                            decision = input("What would you like to ask next? \n"
                                             "A: So how do you survive then with less money? \n"
                                             "B: And you've never stolen money from him, right? \n")
                            if decision.lower() == 'a':
                                print("I still get some money so I can live, but I can't live extravegently, it's so tiring. \n")
                                time.sleep(1)
                                print('Anything else you would like to tell me?')
                                time.sleep(2)
                                print("No, that's all.")
                                time.sleep(1)
                                print('Your interview with the daughter has finished')
                                DaughterInterrogation = True
                                answer1 = True
                                action = 9
                            elif decision.lower() == 'b':
                                print('Right...')
                                time.sleep(3)
                                print('Never')
                                time.sleep(2)
                                print('Anything else you would like to tell me?')
                                time.sleep(2)
                                print("No, that's all.")
                                time.sleep(1)
                                print('Your interview with the daughter has finished')
                                DaughterInterrogation = True
                                answer1 = True
                                action = 9
                            else:
                                print('Your answer must be A or B')
                    else:
                        print('Your answer must be A or B')
            else:
                print('Your answer must be A or B')


    if action == 13:
        if PartnerInterrogation == True:
            print("You already interrogated the business partner! You can't do that again.")
            action = 9
        else:
            decision = input("You are now interrogating the business partner. Before you start, would you like to know some background info? \n")
            if decision.lower() == 'yes':
                print("The business partner is a married 35 year old male. 5 years ago, he and Alistair started a managing business. \n"
                      "All went smooth for them for 4 years, until last year, he had a proposition for Alistair on how to make the business better. \n"
                      "Alistair disagreed, they got into an argument, and it led into the partner being fired and Alistair assuming control of the business. \n")
            decision = input('What would you like to ask? \n'
                             'A: What happened in your business ventures with Alistair? \n'
                             'B: What happened in your meeting with Alistair that day? \n')
            if decision.lower() == 'a':
                print("So me and Alistair started a management firm together, and it was going pretty good. \n"
                      "Just last year, I had a stellar idea on how to improve the business, but he rejected my idea. \n"
                      "I got pretty heated, and we got into a huge argument, and then I left the firm. \n")
                time.sleep(3)
                answer = False
                while answer == False:
                    decision = input('What would you like to ask next? \n'
                                     'A: Why did he reject your idea? \n'
                                     'B: Why did you leave the firm? \n')
                    if decision.lower() == 'a':
                        print("He said that it was a stupid idea that would cost the firm millions. \n"
                              "In my opinion, I think it's because he couldn't bear the thought that someone other than him had a good idea. \n")
                        time.sleep(2)
                        answer = True
                        answer1 = False
                        while answer1 == False:
                            decision = input('What would you like to ask next? \n'
                                             'A: Were you looking to seek any action against Alistair? \n'
                                             'B: Had tensions between you and Alistair existed before that argument? How strong did they last afterwards? \n')
                            if decision.lower() == 'a':
                                print("I wanted to go to the news and expose what kind of person he is. \n"
                                      "He thinks he's so high and mighty, and I want people to realize that. \n")
                                time.sleep(2)
                                print('Anything else you would like to tell me?')
                                time.sleep(2)
                                print("No, that's all.")
                                time.sleep(1)
                                print('Your interview with the business partner has finished')
                                PartnerInterrogation = True
                                answer1 = True
                                action = 9
                            elif decision.lower() == 'b':
                                print("I mean yeah, they existed before the argument. After all, I was a partner to this guy. \n"
                                      'I was technically an equal to this "High and Mighty guy" \n')
                                time.sleep(1)
                                print('Anything else you would like to tell me?')
                                time.sleep(2)
                                print("No, that's all.")
                                time.sleep(1)
                                print('Your interview with the business partner has finished')
                                PartnerInterrogation = True
                                answer1 = True
                                action = 9
                            else:
                                print('Your answer must be A or B')
                    elif decision.lower() == 'b':
                        print("I left the firm because there was some serious pressure from him, and also the fact that I couldn't stand being around this guy. \n")
                        time.sleep(1)
                        answer = True
                        if PartnerEvidence == False:
                            print('Were you going to seek any action against him? \n')
                            time.sleep(1)
                            print("I was going to go to the media so the world could see what kind of person he was. \n")
                            time.sleep(1)
                            print('Anything else you would like to tell me?')
                            time.sleep(2)
                            print("No, that's all.")
                            time.sleep(1)
                            print('Your interview with the business partner has finished')
                            PartnerInterrogation = True
                            action = 9
                        else:
                            answer1 = False
                            while answer1 == False:
                                decision = input('What would you like to ask next? \n'
                                                 'A: Were you going to seek any action against Alistair? \n'
                                                 'B: I noticed some cash missing in a bathroom you were in along with a note. Was that you? \n')
                                if decision.lower() == 'a':
                                    print("I was going to go to the media so the world could see what kind of person he was. \n")
                                    time.sleep(1)
                                    print('Anything else you would like to tell me?')
                                    time.sleep(2)
                                    print("No, that's all.")
                                    time.sleep(1)
                                    print('Your interview with the business partner has finished')
                                    PartnerInterrogation = True
                                    answer1 = True
                                    action = 9
                                elif decision.lower() == 'b':
                                    print("Yes that was me. I consider it compensation for what he did to me. \n")
                                    time.sleep(1)
                                    print('Anything else you would like to tell me?')
                                    time.sleep(2)
                                    print("No, that's all.")
                                    time.sleep(1)
                                    print('Your interview with the business partner has finished')
                                    PartnerInterrogation = True
                                    answer1 = True
                                    action = 9
                                else:
                                    print("Your answer must be A or B")
                    else:
                        print("Your answer must be A or B")
            elif decision.lower() == 'b':
                print("I went to Alistair to tell him how he sucked as a person and that I was going to the news to show what kind of person he is. \n")
                time.sleep(1)
                answer = False
                while answer == False:
                    decision = input('What would you like to ask next? \n'
                                     'A: How did Alistair respond to your announcement? \n'
                                     'B: How was the overall tone of your conversation? \n')
                    if decision.lower() == 'a':
                        print("He was surprising calm, and responded with saying that it didn't matter what I did, since he was already a rich and powerful person. \n")
                        time.sleep(1)
                        print('And did you have any thoughts on that? \n')
                        time.sleep(1)
                        print("Yeah, I went off on him saying how he was such a terrible and arrogant person, and he should go screw himself. \n")
                        time.sleep(1)
                        print('Anything else you would like to tell me?')
                        time.sleep(2)
                        print("No, that's all.")
                        time.sleep(1)
                        print('Your interview with the business partner has finished')
                        PartnerInterrogation = True
                        answer = True
                        action = 9
                    elif decision.lower() == 'b':
                        print("I would say that I was pretty heated, while he remained annoyingly calm")
                        time.sleep(1)
                        answer = True
                        answer1 = False
                        while answer1 == False:
                            decision = input('What would you like to ask next? \n'
                                             'A: Did you do anything after the meeting ended? \n'
                                             'B: Was there anything else during the conversation that was suspicious? Someone else maybe? \n')
                            if decision.lower() == 'a':
                                print('No, just went to the bathroom and left. \n')
                                time.sleep(1)
                                if PartnerEvidence == True:
                                    print('Just before you go, could you just write a random blurb for me?')
                                    time.sleep(1)
                                    print('Sure')
                                    time.sleep(1)
                                    print('The style of writing matches the one found in the bathroom hidden compartment.')
                                    time.sleep(3)
                                print('Anything else you would like to tell me?')
                                time.sleep(2)
                                print("No, that's all.")
                                time.sleep(1)
                                print('Your interview with the business partner has finished')
                                PartnerInterrogation = True
                                answer1 = True
                                action = 9
                            elif decision.lower() == 'b':
                                print("No, maybe the butler walked about a few times, but I think that was normal. \n")
                                time.sleep(1)
                                print('Anything else you would like to tell me?')
                                time.sleep(2)
                                print("No, that's all.")
                                time.sleep(1)
                                print('Your interview with the business partner has finished')
                                PartnerInterrogation = True
                                answer1 = True
                                action = 9
                            else:
                                print('Your answer must be A or B')
                    else:
                        print("Your answer must be A or B")
            else:
                print('Your answer must be A or B')
