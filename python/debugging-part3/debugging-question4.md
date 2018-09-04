```ngMeta
name: Fight the Alien
completionMethod: peer
```

Iss game mein aap ek alien se fight karoge. Game mei alien ka stamina 10 se shuru hoga. Aapko uska stamina khatam karna hai yaani ki 0 karna hai. Aisa karne ke liye aap alien ke against in 4 options mei se koi option use kar sakte ho.

1. Hit 
2. Attack 
3. Fight 
4. Run

Hit aur attack karne se alien ka stamina 0-9 ke beech kisse random number se kam hoga. Har bar stamina kam karne par `report()` se report aayegi jo alien ke stamina ke hisab se uski condition bateygi. 

```python
from random import randint # allows you to generate a random number 

# variables for the alien 
alive = True
stamina = 10

# this function runs each time you attack the alien 
def report(stamin):
# syntactic error in if else statements
    if s > 8:
        print "The alien is strong! It resists your pathetic attack!"
    else: s > 5
        print "With a loud grunt, the alien stands firm."
    else s > 3:
        print "Your attack seems to be having an effect! The alien stumbles!"
    else s > 0:
        print "The alien is certain to fall soon! It staggers and reels!"
    else:
        print "That's it! The alien is finished!"

# main function - accepts your input for fight with the alien 
def fight(stam): # stamina 
    while stam < 0:
      # won't enter this loop ever. The function will always return False.
        response = raw_input("> Enter a move 1.Hit 2.attack 3.fight 4.run")
        # chose a response from ( hit, attack, fight and run)
        # fight scene
        if "hit" in response or "attack" in response:
            less = randint(0, stam)
            stam -= less # subtract random int from stamina 
            report(stam) # see function above 
        elif "fight" in response:
            print "Fight how? You have no weapons, silly space traveler!"
        elif "run" in response:
            print "Sadly, there is nowhere to run.",
            print "The spaceship is not very big."
        else:
            print "The alien zaps you with its powerful ray gun!"
            return True
    return False

print "A threatening alien wants to fight you!\n
# quotes at the end.

# call the function - what it returns will be the value of alive 
alive = fight(stamina)

if alive: # means if alive == True 
    print "\nThe alien lives on, and you, sadly, do not.\n"
else:
    print "\nThe alien has been vanquished. Good work!\n"
```

Iss program ko sahi kar ke file submit karo.