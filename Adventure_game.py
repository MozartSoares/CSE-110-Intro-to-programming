#The additional creativity i made was the various endings being good or bad and showing the player which ending he got with the option to play again to discover new endings.
#Additionally i showed the game for my wife and a friend of mine, both were fascinated with the game and made to the end discovering all possible outcomes.


def main():
    print("Hello player!, welcome to the pydventure game")
    
    character = input("Please first enter your character's name\n")
    
    print(f"Hello {character}, you are about to embark on a journey in search of a legendary treasure hidden on a mysterious island.\n"
          f"You will be challenged by a myriad of monsters, and you will have to fight your way through the dangers of the island to find the treasure.\n"
          f"Good luck, {character}!\n")
    
    while True:
        first_choice = ""
        while first_choice not in ["A", "B", "C"]:
            first_choice = input("""
                                As you traverse the forest, you encounter a series of obstacles. Ahead of you, 
                                there are three paths diverging
                                A: A NARROW ROCKY PATH LEADING UPHILL, SURROUNDED BY THORNY BUSHES.
                                B: A DARK, OMINOUS CAVE ENTRANCE, EMITTING STRANGE SOUNDS FROM WITHIN.
                                C: A RICKETY ROPE BRIDGE SPANNING A DEEP CHASM, SWAYING OMINOUSLY IN THE WIND.
                                Which path do you take? (please answer with A/B/C)\n
                                """).upper()
            if first_choice not in ["A", "B", "C"]:
                print("Please enter a valid option (A, B, or C).\n")
        
        if first_choice == "A":
            second_choice = ""
            while second_choice not in ["A", "B"]:
                second_choice = input("""
                                    You cautiously make your way up the narrow rocky path. As you climb higher, you stumble upon an ancient altar covered in moss. 
                                    At its base lies a weathered map.
                                    You have two choices from here:
                                    A: EXAMINE THE MAP CLOSELY.
                                    B: CONTINUE ASCENDING THE PATH WITHOUT INVESTIGATING THE ALTAR. 
                                    (please answer with A/B)\n
                                    """).upper()
                if second_choice not in ["A", "B"]:
                    print("Please enter a valid option (A or B).\n")
            
            if second_choice == "A":
                third_choice = ""
                while third_choice not in ["A", "B"]:
                    third_choice = input("""
                                        You examine the map closely and decipher its cryptic markings. It reveals the location of a hidden cave deep within the forest.
                                        You decide to head towards the hidden cave. As you enter, you notice two paths.
                                        A: GO LEFT.
                                        B: GO RIGHT.
                                        (please answer with A/B)\n
                                        """).upper()
                    if third_choice not in ["A", "B"]:
                        print("Please enter a valid option (A or B).\n")
                
                if third_choice == "A":
                    game_over("You were ambushed by a group of bandits while exploring the cave.", 1)
                elif third_choice == "B":
                    victory("You found a chamber filled with ancient artifacts, although not the legendary treasure you sought initially.","alternate")
            
            elif second_choice == "B":
                third_choice = ""
                while third_choice not in ["A", "B"]:
                    third_choice = input("""
                                        As you proceed further, you encounter a fork in the path.
                                        A: TAKE THE LEFT FORK.
                                        B: TAKE THE RIGHT FORK.
                                        (please answer with A/B)\n
                                        """).upper()
                    if third_choice not in ["A", "B"]:
                        print("Please enter a valid option (A or B).\n")
                
                if third_choice == "A":
                    game_over("You got lost in the maze-like passages and were unable to find your way out.", 2)
                elif third_choice == "B":
                    victory("You stumbled upon a hidden cave containing valuable gems and artifacts, this is the real treasure you came looking for !.","real")
            
        elif first_choice == "B":
            second_choice = ""
            while second_choice not in ["A", "B"]:
                second_choice = input("""
                                    You steel yourself and enter the dark cave, the sound of your footsteps echoing ominously. Inside, you find yourself in a labyrinth of twisting passages. 
                                    Suddenly, you hear a low growl emanating from the shadows."
                                    You have two choices from here:
                                    A: FOLLOW THE SOUND OF THE GROWL.
                                    B: RETREAT AND EXIT THE CAVE IMMEDIATELY.
                                    (please answer with A/B)\n
                                    """).upper()
                if second_choice not in ["A", "B"]:
                    print("Please enter a valid option (A or B).\n")
            
            if second_choice == "A":
                third_choice = ""
                while third_choice not in ["A", "B"]:
                    third_choice = input("""
                                        You stumble upon a large cavern where the source of the growl awaits you.
                                        A: FIGHT THE CREATURE.
                                        B: ATTEMPT TO FLEE.
                                        (please answer with A/B)\n
                                        """).upper()
                    if third_choice not in ["A", "B"]:
                        print("Please enter a valid option (A or B).\n")
                
                if third_choice == "A":
                    game_over("The creature proved to be too powerful and overwhelmed you in combat.", 3)
                elif third_choice == "B":
                    game_over("You attempted to flee but found yourself trapped in a dead end.", 4)
            
            elif second_choice == "B":
                third_choice = ""
                while third_choice not in ["A", "B"]:
                    third_choice = input("""
                                        As you exit the cave, you find yourself at a crossroads.
                                        A: HEAD DEEPER INTO THE FOREST.
                                        B: EXPLORE THE OUTSKIRTS OF THE CAVE.
                                        (please answer with A/B)\n
                                        """).upper()
                    if third_choice not in ["A", "B"]:
                        print("Please enter a valid option (A or B).\n")
                
                if third_choice == "A":
                    game_over("You encountered a hostile tribe deep in the forest and were unable to negotiate your way out.", 5)
                elif third_choice == "B":
                    victory("You discovered an exit that leads you to a secluded part of the island, where you find a hidden stash of treasure.","hidden stash")
            
        elif first_choice == 'C':
            second_choice = ""
            while second_choice not in ["A", "B"]:
                second_choice = input("""
                                    With trepidation, you step onto the swaying rope bridge, the chasm yawning below you. Midway across, the bridge begins to creak alarmingly, 
                                    threatening to give way at any moment."
                                    You have two choices from here:
                                    A: PRESS ON AND QUICKEN YOUR PACE.
                                    B: RETREAT BACK TO SOLID GROUND WHILE YOU STILL CAN.
                                    (please answer with A/B)\n
                                    """).upper()
                if second_choice not in ["A", "B"]:
                    print("Please enter a valid option (A or B).\n")
            
            if second_choice == "A":
                third_choice = ""
                while third_choice not in ["A", "B"]:
                    third_choice = input("""
                                        As you press forward, the bridge begins to creak alarmingly, threatening to give way at any moment but you manage to get to the other side.
                                        you look at your phone and realize it's about to die
                                        From here you have two options
                                        A: GIVE UP AND CALL YOUR FRIEND WHILE YOU STILL CAN FOR BACKUP TO RETURN HOME
                                        B: TRY TO SURVIVE AND GO AFTER THE TREASURE EVEN THOUGH YOU'RE STRANDED IN A ROCK ISLAND
                                        (please answer with A/B)\n
                                    """).upper()
                    if third_choice not in ["A", "B"]:
                        print("Please enter a valid option (A or B).\n")
                
                if third_choice == "A":
                    victory("you manage to call your friend for backup and flew away from the island leaving the treasure behind but at least you're still alive.", "coward's")
                elif third_choice == "B":
                    game_over("You try to survive and realize your phone's dead so you die all by yourself in the island, sometimes it's better to be a coward and run away than trying to do the impossible", 6)
            elif second_choice == "B":
                third_choice = ""
                while third_choice not in ["A", "B"]:
                    third_choice = input("""
                                    After retreating, you notice a hidden path leading deeper into the forest.
                                    A: EXPLORE THE HIDDEN PATH.
                                    B: CONTINUE EXPLORING THE AREA AROUND THE CAVE.
                                    (please answer with A/B)\n
                                    """).upper()
                    if third_choice not in ["A", "B"]:
                        print("Please enter a valid option (A or B).\n")
                
                if third_choice == "A":
                    game_over("You were bitten by poisonous snakes while exploring the hidden path.", 7)
                elif third_choice == "B":
                    victory("You discovered an ancient shrine hidden within the cave, adorned with valuable artifacts and treasures.","ancient shrine")
            else:
                print("Please enter a valid answer.")

def game_over(reason, final):
    print(f"Game Over. {reason} You discovered ending {final} out of 7 possible game overs. Would you like to play again?")
    play_again = input("YES or NO?\n").lower()
    if play_again == "yes":
        main()
    else:
        print("Thank you for playing!")
        exit()

def victory(outcome, treasure):
    print(f"Congratulations! {outcome} You discovered the {treasure} treasure !, there are many treasures to be found in the island, Would you like to play again?")
    play_again = input("YES or NO?\n").lower()
    if play_again == "yes":
        main()
    else:
        print("Thank you for playing!")
        exit()

main()
