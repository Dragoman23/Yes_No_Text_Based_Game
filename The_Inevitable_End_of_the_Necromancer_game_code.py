import time
print("NOTE: Type the words surrounded by these '' to make a decision")
print("You slowly wake up in a dark alley. \nYou have no memory of how you got here, but you feel a strange energy, a magic of sorts coursing through your veins. \nYou look around and see a small, glowing amulet lying on the ground next to you. \nAs you pick it up, you feel a surge of power and knowledge flood your mind. \nYou learn you were a great adventurers, but you were betrayed by your own companions and kingdom.")
gold = 0
time.sleep(4)
print("You decide to start seeking revenge on those who betrayed you. \nYou start to use your newfound powers to track down your former companions and kingdom.")
time.sleep(4)
print("Since you let your anger consume you, you unlock the necromancer class. \nThis class allows you to control the bodies and spirit of the people you kill.")
time.sleep(4)
print("You begin your revenge driven quest at level one since your former companions has stolen all of your powers. \nAt level one you are able to control 5 basic dead spirits, as well as control a poisonous mist. \nEvery opponent you touch slowly loses health.")
time.sleep(4)
print("You now have two options: return to the 'guild' to take some quests in hope of learning the whereabouts of your traitorous allies or to 'wander' the lands, claiming the souls of dead soldiers.")
action = input("> ")
if action.lower() == "guild":
    print("You stride into the guild, scaring the living daylight out of the desk attendant. \nAccording to her, your former party claimed you were dead. \nShe runs to tell the guildmaster. \nThe guildmaster invites you into his office and he asks you what really happened. \nAfter you tell him the full story, he asks about your plans for the future. \nYou can 'lie' to the trusting guildmaster or be straightforward and tell him the 'truth'.")
    action = input("> ")
     
    if action.lower() == "lie":
        print("You decide to lie to the guildmaster. \nYou tell him that you are still a warlock and you have no intentions of seeking revenge. \nSatisifed with your answers, the guildmaster gives you 20 gold and lets you carry on.")
        time.sleep(4)
        gold += 20
        print("You return to the main hall of the guild. \nYou walk up to the desk attendant and ask for a book on dark classes. \nAlthough she was confused, the desk attendant give you the book. \nUnknown to you, she tells the guild master about this progression.\nWhile he doesn't directly do anything, but he sends a few spies and rouges to follow you around.")
        time.sleep(2)
        print("You approach the quest board. \nSince you were a powerful Warlock in the past, you are able to take quests up until rank A.")
        time.sleep(1)
        print("On the board there are two quests: A 'D-Rank' quest to hunt rabbits on the outskirts of the Dark Forest or a 'A-Rank' quest to subjugate a goblin village and the their chief, also in the Dark Forest.")
        action = input("> ")
        if action.lower() == "d-rank":
            print("You decide to take the easier, D-Rank quest since you are back at level 1. \nYou gather your gear and the quest map from the front desk and start your journey.")
            time.sleep(2.5)
            print("Once you arrive at the Dark Forest, you start killing rabbits and things are going swimmingly. \n\nThat is until you hear a guttural scream. \n\nAn army of goblin mages and warriors stream out of the forest. \n\nYou try to escape, but in the process you trip on a rabbit you killed. \n\nThe goblins catch up with you and mutilate your body, leaving it for the rabbit to feast on. \n\nTo think you would die because of a body dead rabbit.")
            print("THE END")
        if action.lower() == "a-rank":
            print("Confident in your adventuring skills and the basic multi-class spells you decide to take on the A-Rank quest. \nYou gather your gear and the quest map from the front desk and start you journey.")
            time.sleep(2.5)
            print("Once you arrive in the Dark Forest, you begin to look for the goblin village. \n\nBefore you know it, you are smack dab in the middle of the village, surrounded by rabid goblins.")
            print("You try to stick to your basic multi-class spells, but before you know it those skills become insignificant. \n\nYou are forced to resort to using your new necromancer skills. \n\nLuckily, you are able to escape the Dark Forest safely, with your undead warriors trailing behind you.")
            time.sleep(2.5)
            print("Suddenly, an arrow pierces your throat. \n\nA rouge appears from the trees and whispers in your in your ear 'Compliments of the Guild, evil necromancer. \n\nYou slowly bleed out, regretting the fact that you could never achieve your revenge.")
            print("THE END")
    elif action.lower() == "truth":
        print("You decide to the honest for once and you tell the guild master your true intentions and your necromancer class. \nTurns out the necromancer class is considered a dark class. \nThese dark classes are fated to bring the end of the world. \nThe shocked guildmaster sends out a guild wide bounty. \nYou now have two options: 'Give Up' or 'Run Away'")
        action = input("> ")
        if action.lower() == "give up":
            print("You slowly kneel before the guildmaster. \nYou know that running away would be pointless. \nA group of royal guards arrest you and take you to the royal court. \nAt the court, you are sentenced to death with a public execution. \nAs you kneel on the execution stand, a guillotine blade is held above your head. \n3,2,1! \nYOU HAVE DIED")
            time.sleep(3)
            print("THE END")
           
        if action.lower() == "run away":
            print("Realizing the folly in you actions, you choose to run away and live a life as a fugitive. \nAs a stumble into the slums, your stomach growls loudly. \nYou haven't eaten in days. \nSomewhere to your right, an old man appears. \n'Hungry are we my child. What if told you I had a way for you to make a little bit of cash. All you have to do is to follow me... \nDo you 'follow' or do you 'ignore' the strange old man.")
            action = input("> ")
               
            if action.lower() == "ignore":
                time.sleep(4)
                print("You choose to ignore the strange, old man, but as you walk away he mutters something under his breath. \nDays pass and you can't seem to find a job or food. \nAs you lay dying in a quiet, dark alleyway, the old man appears again. \n'Hello child, you couldn't find job or get a job could you?' \n'How... How did you know that? Who are you?' you ask.' \n'My stupid child, I am the guildmaster of the dark guild. When you first entered the slums, I saw a great potential within you, but you turned me down. In my rage, I cursed you to never find success in this life. Hopefully your next life will be happier.' \nMustering the last bits of your magical energy together, you try to cast a curse, but you fail miserably as the poisonous curse rebounds back towards you, ending your life.")
                time.sleep(4)
                print("THE END")
               
            if action.lower() == "follow":
                print("You choose to follow the strange old man. \nYou follow him a what seems to be a decripit old building, but the second you walk in the setting complete changes. \nThe inside of the building is like the guild hall, but more extravagent. \nThe walls are covered in gold and gems, and dark shades cover every single window. \n'My little necromancer, this is the Dark Guild and I am the guildmaster, Morgan the Dark.' \nHere at the Dark Guild, we shelter people with dark classes, people who the nation can't acknowledge. \nHere we carry out jobs the nation can't publicize: assasinations, murders, theft, economic manipulation, etc. \nTurns out all that nonsense about dark classes ending the world was absolute nonsense, mere government propaganda. \nThis is our compromise: The Dark Guild, open to only those who can find it.")                    
                time.sleep(4)
                print("My child, you now have two options: 'join' this guild and this bloody life or 'leave' and try to survive on your own.")
                action = input("> ")
                if action.lower() == "leave":
                    print("You decide to leave the guild. \nYou don't want to kill everyone, just those who have wronged you. \n'Unfortunately, no one who knows about the exsistence of the Dark Guild is permitted to leave.' \nA strange feeling spreads trhoughout your body. \nYou quickly realize it is a fast acting poison and before you know it, you are dead.")
                    time.sleep(4)
                    print("THE END")
                if action.lower() == "join":
                    print("Smart choice child, no one who leaves the guild survives.")
                    time.sleep(4)
                    print("You have been warned.")
                    time.sleep(4)
                    print("Before you get started, there are a few ground rules we must cover: ")
                    time.sleep(4)
                    print("Every guild member is given one job every two months that they must complete. \nBeside that mission, you are allowed to take missions from the notice board. \nEvery guild member is required to complete atleast 8 missions. \nFail to do so, there will be consequences. \nAdditionally, we ask that you don't not pry into the details of your party members pasts. \nEveryone here has thier own secrets. \nTry not to kill your fellow guild members, but what happens happens. \nThat's it.")
                    time.sleep(4)
                    print("For your first mission, you need to kill Baron Equivialancer of the Algian Territory.")
                    time.sleep(2)
                    print("Since the Baron does have guards you will be working in a team with a Assassin Rogue named Shadow and a Oathbreaker Paladin named Hereticon. \nThey are waiting for you at the bar. Right there.")
                    time.sleep(4)
                    print("'Hello, I am the necromancer you will be working with.' \n'Dammit, another sunny newbie' Shadow mutters under her breath. \n'Be quiet, Shadow. Atleast he has a strong class. Better than the last sacrifice... teammate. I said teammate.' Hereticon utters ominously")
                    time.sleep(4)
                    print("You and your reluctant teammates work out a plan to kill the Baron. \nShadow and you will be using her shared stealth skill to sneak into the manor. \nHereticon will create distraction and try to tank the guards attack. \nOnce inside the manor you will be using your poison gas and shadow soliders to deal with the guards. \nShadow will then use her assassination skill to kill the Baron.")
                    time.sleep(4)
                    print("'Don't you ever wonder what these people did to deserve to die.' You ask")
                    time.sleep(2)
                    print("'We aren't payed to ask questions. Just shut up and get the job down' Shadow replies harshly. \nYou shut up, hoping that you didn't sour the team dynamic.")
                    time.sleep(3)
                    print("You arrive at the manor, and everything is going swimmingly. Shadow just entered the Baron's quarters and you are standing guard outside.")
                    time.sleep(2)
                    print("Suddenly, Shadow burst out of the quarters, running faster than you've ever seen a human run. \n'Run!' she yells. \n'Why?' you ask. \n'Just run, idiot!' she screams back. \nJust as she turned back around, a giant blade cut her in half.")
                    time.sleep(4)
                    print("Out walk a giant beat. \nIt has the head of a lion and the body of a man. \nIt seems like a sphnix...")
                    time.sleep(3)
                    print("The hall fills with its thundering voice: 'Answer my question or die'.")
                    time.sleep(1.5)
                    print("You must now make a decision: 'Stay' and test your luck aganist the beast or 'Run' and hope you make it out alive")
                    action = input("> ")
                    if action.lower() == 'run':
                        print("You try to run away, but the beast voice echos through the halls once again: 'I told you to answer my question'.")
                        time.sleep(2.5)
                        print("The beast's blade, sails through the air, piercing every one of your undead summons. \nSoon enough, the blade piecers you through the heart, pinning you dying body to the wall.")
                        time.sleep(2.5)
                        print("THE END")
                    if action.lower() == 'stay':
                        print("You have decided to stay and try your luck with the beast's question")
                        time.sleep(1)
                        print("'You have made the correct decision staying. \nIf you tried running you would have died before you reached the end of hallway, just like that annoying bug I just killed.")
                        time.sleep(1.5)
                        print("Here is my question:What is the creature that walks on four legs in the morning, two legs in the afternoon, and three legs in the evening?")
                        answer = input("> ")
                        answer_list=['man','humans','humanity', 'people','human']
                        if answer.lower() not in answer_list:
                            print(f"You have failed the riddle of the beast. The acceptable answers were {answer_list}. Now face your death!")
                            time.sleep(3)
                            print("The beast's blade cuts you in two right where you stand.")
                            print("THE END.")
                        if answer.lower() in answer_list:
                            print("You have answered the riddle of the beast correctly.")
                            print("The beast slowly fades into a pile of dust leaving behind a bag with 20 gold pieces and enough experience to get you level 2.")
                            gold += 20
                            time.sleep(3)
                            print("As you level up to level 2, you unlock 3 new skills: \n-You can now control 10 basic dead spirits and 3 intermediate dead spirits \n-You can now temporarily control 25 newly dead bodies \n-You unlock a slow lifesteal ability.")
                            time.sleep(3)
                            print("You quietly enter the Baron's quarters to see him already dead. \nTurns out the beast was a failed experiment and it killed its master will escaping")
                            time.sleep(2)
                            print("You exit the manor to find Hereticon, covered in blood, hopefully the guards' \n'Where is she?' \n'Where is Shadow?' \n'Where is my wife!!?'")
                            time.sleep(2)
                            print("That explains a lot... \n'She died inside the manor to a savage monster.' \n'NOOOOOO, you must be lying! How could she die but you survive?' \n'I know! You must have secretly killed her to increase your own record. You are probably planning to kill me too, but I am going to end you first.' A twisted rage fills Hereticons face. \nYou try to activate your new powers, but your magic power was depleted during the assassination attempt. \nHereticon's greataxe comes down on your head, ending your life.")
                            print("THE END")
    else:
        print("Invalid Choice")
if action.lower() =="wander":
    print("You decide to wander the world to try and find powerful souls. \nYou succesfully find the soul of a powerful warrior, named Roland the Great, but you come across a major issue. \nYou aren't strong enough to control the spirit of Roland and he takes over you body.")
    time.sleep(4)
    print("Your body was taken over by the spirit of a dead man. \nSince your spirit has been destroyed and you have officially passed away.")
    time.sleep(4)
    print("THE END")



#Hero pathway to add later
#action = input("Make a choice: 'Revenge' or 'Hero': ")
#if action.lower() == "revenge":
#elif action.lower() == "hero":
    #print("You decide to use your newfound powers to help others and become a hero. \nYou decide to dedicate your life to protecting the innocent and fighting for justice.")
#print("You slowly wake up in a dark alley. \nYou have no memory of how you got here, but you feel a strange energy, a magic of sorts coursing through your veins. \nYou look around and see a small, glowing amulet lying on the ground next to you. \nAs you pick it up, you feel a surge of power and knowledge flood your mind. \nYou learn you were a great adventurers, but you were betrayed by your own companions and kingdom. \nYou have to make a decision: do you seek revenge on those who betrayed you, or do you use your newfound powers to help others and become a hero? \nThe choice is yours.\n")
#add back the decision path
