# Challenge One: The Mining Engine


"""
PROCEDURE mining(inventoryPick, gem_inventory, gemstones, rarity) {
    DISPLAY "You head down to the mines..."
    
    IF (inventoryPick = "basic"){
        start_percent ← 30
    } ELSE IF (inventoryPick = "good"){
        start_percent ← 50
    } ELSE IF (inventoryPick = "better"){
        start_percent ← 70
    } ELSE {
        start_percent ← 90
    }
    
    DISPLAY "You swing your pick at the rock..."
    
    chance ← start_percent
    keepSwinging ← "y"
    
    REPEAT UNTIL (keepSwinging ≠ "y" AND keepSwinging ≠ "Y") {
        DISPLAY "Swing? Y/N"
        keepSwinging ← INPUT()
        
        IF (keepSwinging = "y" OR keepSwinging = "Y") {
            DISPLAY "You reveal a little more gemstone..."
            chance ← chance + 5
        }
        ELSE {
            roll ← RANDOM(1, 100)
            
            IF (roll ≤ chance) {
                // Pick a random gem and rarity using 1-based indexing
                gem_name ← gemstones[RANDOM(1, LENGTH(gemstones))]
                gem_rarity ← rarity[RANDOM(1, LENGTH(rarity))]
                
                DISPLAY "You carefully uncover a " + gem_name + "!"
                
                // Append as a list: [Name, Value, Rarity]
                newGem ← [gem_name, 0, gem_rarity] 
                APPEND(gem_inventory, newGem)
            }
            ELSE {
                DISPLAY "Unlucky! Your wild swings crack the gem. You'll have to return and try again."
            }
        }
    }
}
"""

import random

def mining(inventory_pick, gem_inventory):
    gemstones = ["diamond", "ruby", "emerald", "topaz", "onyx", "opal", "turquoise", "lapis lazuli"]
    rarity = ["common", "uncommon", "rare", "unique", "fake"]
    value = ["1$", "5$", "10$", "25$", "50$", "100$"]

    inventory_pick = 0
    start_percent = 0

    print("You head down the mines...")
    if(inventory_pick == "basic"):
        start_percent = 30
    elif(inventory_pick == "good"):
        start_percent = 50
    elif(inventory_pick == "better"):
        start_percent = 70
    else: 
        start_percent = 90
    
    
    print("You swing your pick at the rock...")
    
    chance = start_percent
    keepSwinging = "y"
    
    keepSwinging = input("Swing? Y/N: ")
    while (keepSwinging == "y" or keepSwinging == "Y"):
        
        if (keepSwinging == "y" or keepSwinging == "Y"):
            print("You reveal a little more gemstone...")
            chance = chance + 5
        
        else:
            roll = random.randint(1, 100)
            
            if (roll <= chance):
                random.randint = gemstones and rarity and value
                gem_name = gemstones[random.randint(1, len(gemstones))]
                gem_rarity = rarity[random.randint(1, len(rarity))]
                gem_value = value[random.randint(1, len(value))]

                print("You carefully uncover a" + gem_name + "!")
                
                list.append: [gem_name, gem_value, gem_rarity]
                newGem = [gem_name, 0, gem_rarity, gem_value] 
                list.append(gem_inventory, newGem)
            
            else:
                print("Unlucky! Your wild swings crack the gem. You'll have to return and try again.") 
        