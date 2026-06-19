print("You slowly wake up in a dark alley. \nYou have no memory of how you got here, but you feel a strange energy, a magic of sorts coursing through your veins. \nYou look around and see a small, glowing amulet lying on the ground next to you. \nAs you pick it up, you feel a surge of power and knowledge flood your mind. \nYou learn you were a great adventurers, but you were betrayed by your own companions and kingdom. \nYou have to make a decision: do you seek revenge on those who betrayed you, or do you use your newfound powers to help others and become a hero? \nThe choice is yours.\n")
gold = 0
action = input("Make a choice: 'Revenge' or 'Hero': ")
if action.lower() == "revenge":
    print("You decide to seek revenge on those who betrayed you. \nYou start to use your newfound powers to track down your former companions and kingdom, and you unleash your wrath upon them.")
    print("Since you let your anger consume you, you unlock the necromancer class. \nThis class allows you to control the bodies and spirit of the people you kill.")
    print("You begin your revenge driven quest at level one since your former companions has stolen all of your powers. \nAt level one you are able to control 5 dead spirits, as well as control a poisonous mist. \nEvery opponent you touch slowly loses health.")
    print("You now have two options: return to the 'guild' to take some quests in hope of learning the whereabouts of your traitorous allies or to 'wander' the lands, claiming the souls of dead soldiers.")
    action = input("> ")
    if action.lower() == "guild":
        print("You stride into the guild, scaring the living daylight out of the desk attendant. \nAccording to her, your former party claimed you were dead. \nShe runs to tell the guildmaster. \nThe guildmaster invites you into his office and he asks you what really happened. \nAfter you tell him the full story, he asks about your plans for the future. \nYou can 'lie' to the trusting guildmaster or be straightforward and tell him the 'truth'.")
        action = input("> ")
        if action.lower() == "lie":
            print("You decide to lie to the guildmaster. \nYou tell him that you are still a warlock and you have no intentions of seeking revenge. \nSatisifed with your answers, the guildmaster gives you 20 gold and lets you carry on.")
            gold += 20
            print("You return to the main hall of the guild. \nYou walk up to the desk attendatn and ask for a book on dark classes. \nAlthough she was confused, the desk attendant give you the book. \nUnknown to you, she tells the guild master about this progression.\nWhile he doesn't directly do anything, but he sends a few spies and rouges to follow you around.")


        if action.lower == "truth":
            print("You decide to the honest for once and you tell the guild master your true intentions and your necromancer class. \nTurns out the necromancer class is considered a dark class. \nThese dark classes are fated to bring the end of the world. \nThe shocked guildmaster sends out a guild wide bounty. \nYou now have two options: 'Give Up' or 'Run Way'")
            action = input("> ")
            if action.lower() == "give up":
                print("You slowly kneel before the guildmaster. \nYou know that running away would be pointless. \nA group of royal guards arrest you and take you to the royal court. \nAt the court, you are sentenced to death with a public execution. \nAs you kneel on the execution stand, a guillotine blade is held above your head. \n3,2,1! \nYOU HAVE DIED")
                print("THE END")
            if action.lower() == "run away":
                print("Realizing the folly in you actions, you choose to run away and live a life as a fugitive. \nAs a stumble into the slums, your stomach growls loudly. \nYou haven't eaten in days. \nSomewhere to your right, an old man appears. \n'Hungry are we my boy. What if told you I had a way for you to make a little bit of cash. All you have to do is to follow me... \nDo you 'follow' or do you 'ignore' the strange old man.")

    if action.lower() =="wander":
        print("You decide to wander the world to try and find powerful souls. \nYou succesfully find the soul of a powerful warrior, named Roland the Great, but you come across a major issue. \nYou aren't strong enough to control the spirit of Roland and he takes over you body.")
        print("Your body was taken over by the spirit of a dead man. \nSince your spirit has been destroyed and you have officially passed away.")
        print("THE END")

elif action.lower() == "hero":
    print("You decide to use your newfound powers to help others and become a hero. \nYou decide to dedicate your life to protecting the innocent and fighting for justice.")