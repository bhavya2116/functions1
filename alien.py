from random import randint 

alive = True
stamin = 10

def report(stamin):
    print(stamin)
    if stamin > 8:
        print ("The alien is strong! It resists your pathetic attack!")
    elif stamin > 5:
        print ("With a loud grunt, the alien stands firm.")
    elif stamin > 3:
        print ("Your attack seems to be having an effect! The alien stumbles!")
    elif stamin > 0:
        print ("The alien is certain to fall soon! It staggers and reels!")
    else:
        print ("That's it! The alien is finished!")
# main function - accepts your input for fight with the alien
def fight(stam): 
    while stam > 0:
        response = input("> Enter a move 1.hit 2.attack 3.Fight 4.run: ")
        if "hit" in response or "attack" in response:
            less = randint(0, stam)
            stam -= less # subtract random int from stamina
            report(stam) # see function above
        elif "fight" in response:
            print ("Fight how? You have no weapons, silly space traveler!")
        elif "run" in response:
            print ("Sadly, there is nowhere to run."),
            print ("The spaceship is not very big.")
        else:
            print ("The alien zaps you with its powerful ray gun!")

print ("A threatening alien wants to fight you!\n")
# call the function - what it returns will be the value of alive
alive = fight(stamin)

if alive: # means if alive == True
    print ("\n still The alien lives on, sadly you loss")
else:
    print ("\nThe alien has been vanquished. Good work!\n")

